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
PLAYER_SPITE_LOC = 51, 96

BOT_HP_BAR_LOC = 104, 66
BOT_NAME_LOC = 42, 42
BOT_SPRITE_LOC = 283, 13


run = False
party = False
bag = False
fight = False

DENIED_CHOICE_LOC = [(366, 239), (266, 273), (366, 270)]
MOVE_CHOICE_LOC = [(32, 245), (172, 245), (32, 274)]
CHOICE_ARROW_LOC = [(258, 248), (370, 248), (258, 280), (370, 280)]
MOVE_ARROW_LOC = [(20, 245), (160, 245), (20, 274)]



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
        self.actor = Actor("moves/" + self.name.lower().replace(" ", "_"))


class Character(BaseCharacter):
    def __init__(self, name: str, hp: int, moves: list[Move], camp: int):
        BaseCharacter.__init__(self, name, hp, moves, camp)
        self.actor = Actor("characters/" + self.name.lower().replace(" ", "_"))
        self.actor.topleft = PLAYER_SPITE_LOC if self.camp == 0 else BOT_SPRITE_LOC


class Game(object):
    def __init__(self):
        self.game_state = 0
        self.characters = {}
        self.choice_menu = ChoiceMenu([], 0)
        self.move_display = False
        self.display_log = []

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

    @staticmethod
    def display_main_screen():
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

        self.display_choice_menu()

        # Draw Player
        #   HP Bar
        screen.blit(self.player.current_character.hp_bar, PLAYER_HP_BAR_LOC)
        #   Character Name
        screen.draw.text(self.player.current_character.name, PLAYER_NAME_LOC, color='black')
        #   Character Sprite
        self.player.current_character.actor.draw()

        # Draw Bot
        #   HP Bar
        screen.blit(self.bot.current_character.hp_bar, BOT_HP_BAR_LOC)
        #   Character Name
        screen.draw.text(self.bot.current_character.name, BOT_NAME_LOC, color='black')
        #   Character Sprite
        self.bot.current_character.actor.draw()

    def display_choice_menu(self):
        if self.choice_menu.type == 0:
            screen.blit('battle_choice', (240, 224))
            # Draw Denied Boxes
            for denied_no in range(3):
                if self.choice_menu.denied[denied_no]:
                    screen.blit('denied', DENIED_CHOICE_LOC[denied_no])
            # Draw Arrow
            screen.blit('choice_arrow', CHOICE_ARROW_LOC[self.choice_menu.pos])
        else:
            screen.blit('battle_moves', (0, 224))
            move_no = 0
            # Draw Move Names
            for move in self.choice_menu.choices:
                screen.draw.text(move.name, MOVE_CHOICE_LOC[move_no], color='black')
                move_no += 1
            # Draw Move Arrow
            screen.blit('choice_arrow', MOVE_ARROW_LOC[self.choice_menu.pos])

    def handle_inputs(self, key):
        if key == keys.ESCAPE:
            sys.exit()

        if self.game_state == 0:
            if key == keys.SPACE:
                self.game_state = 1
        elif self.game_state == 1 and not self.move_display:
            if self.choice_menu.handle_input(key, keys):
                if self.choice_menu.choice == 0:
                    self.choice_menu = ChoiceMenu(self.player.current_character.moves)
                else:
                    print(self.display_log)
                    player_result = self.player.attack(self.choice_menu.choice, self.bot.current_character)
                    self.display_log.append(player_result)
                    if player_result[2][0]:
                        self.display_log.append(self.bot.attack(self.player.current_character))
                    self.move_display = True

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


pgzrun.go()

