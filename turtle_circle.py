import colorsys
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.speed(0)
n=70
h=0
turtlesize=6  #adjust turtul size
circle_radius=100
t.turtlesize(turtlesize)  #adjust turtul size
for i in range(350):
    c = colorsys.hsv_to_rgb(h, 1, 0.5)
    h+=2/n
    t.color(c)
    t.left(1)
    for j in range(2):
        t.left(2)
        #t.circle(10)
        t.circle(circle_radius)  #adjust the circle size       
turtle.done()