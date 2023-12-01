import sys
from structures.character import *
from data.characters import characters

# Basic Setup
TITLE = 'Battle!'
WIDTH = 480
HEIGHT = 320

#Graphics Locations
enemy_hp_bar_loc = 104, 66
player_hp_bar_loc = 348, 182
run = False
party = False
bag = False
fight = False
run_x_loc = 366, 270
party_x_loc = 266, 273
bag_x_loc = 366, 239
mov_one_loc = 20, 240
mov_two_loc = 160, 240
mov_three_loc = 20, 274
e_name_loc = 42, 42
p_name_loc = 284, 158

gamestate = 0

# Testing Variables to be replaced with actual numbers
e_hp = 100
e_hp_max = 100
e_name = "Dog.jpg"

p_hp = 100
p_hp_max = 100
p_name = "Man"


class Game(object):
    def __init__(self):
        self.gamestate = 0
        self.characters = {}

        self.player = Player(self.characters["Man"])
        self.bot = Player(self.characters["Dog"], True)

    def load_characters(self):
        for character in characters:
            character["moves"] = self.load_moves(character["moves"])
            self.characters[character["name"]] = (Character(**character))

    def load_moves(self, moves):
        _moves = []
        for move in moves:
            if move.get("status"):
                status = Status(**move["status"])
                move["status"] = status
            _moves.append(Move(**move))
        return _moves


def on_key_down(key):
    global gamestate, fight
    # Exit Game
    if key == keys.ESCAPE:
        sys.exit()
    # Enter Game
    if gamestate == 0:
        if key == keys.SPACE:
            gamestate = 1
    # Choose Fight
    if gamestate == 1:
        if key == keys.RETURN:
            fight = True
            
    
        

def draw():
    # Clear Screen
    screen.fill((0, 0, 50))
    # Draw Main Menu for Gamestate = 0
    if gamestate == 0:
        screen.blit('title', (20, 20))
        screen.draw.text("Welcome to:", (20, 10))
        screen.draw.text("Space = Start", (60, 200))
        screen.draw.text("Esc = Exit", (60, 250))
        screen.blit('man_front', (10, 300))
        screen.blit('dog', (300, 300))
    # Draw Battle for Gamestate = 1
    elif gamestate == 1:
        screen.blit('battle_background', (0, 0))
        screen.blit('battle_text', (0,224))
        screen.blit('battle_choice', (240,224))
        # Draw Player HP
        if p_hp > p_hp_max/50:
            screen.blit('health', (player_hp_bar_loc))
        elif p_hp >= p_hp_max/25:
            screen.blit('health_some_dmg', (player_hp_bar_loc))
        elif p_hp > 0:
            screen.blit('health_dmg', (player_hp_bar_loc))
        # Draw Enemy HP    
        if e_hp > e_hp_max/2:
            screen.blit('health', (enemy_hp_bar_loc))
        elif e_hp >= e_hp_max/4:
            screen.blit('health_some_dmg', (enemy_hp_bar_loc))
        elif e_hp > 0:
            screen.blit('health_dmg', (enemy_hp_bar_loc))
        # Draw Character Names
        screen.draw.text(e_name, (e_name_loc), color='black')
        screen.draw.text(p_name, (p_name_loc), color='black')    
        # Draw Red Xs
        if run:
            screen.blit('denied', (run_x_loc))
        if bag:
            screen.blit('denied', (bag_x_loc))
        if party:
            screen.blit('denied', (party_x_loc))
        # Draw moves list if Fight is selected
        if fight:
            screen.blit('battle_moves', (0,224))
            screen.draw.text("Move One", (mov_one_loc), color='black')
            screen.draw.text("Move Two", (mov_two_loc), color='black')
            screen.draw.text("Move Three", (mov_three_loc), color='black')
            
            
        
    

def update():
    
    # Run Draw Function
    draw()

pgzrun.go()

