"""
Version 1
In this version the turtle race has a flat single-file structure
"""
import turtle
import random

#Create the race track window and configure it.
raceTrack = turtle.Screen()
raceTrack.bgcolor('lightgreen')

#Create the racers
larry = turtle.Turtle()
larry.shape("turtle")
larry.color("darkgreen")
larry.turtlesize(3, 3, 1)
larry.penup()

curly = turtle.Turtle()
curly.shape("turtle")
curly.color("darkred")
curly.turtlesize(3, 3, 1)
curly.penup()

moe = turtle.Turtle()
moe.shape("turtle")
moe.color("blue")
moe.turtlesize(3, 3, 1)
moe.penup()

#Position the racers on the starting line
larry.left(180)
larry.forward(200)
larry.right(90)
curly.left(90)
moe.forward(200)
moe.left(90)

#get them ready to race
larry.pendown()
curly.pendown()
moe.pendown()

#Run the race
dist = random.randint(10, 100)
larry.forward(dist)

dist = random.randint(10, 100)
curly.forward((dist))

dist = random.randint(10, 100)
moe.forward(dist)

#Determine the winner

#Let the user know who the winner is

#Wait for user confirmation to close the program
raceTrack.exitonclick()