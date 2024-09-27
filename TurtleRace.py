"""
Version 1
In this version the turtle race has a flat single-file structure
"""
import turtle
import random
from tkinter import messagebox

#Create the race track window and configure it.
raceTrack = turtle.Screen()
raceTrack.bgcolor('lightgreen')

#Create the racers
leo = turtle.Turtle()
leo.shape("turtle")
leo.color("darkgreen")
leo.turtlesize(3, 3, 1)
leo.penup()

mikey = turtle.Turtle()
mikey.shape("turtle")
mikey.color("darkred")
mikey.turtlesize(3, 3, 1)
mikey.penup()

don = turtle.Turtle()
don.shape("turtle")
don.color("blue")
don.turtlesize(3, 3, 1)
don.penup()

#Position the racers on the starting line
leo.left(180)
leo.forward(200)
leo.right(90)
mikey.left(90)
don.forward(200)
don.left(90)

#get them ready to race
leo.pendown()
mikey.pendown()
don.pendown()

#Run the race
dist = random.randint(10, 100)
leo.forward(dist)

dist = random.randint(10, 100)
mikey.forward((dist))

dist = random.randint(10, 100)
don.forward(dist)

#Determine the winner
#TODO: use branching to determine which turtle advanced the most
winner = don

#Let the user know who the winner is
messagebox.showinfo("Turtle Race", "Mikey")

#Wait for user confirmation to close the program
raceTrack.exitonclick()