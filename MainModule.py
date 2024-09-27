"""
Version 3
In this version the turtle race program is organized using multiple modules
Main module coordinates the entire program and interacts with the user
"""
import turtle
import random
from tkinter import messagebox

#Create the race track window and configure it.
def createRaceTrack():
    raceTrack = turtle.Screen()
    raceTrack.bgcolor('lightgreen')
    return raceTrack

#Create the racers
def registerRacers():
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
    return leo,mikey,don

#Position the racers on the starting line
def positionRacers(leo, mikey, don):
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
def runRace(leo, mikey, don):
    dist = random.randint(10, 100)
    leo.forward(dist)

    dist = random.randint(10, 100)
    mikey.forward((dist))

    dist = random.randint(10, 100)
    don.forward(dist)

#Determine the winner
def determineWinner(don):
    #TODO: use branching to determine which turtle advanced the most
    winner = don

#run the main program using the functions we have defined
raceTrack = createRaceTrack()

leo, mikey, don = registerRacers()

positionRacers(leo, mikey, don)

runRace(leo, mikey, don)

determineWinner(don)

#Let the user know who the winner is
messagebox.showinfo("Turtle Race", "Mikey")

#Wait for user confirmation to close the program
raceTrack.exitonclick()