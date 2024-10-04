"""Creates the race track and the racers, configures them and prepares them for the race"""
import turtle

#define the module variables
raceTrack = None


#Create the race track window and configure it.
def createRaceTrack():
    global raceTrack
    raceTrack = turtle.Screen()
    raceTrack.bgcolor('lightgreen')
    return raceTrack


def closeRaceTrack():
    #Wait for user confirmation to close the program
    raceTrack.exitonclick()