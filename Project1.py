import turtle
#making background blue 
screen = turtle.Screen()
screen.bgcolor("skyblue")
import turtle
import pydoc
t=turtle.Turtle()
def draw_rectangle(x, y, width, height, color): #definiton or formula to draw rectangle for my road 
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("black")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.color("white")

#making the dashed lines, Used Chat GPT to learn how to do it with the promt how to i creat dashed lines for a road.
draw_rectangle(-300, -150, 600, 100, "gray")
t.penup()
t.goto(-300, -100)  # middle of the road
t.pendown()

for _ in range(36):
    t.forward(10)  # dash length
    t.penup()
    t.forward(10)  # gap
    t.pendown()
# now im making the sun
t.penup()
t.goto(300, 250)  # position the sun
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)  # radius of the sun
t.end_fill()
#I used chat gpt to help me learn to make little birds 
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

#multiple birds!!!!
draw_bird(-200, 150, 20)
draw_bird(-100, 180, 15)
draw_bird(50, 160, 25)
draw_bird(200, 140, 20)

#using a conditional to make the side of the drawing night and day 
t.shape("turtle")
t.penup()
t.goto(0, 0)

# Move the turtle to the right
t.goto(20, 0)  # x > 0 means turtle is on the right

# Conditional statement
if t.xcor() > 20:  # if x-coordinate is greater than 20
    screen.bgcolor("black")  # change background to black
else:
    screen.bgcolor("skyblue") #if not sky stays blue 


turtle.done()


