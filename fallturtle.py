
import turtle

screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightgreen")

anna = turtle.Turtle()

anna.shape("turtle")
anna.color("darkorchid")

def drawClock():
    anna.stamp()
    for i in range(11):
        anna.penup()
        anna.forward(150)
        anna.pendown()
        anna.stamp()
        anna.penup()
        anna.forward(-150)
        anna.left(30)
        anna.forward(150)
        anna.pendown()
        anna.stamp()
        anna.penup()
        anna.forward(-150)
    
    
    
#drawClock()

def spiral():
    for i in range(100):
        anna.pensize(1.5)
        anna.speed(80)
        anna.pendown()
        anna.forward(i)
        anna.left(90)
        anna.forward(i)

#spiral()


def spiralTwist():
    for i in range(100):
        anna.pensize(1.5)
        anna.speed(80)
        anna.pendown()
        anna.forward(i)
        anna.left(86)
        anna.forward(i)

spiralTwist()


screen.listen()
screen.mainloop()

