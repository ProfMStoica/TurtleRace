"""Manage the race and determine the winner"""
import random
import turtle
import RaceTrack

#define global variables
leo = None
mickey = None
don = None

#Create the racers
def registerRacers():
    global leo,mikey,don

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
def positionRacers():
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
def runRace():
    dist = random.randint(10, 100)
    leo.forward(dist)

    dist = random.randint(10, 100)
    mikey.forward((dist))

    dist = random.randint(10, 100)
    don.forward(dist)

#Determine the winner
def determineWinner():
    #TODO: use branching to determine which turtle advanced the most
    winner = don
