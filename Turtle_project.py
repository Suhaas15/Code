from turtle import Turtle,Screen
import turtle as t
import random

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkSeaGreen")

side=3
t.colormode(255)
# for i in range(8):
#     angle = 360 / side
#     r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#     for j in range(side):
#         timmy.right(angle)
#         timmy.pencolor((r,g,b))
#         timmy.forward(100)
#     side+=1


# for i in range(100):
#     r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#     timmy.pencolor(r,g,b)
#     timmy.pensize(10)
#     timmy.speed("fastest")
#     steps = int(random.randint(0,100))
#     angle = int(random.randint(0,360))
#     timmy.right(angle)
#     timmy.fd(steps)

for i in range(int(360/5)):
    timmy.speed("fastest")
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    timmy.pencolor(r,g,b)
    timmy.circle(100)
    timmy.setheading(timmy.heading() + 5)


import heroes
print(heroes.gen())

my_screen = Screen()
my_screen.exitonclick()

