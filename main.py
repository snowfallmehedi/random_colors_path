import random
import turtle as t

tim_the_turtle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0,255)
    r_color = (r, g, b)
    return r_color


directions = [0, 90, 180, 270]
tim_the_turtle.pensize(15)
tim_the_turtle.speed("fastest")

for i in range(200):
    tim_the_turtle.color(random_color())
    tim_the_turtle.forward(30)
    tim_the_turtle.setheading(random.choice(directions))
