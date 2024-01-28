"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
from random import *


t = turtle.Turtle()
t.goto(0,0)
t.speed(100)

answers = ['It is certain',
'Without a doubt',
'Yes definitely',
'As I see it, yes',
'Most likely',
'Yes',
'Signs point to yes',
'Reply hazy try again',
'Ask again later',
'Better not tell you now',
'Cannot predict now',
'No', 'Of course not', 'It looks like no', 'How would i know, im just a program', 'heck no']



def thing ():
  t.goto(0,-200)
  t.color('black')
  t.begin_fill()
  t.circle(200)
  t.end_fill()
  t.penup()
  t.color('white')
  t.goto(0, -50)
  t.pendown()
  t.write('8', align = 'center', font = ('Arial', 130, 'bold'))
  t.penup()
  t.goto(0,-100)
  t.pendown()



thing()
num = 0
while(num == 0):
   turtle.Screen().textinput('Ask A Question', 'specifically, a yes or no question')
   thing()
   t.write(answers[randint(0,13)], align = 'center', font=('Arial', 10, 'bold'))