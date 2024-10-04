"""
Version 3
In this version the turtle race program is organized using multiple modules
Main module coordinates the entire program and interacts with the user
"""
from tkinter import messagebox
import RaceTrack
import Race

#run the main program using the functions we have defined
RaceTrack.createRaceTrack()

Race.registerRacers()

Race.positionRacers()

Race.runRace()

Race.determineWinner()

#Let the user know who the winner is
messagebox.showinfo("Turtle Race", "Mikey")

#wait for the user to confirm closing the race track
RaceTrack.closeRaceTrack()