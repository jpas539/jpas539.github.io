'''
Name: Julian Pas
Description: A nice sandy beach with birds and the sun about to set. There are two umbrellas ready for people to enjoy the sounds of the waves.
'''

import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Project2")
    return t, screen

#helper functions
def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with fill"""
    draw_rectangle(t, size, size, fill_color)

def draw_triangle(t, size, fill_color=None):
    """Draw an  triangle with fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

def draw_circle(t, radius, fill_color=None):
    """Draw a circle with fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

def draw_polygon(t, sides, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """Drawed a curved line using small lines"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    segment_length = length / segments
    original_heading = t.heading()
    for i in range(segments):
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)
    t.setheading(original_heading)
    if fill_color:
        t.end_fill()

def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_scene(t):
    """Draw a colorful beach scene with various shapes"""

    # Set background color
    screen = t.getscreen()
    screen.bgcolor("skyblue")

    # Ocean 
    jump_to(t, -400, -100)
    draw_rectangle(t, 800, 100, "navy")

    # Sand 
    jump_to(t, -400, -200)
    draw_rectangle(t, 800, 100, "khaki")

    # Sun 
    jump_to(t, 320, 250)
    draw_circle(t, 50, "orange")

    # Umbrella pole 
    jump_to(t, 230, -40)
    draw_rectangle(t, 5, 60, "brown")

    # Umbrella top 
    jump_to(t, 200, -40)
    draw_triangle(t, 70, "red")


 # Multiple Umbrellas just copied the code to make umbrella and just moved the positions
    jump_to(t, 130, -40)
    draw_rectangle(t, 5, 60, "brown")
    jump_to(t, 100, -40)
    draw_triangle(t, 70, "red")

    
   # Drawing Birds, code pasted from project one 
    def draw_bird(x, y, size=30):
        t.color("white")
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(0)  
        t.forward(size)
        t.right(120)
        t.forward(size)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.setheading(0)
        t.forward(size)
        t.left(120)
        t.forward(size)

#multiple birds!! Copied code from project one 
    draw_bird(-200, 150, 20)
    draw_bird(-100, 180, 15)
    draw_bird(50, 160, 25)
    draw_bird(200, 140, 20) 




def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()
