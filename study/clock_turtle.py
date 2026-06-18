import turtle
import time
import math

# =========================
# SETTINGS
# =========================
W, H = 700, 700
R = 260  # clock radius
BG = "#0b0f1a"
FG = "#e8eefc"

screen = turtle.Screen()
screen.setup(W, H)
screen.title("Live Turtle Clock")
screen.bgcolor(BG)
screen.tracer(0, 0)

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.penup()

hand = turtle.Turtle(visible=False)
hand.speed(0)
hand.penup()

label = turtle.Turtle(visible=False)
label.speed(0)
label.penup()

# =========================
# HELPERS
# =========================
def goto(p, x, y):
    p.penup()
    p.goto(x, y)

def draw_circle_outline(radius, thickness=6):
    pen.pensize(thickness)
    pen.pencolor(FG)
    goto(pen, 0, -radius)
    pen.setheading(0)
    pen.pendown()
    pen.circle(radius)
    pen.penup()

def draw_ticks():
    # Hour ticks
    pen.pencolor(FG)
    for i in range(60):
        angle = 90 - i * 6  # 12 o'clock is 90 degrees
        length = 18 if i % 5 == 0 else 8
        thickness = 4 if i % 5 == 0 else 2

        pen.pensize(thickness)
        pen.setheading(angle)
        goto(pen, 0, 0)
        pen.forward(R - 12)
        pen.pendown()
        pen.forward(-length)
        pen.penup()

def draw_numbers():
    pen.pencolor(FG)
    pen.pensize(1)
    for n in range(1, 13):
        angle = math.radians(90 - n * 30)
        x = math.cos(angle) * (R - 52)
        y = math.sin(angle) * (R - 52)
        goto(pen, x, y - 12)
        pen.write(str(n), align="center", font=("Arial", 20, "bold"))

def draw_center():
    # center cap
    pen.pencolor(FG)
    pen.fillcolor(FG)
    goto(pen, 0, 0)
    pen.begin_fill()
    pen.dot(18)
    pen.end_fill()

def clear_hands():
    hand.clear()
    label.clear()

def draw_hand(angle_deg, length, thickness, color):
    hand.pensize(thickness)
    hand.pencolor(color)
    goto(hand, 0, 0)
    hand.setheading(angle_deg)
    hand.pendown()
    hand.forward(length)
    hand.penup()

def draw_clock_face():
    pen.clear()
    draw_circle_outline(R, thickness=7)
    draw_ticks()
    draw_numbers()
    draw_center()
    screen.update()

# =========================
# MAIN LOOP
# =========================
def update():
    clear_hands()

    now = time.localtime()
    h = now.tm_hour % 12
    m = now.tm_min
    s = now.tm_sec

    # Smooth movement (use fractional seconds)
    frac = time.time() % 1.0
    s_smooth = s + frac
    m_smooth = m + s_smooth / 60.0
    h_smooth = h + m_smooth / 60.0

    # Angles: 12 o'clock = 90 degrees
    sec_angle = 90 - (s_smooth * 6)
    min_angle = 90 - (m_smooth * 6)
    hour_angle = 90 - (h_smooth * 30)

    # Draw hands (hour, min, sec)
    draw_hand(hour_angle, R * 0.55, 8, FG)
    draw_hand(min_angle,  R * 0.78, 5, FG)
    draw_hand(sec_angle,  R * 0.90, 2, "#ff4d6d")

    # Digital time + date
    timestr = time.strftime("%H:%M:%S", now)
    datestr = time.strftime("%a %d %b %Y", now)

    goto(label, 0, -R - 55)
    label.pencolor(FG)
    label.write(timestr, align="center", font=("Arial", 22, "bold"))

    goto(label, 0, -R - 85)
    label.pencolor("#a9b7e6")
    label.write(datestr, align="center", font=("Arial", 14, "normal"))

    # Redraw center cap on top
    pen.pencolor(FG)
    goto(pen, 0, 0)
    pen.dot(18, FG)

    screen.update()

    # schedule next frame (about 30 fps)
    screen.ontimer(update, 33)

# Draw static face once, then animate
draw_clock_face()
update()
turtle.done()
