"""Creates the race track and the racers, configures them and prepares them for the race"""
import turtle

#define the module variables
raceTrack = None
leo = None
mickey = None
don = None

#Create the race track window and configure it.
def createRaceTrack():
    global raceTrack
    raceTrack = turtle.Screen()
    raceTrack.bgcolor('lightgreen')
    return raceTrack

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

def closeRaceTrack():
    #Wait for user confirmation to close the program
    raceTrack.exitonclick()