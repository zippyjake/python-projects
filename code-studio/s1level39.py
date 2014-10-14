import mymod
import turtle

bob = turtle.Turtle()
bob.pensize(7)
bob.speed(100)

for count2 in range(36):
    bob.pencolor(mymod.random_color())
    for count in range(3):
        bob.forward(100)
        bob.right(120)
    bob.right(10)
