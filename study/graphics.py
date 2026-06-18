######################## module_turtle.py ########################
import turtle
import random
import math
import colorsys

# -----------------------------
# SETTINGS
# -----------------------------
W, H = 1200, 800
BG = "#05060a"
SEED = 7

random.seed(SEED)

# ✅ ONE screen only
screen = turtle.Screen()
screen.setup(W, H)
screen.bgcolor(BG)
screen.title("Complex Turtle Generative Art (fractal + spiro + golden spiral + mandala)")
screen.tracer(0, 0)
screen.colormode(1.0)

# ✅ ONE turtle only
pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.width(1)
pen.penup()

# -----------------------------
# COLOR HELPERS
# -----------------------------
def hsv(h, s=1.0, v=1.0):
    r, g, b = colorsys.hsv_to_rgb(h % 1.0, max(0, min(1, s)), max(0, min(1, v)))
    return (r, g, b)

def glow_dot(x, y, base_r, layers, hue, jitter=0.0):
    for i in range(layers, 0, -1):
        rr = base_r * (i / layers)
        h = hue + random.uniform(-0.01, 0.01)
        s = 0.9
        v = 0.2 + 0.8 * (i / layers)
        pen.goto(x + random.uniform(-jitter, jitter), y + random.uniform(-jitter, jitter))
        pen.dot(rr * 2, hsv(h, s, v))

# -----------------------------
# 1) FRACTAL CORAL / TREE
# -----------------------------
def coral_branch(x, y, heading, length, depth, hue, spread=28):
    if depth <= 0 or length < 2:
        glow_dot(x, y, base_r=3, layers=6, hue=hue, jitter=1.2)
        return

    pen.goto(x, y)
    pen.setheading(heading)
    pen.pendown()

    s = 0.7
    v = 0.3 + 0.7 * (depth / 10.0)
    pen.pencolor(hsv(hue + depth * 0.015, s, v))
    pen.width(max(1, int(depth * 0.7)))

    steps = int(max(6, length / 5))
    step_len = length / steps
    wobble = 6.0 / (depth + 1)

    for _ in range(steps):
        pen.left(random.uniform(-wobble, wobble))
        pen.forward(step_len)

    pen.penup()
    x2, y2 = pen.position()

    n = 2 + (1 if random.random() < 0.35 else 0)
    for _ in range(n):
        ang = random.uniform(-spread, spread)
        shrink = random.uniform(0.62, 0.78)
        coral_branch(x2, y2, heading + ang, length * shrink, depth - 1, hue, spread=spread + 1.2)

def draw_coral():
    base_y = -H * 0.40
    for i in range(5):
        x = random.uniform(-W * 0.38, W * 0.38)
        hue = 0.55 + i * 0.06
        length = random.uniform(170, 260)
        depth = random.randint(7, 10)
        coral_branch(x, base_y, 90 + random.uniform(-6, 6), length, depth, hue, spread=random.uniform(22, 35))

# -----------------------------
# 2) SPIROGRAPH ROSETTES
# -----------------------------
def spiro(center_x, center_y, R, r, d, loops, hue):
    pen.goto(center_x, center_y)
    pen.setheading(0)
    pen.width(2)
    pen.pendown()
    steps = 2600

    for i in range(steps * loops):
        tt = i * (2 * math.pi / steps)
        x = (R - r) * math.cos(tt) + d * math.cos(((R - r) / r) * tt)
        y = (R - r) * math.sin(tt) - d * math.sin(((R - r) / r) * tt)

        pen.pencolor(hsv(hue + i / (steps * loops) * 0.25, 0.95, 0.95))
        pen.goto(center_x + x, center_y + y)

    pen.penup()

def draw_spiros():
    for k in range(4):
        cx = random.uniform(-W * 0.25, W * 0.25)
        cy = random.uniform(-H * 0.1, H * 0.25)
        R = random.uniform(90, 160)
        r = random.uniform(25, 60)
        d = random.uniform(40, 120)
        loops = random.choice([2, 3, 4])
        hue = random.uniform(0.05, 0.25) + k * 0.05
        spiro(cx, cy, R, r, d, loops, hue)

# -----------------------------
# 3) GOLDEN ANGLE "GALAXY"
# -----------------------------
def draw_galaxy(cx=0, cy=0, n=1600, scale=9.5, hue0=0.82):
    golden_angle = math.pi * (3 - math.sqrt(5))
    for i in range(1, n + 1):
        r = scale * math.sqrt(i)
        a = i * golden_angle
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a)

        hue = hue0 + (i / n) * 0.12
        radius = 1.2 + 3.2 * (1 - i / n)
        glow_dot(x, y, base_r=radius, layers=6, hue=hue, jitter=0.6)

# -----------------------------
# 4) MANDALA
# -----------------------------
def mandala(cx, cy, rings=8, petals=18, base_radius=40, hue=0.35):
    for ring in range(rings):
        rr = base_radius + ring * 28
        pet = petals + ring * 3
        pen.width(2)

        for p in range(pet):
            ang = (360 / pet) * p
            wob = random.uniform(-5, 5)
            pen.goto(cx, cy)
            pen.setheading(ang + wob)
            pen.pendown()
            pen.pencolor(hsv(hue + ring * 0.03 + p / pet * 0.06, 0.9, 0.9))

            a = rr * random.uniform(0.85, 1.05)
            b = rr * random.uniform(0.25, 0.45)
            pen.forward(a)
            pen.left(65)
            pen.forward(b)
            pen.left(50)
            pen.forward(b)
            pen.forward(-b)
            pen.right(50)
            pen.forward(-b)
            pen.forward(-a)

            pen.penup()

        for _ in range(140):
            th = random.random() * 2 * math.pi
            x = cx + rr * math.cos(th)
            y = cy + rr * math.sin(th)
            glow_dot(x, y, base_r=1.5, layers=4, hue=hue + ring * 0.03, jitter=0.4)

# -----------------------------
# MAIN
# -----------------------------
def main():
    for _ in range(900):
        x = random.uniform(-W/2, W/2)
        y = random.uniform(-H/2, H/2)
        h = random.uniform(0.55, 0.95)
        pen.goto(x, y)
        pen.dot(random.choice([1, 1, 2]), hsv(h, 0.2, random.uniform(0.3, 0.9)))

    draw_galaxy(0, 30, n=1700, scale=10.5, hue0=0.78)
    draw_spiros()
    mandala(0, 40, rings=7, petals=16, base_radius=45, hue=0.28)
    draw_coral()

    screen.update()
    print("Done.")

main()

# ✅ ONLY ONE of these (use done)
turtle.done()
