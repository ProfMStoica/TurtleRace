"""Manage the race and determine the winner"""
import random
import RaceTrack

#Position the racers on the starting line
def positionRacers():
    RaceTrack.leo.left(180)
    RaceTrack.leo.forward(200)
    RaceTrack.leo.right(90)
    RaceTrack.mikey.left(90)
    RaceTrack.don.forward(200)
    RaceTrack.don.left(90)

    #get them ready to race
    RaceTrack.leo.pendown()
    RaceTrack.mikey.pendown()
    RaceTrack.don.pendown()

#Run the race
def runRace():
    dist = random.randint(10, 100)
    RaceTrack.leo.forward(dist)

    dist = random.randint(10, 100)
    RaceTrack.mikey.forward((dist))

    dist = random.randint(10, 100)
    RaceTrack.don.forward(dist)

#Determine the winner
def determineWinner():
    #TODO: use branching to determine which turtle advanced the most
    winner = RaceTrack.don
