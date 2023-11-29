import pgzrun
import random
import sys

TITLE = 'Battle!'
WIDTH = 500
HEIGHT = 500

gamestate = 0

def on_key_down(key):
    global gamestate
    # Exit Game
    if key == keys.ESCAPE:
        sys.exit()
    # Enter Game
    if gamestate == 0:
        if key == keys.SPACE:
            gamestate = 1
            
        

def draw():
    # Clear Screen
    screen.fill((0, 0, 50))
    # Draw Main Menu for Gamestate = 0
    if gamestate == 0:
        screen.blit('title', (20, 100))
        screen.draw.text("Welcome to:", (20, 90))
        screen.draw.text("Space = Start", (60, 200))
        screen.draw.text("Esc = Exit", (60, 250))
        screen.blit('man_front', (10, 300))
        screen.blit('dog', (300, 300))
    elif gamestate == 1:
        screen.draw.text("Woah! It's a game!!!!!!!", (60, 200))
    

def update():
    
    # Run Draw Function
    draw()

pgzrun.go()

