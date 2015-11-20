import runWorld as rw
import drawWorld as dw
import pygame as pg
import math

# Initialize world
name = "Scaredy Cat!"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")

def updateDisplay(state):
    dw.fill(dw.red)
    dw.draw(myimage, (state[0], math.sin(math.radians(state[0]))*100 + height/3))

def updateState(state):
     return((state[0] + state[2],state[1], state[2], state[3]))

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state[0] > width or state[0] < 0):
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
        if (state[2]) == 1:
            newState = -1
        else:
            newState = 1   
        return(state[0], state[1], newState, state[3])
    else:
        return(state)

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right 
initState = (0,100,1,1)

# Run the simulation no faster than 60 frames per second
frameRate = 60

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
