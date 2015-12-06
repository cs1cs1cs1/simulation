import runWorld as rw
import drawWorld as dw
import pygame as pg
import math
from random import randint

# Initialize world
name = "Scaredy Cat!"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")

class State:
    endState = False
    def setState(self, x, xv, r, g, b):
        self.x = x
        self.xv = xv
        self.r = r
        self.g = g
        self.b = b
    def __init__(self, x, xv, r, g, b):
        self.setState(x, xv, r, g, b)

ooInitState = State(0, 1, 125, 125, 125)

def updateDisplay(state):
    mycolor = (state.r, state.g, state.b);
    dw.fill(mycolor)
    dw.draw(myimage, (state.x, math.sin(math.radians(state.x))*100 + height/3))

def updateState(state):
    return State(state.x + state.xv, state.xv, state.r, state.g, state.b)

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state.x > width or state.x < 0):
        return True
    else:
        return False

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state.xv) == 1:
            newState = -1
            newR = randint(0,255);
            newG = randint(0,255);
            newB = randint(0,255);
            return State(state.x, newState, newR, newG, newB);
        else:
            newR = randint(0,255);
            newG = randint(0,255);
            newB = randint(0,255);
            newState = 1
            return State(state.x, newState, newR, newG, newB);
   
    else:
        return(state)

# World state will be single x coordinate at left edge of world

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(ooInitState, updateDisplay, updateState, handleEvent, endState, frameRate)
