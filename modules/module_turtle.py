######################## module_turtle.py ########################
# This module provides a simple interface to the turtle graphics library.
import turtle
import random

screen = turtle.Screen()
turtle.hideturtle()  # Hide the turtle cursor
t = turtle.Turtle()
# ------------------------------
# t.forward(200)  # Move the turtle forward by 200 units
# t.left(90) # Move the turtle to the left
# t.forward(200)
# t.left(90)
# t.forward(200)
# t.left(90)
# t.forward(200)

# for i in range(4):
#     t.forward(200)
#     t.left(90)
# ------------------------------
# create a triangle
# for i in range(3):
#     t.forward(200)
#     t.left(60)
# ------------------------------
# create a hexagon
# for i in range(6):
#     t.forward(200)
#     t.left(60)
#     t.forward(200)
# ------------------------------
#create a 36 sided polygon
# for i in range(36):
#     t.forward(20)
#     t.left(10)
# ------------------------------
# create a star art that has infinite loops
# for i in range(1000):
#     t.forward(200)
#     t.left(170)
#     t.forward(220)
#     t.left(170)
#     t.backward(260)
#     t.right(175)
# ------------------------------
# create a spiral art that has infinite loops
# t.speed(0)  # Set the turtle's speed to the maximum
# t.color("blue")  # Set the turtle's color to red
# for j in range(1000000):
#     for i in range(10):
#         t.forward(200)
#         t.left(90)
#     t.left(1)
# ------------------------------
# t.speed(0)
# lst_colors = ["red", "blue", "green", "yellow", "cyan", "magenta"]
# for j in range(72):
#     t.color(random.choice(lst_colors))
#     for i in range(10):
#         t.forward(200)
#         t.left(90)
#     t.left(5)
# ------------------------------
# create a line that rotates around the inside of itself (the value should reduce by 10 each time).
# t.speed(0)
# length = 200
# for i in range(20): 
#     t.forward(length)
#     t.left(90)
#     length = length - 10
# ------------------------------
# create a infinity spiral circle
# t.speed(0)

# length = 20
# while length > 0:
#     t.forward(length)
#     t.left(5)     
#     length -= 0.01
# ------------------------------
# race game between 4 turtles
# t_1 = turtle.Turtle()
# t_1.penup()  # Lift the pen to avoid drawing
# t_1.color("red")
# t_1.goto(-300, 300)
# t_1.pendown()  # Lower the pen to start drawing

# t_2 = turtle.Turtle()
# t_2.penup()
# t_2.color("blue")
# t_2.goto(-300, 100)
# t_2.pendown()

# t_3 = turtle.Turtle()
# t_3.penup()
# t_3.color("green")  
# t_3.goto(-300, -100)
# t_3.pendown()

# t_4 = turtle.Turtle()
# t_4.penup()
# t_4.color("cyan")
# t_4.goto(-300, -300)
# t_4.pendown()

# t_end = turtle.Turtle()
# t_end.penup()
# t_end.goto(300, -300)
# t_end.pendown()
# t_end.left(90)
# t_end.forward(600)
# t_end.hideturtle()

# lst = [20, 80, 5 , 45, 15, 30, 60, 10, 50, 25]
# while True:
#     t_1.forward(random.choice(lst))
#     pos_1 = t_1.position()
#     if pos_1[0] >= 300:
#         print("Red wins!")
#         break
#     t_2.forward(random.choice(lst))
#     pos_2 = t_2.position()
#     if pos_2[0] >= 300:
#         print("Blue wins!")
#         break
#     t_3.forward(random.choice(lst))
#     pos_3 = t_3.position()
#     if pos_3[0] >= 300:
#         print("Green wins!")
#         break
#     t_4.forward(random.choice(lst))
#     pos_4 = t_4.position()
#     if pos_4[0] >= 300:
#         print("Cyan wins!")
#         break
# ------------------------------
# create a game that has a rock in the (ranom position) and if one of the turtles hits the rock, it will be redirect to and hit out of the track
# ------------------------------
# create an analog clock with turtle
# ------------------------------



turtle.mainloop()