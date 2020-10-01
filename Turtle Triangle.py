# Author: Christine Okubo
# A	program that reads 2 triangle lengths and 1 angle input from a user 
# and draws the triangle using Turtle Graphics.
# Sample lengths: 150, 200; Sample angle: 120
# 09/27/2019

import math
import turtle

a = float(input('Enter length of side 1: '))
b = float(input('Enter length of side 2: '))
theta = float(input('Enter angle between these two edges: '))
theta_deg = math.degrees(theta)

c = math.sqrt((a**2) + (b**2) - (2*a*b*math.cos(theta_deg)))

turtle.forward(a)
turtle.right(180+theta)
turtle.forward(b)
turtle.goto(0,0)