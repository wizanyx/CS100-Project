import sys
import pgzrun
from structures import *
from data import characters

# Basic Setup
TITLE = 'Battle!'
WIDTH = 480
HEIGHT = 320

# Graphics Locations

PLAYER_HP_BAR_LOC = 348, 182
PLAYER_NAME_LOC = 284, 158

BOT_HP_BAR_LOC = 104, 66
BOT_NAME_LOC = 42, 42


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


gamestate = 0

# Testing Variables to be replaced with actual numbers
e_hp = 100
e_hp_max = 100
e_name = "Dog.jpg"

p_hp = 100
p_hp_max = 100
p_name = "Man"


class Move(BaseMove):
    def __init__(self, name: str, dmg: int, speed: int, percent: bool = False, status: Status = None):
        BaseMove.__init__(self, name, dmg, speed, percent, status)
        self.actor = Actor("moves/" + self.name.lower())


class Character(BaseCharacter):
    def __init__(self, name: str, hp: int, moves: list[Move]):
        BaseCharacter.__init__(self, name, hp, moves)
        self.actor = Actor("characters/" + self.name.lower())


class Game(object):
    def __init__(self):
        self.game_state = 0
        self.characters = {}

        self.load_characters()

        self.player = Player(self.characters["Man"])
        self.bot = Player(self.characters["Dog"], True)

    def load_characters(self):
        for character in characters:
            character["moves"] = self.load_moves(character["moves"])
            self.characters[character["name"]] = (Character(**character))

    def draw_screen(self):
        screen.fill((0, 0, 50))

        if self.game_state == 0:
            print(self.game_state)
            self.display_main_screen()
        elif self.game_state == 1:
            self.display_battle_screen()

    def display_main_screen(self):
        global screen

        screen.blit('title', (20, 20))
        screen.draw.text("Welcome to:", (20, 10))
        screen.draw.text("Space = Start", (60, 200))
        screen.draw.text("Esc = Exit", (60, 250))
        screen.blit('man_front', (10, 300))
        screen.blit('dog', (300, 300))

    def display_battle_screen(self):
        global screen

        # Battle Screen Background
        screen.blit('battle_background', (0, 0))
        screen.blit('battle_text', (0, 224))
        screen.blit('battle_choice', (240, 224))

        # Draw Player
        #   HP Bar
        screen.blit(self.player.current_character.hp_bar, PLAYER_HP_BAR_LOC)
        #   Character Name
        screen.draw.text(self.player.current_character.name, PLAYER_NAME_LOC, color='black')

        # Draw Bot
        #   HP Bar
        screen.blit(self.bot.current_character.hp_bar, BOT_HP_BAR_LOC)
        #   Character Name
        screen.draw.text(self.bot.current_character.name, BOT_NAME_LOC, color='black')

    def handle_inputs(self, key):
        print(self.game_state)
        if key == keys.ESCAPE:
            sys.exit()

        if self.game_state == 0:
            if key == keys.SPACE:
                self.game_state = 1

    @staticmethod
    def load_moves(moves):
        _moves = []
        for move in moves:
            if move.get("status"):
                status = Status(**move["status"])
                move["status"] = status
            _moves.append(Move(**move))
        return _moves


game = Game()


def on_key_down(key):
    game.handle_inputs(key)


def draw():
    # Clear Screen
    screen.fill((0, 0, 50))
    # Draw Main Menu for Gamestate = 0
    if game.game_state == 0:
        game.display_main_screen()
    # Draw Battle for Gamestate = 1
    elif game.game_state == 1:
        game.display_battle_screen()
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
    #game.draw_screen()

pgzrun.go()

