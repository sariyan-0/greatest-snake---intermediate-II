import os
import time
from dataclasses import dataclass, field
from typing import List, Dict, Optional

from openai import OpenAI
# pip install openai (use this)


# -----------------------------
# Config
# -----------------------------

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = "gpt-4.1-mini"  # "gpt-4.1-nano" is even cheaper/faster
MAX_TURNS_TO_KEEP = 8  # keep last N turns so follow-ups still work


BEGINNER_STYLE_RULES = """\
Write ULTRA-SIMPLE Python code like an intro programming class (weeks 1-4 material):
- ONLY use: simple variables (a, x, total, count), print(), input(), basic math (+, -, *, /, %)
- ONLY use: if/elif/else, for loops with range() or lists, while loops
- ONLY use: lists with [], basic list operations (append, simple indexing)
- Use VERY simple variable names: a, b, x, y, total, count, num, item, i
- Keep code SHORT (5-15 lines max for most tasks)
- NO functions unless specifically requested
- NO list comprehensions, NO classes, NO dictionaries (unless essential)
- NO 'with' statements, NO try/except, NO imports (unless absolutely needed like random)
- NO fancy features - pretend you're teaching a complete beginner
- Add simple comments only when needed to explain logic
- Output ONLY the final Python code (no explanations, no markdown fences, no extra text)
"""


SYSTEM_PROMPT = """\
You are a coding tutor for absolute beginners. Generate ONLY ultra-simple Python code.
Think: "What would I write in week 1-2 of an intro programming class?"
Keep it as basic and straightforward as possible. Use simple variable names like a, x, total, num.
No explanations, no markdown. Just clean, simple code that a beginner can understand immediately.
Output ONLY code.
"""


@dataclass
class Session:
    model: str = DEFAULT_MODEL
    history: List[Dict[str, str]] = field(default_factory=list)  # list of {"role": "...", "content": "..."}
    last_code: str = ""

    def push(self, role: str, content: str):
        self.history.append({"role": role, "content": content})
        # Keep history small
        if len(self.history) > MAX_TURNS_TO_KEEP * 2:
            self.history = self.history[-MAX_TURNS_TO_KEEP * 2 :]




def build_input(session: Session, user_question: str) -> List[Dict[str, str]]:
    # We feed a mini conversation: system -> style rules -> history -> question
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "system", "content": BEGINNER_STYLE_RULES},
    ]
    messages.extend(session.history)
    messages.append({"role": "user", "content": user_question})
    return messages


def generate_code(client: OpenAI, session: Session, user_question: str) -> str:
    # Responses API call. We request text output and try to hard-enforce "code only".
    # Docs: https://platform.openai.com/docs/api-reference/responses  (not linked here per policy)
    inp = build_input(session, user_question)

    resp = client.responses.create(
        model=session.model,
        input=inp,
        temperature=0.2,
        max_output_tokens=1200,
    )

    # The SDK exposes response text conveniently via output_text in many examples.
    # If unavailable in your version, fall back to parsing.
    code = getattr(resp, "output_text", None)
    if not code:
        # Fallback: best-effort parse
        try:
            parts = []
            for item in resp.output:
                if item.type == "message":
                    for c in item.content:
                        if c.type == "output_text":
                            parts.append(c.text)
            code = "\n".join(parts).strip()
        except Exception:
            code = str(resp)

    # Tiny cleanup: remove accidental markdown fences if the model slips
    code = code.strip()
    if code.startswith("```"):
        code = code.strip("`")
        # remove an initial 'python' label if present
        if code.lower().startswith("python"):
            code = code[6:].lstrip()
    return code.strip()


def print_menu(session: Session):
    print("\n=== Code Tutor CLI ===")
    print(f"Model: {session.model}")
    print("1) Ask a question (get code)")
    print("2) Follow-up (uses chat memory)")
    print("3) Switch model (gpt-4.1-mini / gpt-4.1-nano)")
    print("4) Save last code to file")
    print("5) Clear memory")
    print("0) Exit")


def switch_model(session: Session):
    print("\nEnter model name (suggestions: gpt-4.1-mini, gpt-4.1-nano):")
    m = input("> ").strip()
    if m:
        session.model = m
        print(f"OK, model set to: {session.model}")
    else:
        print("No change.")


def save_last_code(session: Session):
    if not session.last_code:
        print("No code to save yet.")
        return
    filename = input("Save as (e.g. answer.py): ").strip()
    if not filename:
        print("Cancelled.")
        return
    with open(filename, "w", encoding="utf-8") as f:
        f.write(session.last_code)
    print(f"Saved to {filename}")


def clear_memory(session: Session):
    session.history = []
    session.last_code = ""
    print("Memory cleared.")


def get_multiline_input(prompt: str) -> str:
    """Read multi-line input. Press Enter twice (empty line) to finish."""
    print(prompt)
    print("(Press Enter twice when done, or paste multiple lines)")
    lines = []
    while True:
        line = input()
        if line == "":
            if lines:  # If we have content and get empty line, we're done
                break
            # If first line is empty, keep waiting
        else:
            lines.append(line)
    return "\n".join(lines).strip()


def main():
    client = OpenAI(api_key=OPENAI_API_KEY)
    session = Session()

    while True:
        print_menu(session)
        choice = input("> ").strip()

        if choice == "0":
            print("Bye.")
            break

        elif choice == "1":
            q = get_multiline_input("\nQuestion (describe what code you want):")
            if not q:
                continue

            code = generate_code(client, session, q)
            session.push("user", q)
            session.push("assistant", code)
            session.last_code = code

            print("\n----- GENERATED CODE -----\n")
            print(code)
            print("\n--------------------------\n")

        elif choice == "2":
            if not session.history:
                print("No memory yet. Use option 1 first.")
                continue
            q = get_multiline_input("\nFollow-up (e.g. 'make it use a for loop' / 'fix my bug'):")
            if not q:
                continue

            code = generate_code(client, session, q)
            session.push("user", q)
            session.push("assistant", code)
            session.last_code = code

            print("\n----- GENERATED CODE -----\n")
            print(code)
            print("\n--------------------------\n")

        elif choice == "3":
            switch_model(session)

        elif choice == "4":
            save_last_code(session)

        elif choice == "5":
            clear_memory(session)

        else:
            print("Pick 0–5.")


if __name__ == "__main__":
    main()
