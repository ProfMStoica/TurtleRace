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
    #calculate the coordinate of the finish line
    finishLineCoordinate = RaceTrack.raceTrack.window_height()/2

    #repeat advancing turtles until they reach the finish line (DO NOT use "until")
    #repeat advancing turtles for as long as (while) they did NOT reach the finish line
    finishLineReached = False
    while not finishLineReached:
        #have the turtle racers hop once
        dist = random.randint(10, 100)
        leo.forward(dist)

        dist = random.randint(10, 100)
        mikey.forward((dist))

        dist = random.randint(10, 100)
        don.forward(dist)

        #determine if any of the turtles have crossed the finish line
        if leo.ycor() >= finishLineCoordinate or mikey.ycor() >= finishLineCoordinate or \
            don.ycor() >= finishLineCoordinate:
            #one or more turtles have crossed the finish line
            finishLineReached = True

        

#Determine the winner
def determineWinner():
    winner = None
    raceResult = None

    #determine the winner by comparing how far they reached in the race
    if leo.ycor() > mikey.ycor() and leo.ycor() > don.ycor():
        #leo won
        winner = leo
        raceResult = "Leo won!"
    elif mikey.ycor() > leo.ycor() and mikey.ycor() > don.ycor():
        #mikey won
        winner =  mikey
        raceResult = "Mikey won!"
    elif don.ycor() > leo.ycor() and don.ycor() > mikey.ycor():
        #don won
        winner = don
        raceResult = "Don won!"
    else:
        #At least two turtles are tied
        winner = None
        raceResult = "Race is tied! Try again."
    
    #(return the information to the caller)
    return winner, raceResult
    
