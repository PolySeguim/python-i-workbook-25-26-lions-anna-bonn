import turtle

# Create a turtle object
#turtle is a complex data type
#screen is a complex data type - has attributes and behaviors
screen = turtle.Screen()
screen.title("Turtle Example in Python") 
anna = turtle.Turtle()
"""
# Move the turtle forward by 100 units
def forward100():
    anna.forward(100)

# Turn the turtle to the right by 90 degrees
def right90():
    anna.right(90)


# Repeat the above steps to complete the square
screen.onkey(forward100, "Up")
screen.onkey(right90, "Right")

screen.listen()
screen.mainloop()

# Keep the window open until clicked



def iterationTest():
    
    subjects= ["english", "math", "science"]
    for subject in subjects:
        print("my favorite subject is", subject)
       
"""

 
def rainbow():
    colors = ["red", "orange", "yellow","green", "blue", "indigo", "violet"]

    for color in colors:
        anna.speed(10)
        anna.shape("turtle")
        anna.color(color)
        anna.forward(10)
        anna.circle(50)
        anna.forward(10)
        
rainbow()


def activity():
    size = 20
    
    for i in range(30):
        anna.stamp()
        size = size + 3
        anna.forward(size)
        anna.right(24)
        
activity()


turtle.done()