import random
import pgzrun


class Status:
    def __init__(self, dmg_boost: int, def_boost: int, duration: int = 1, carry_over: bool = False):
        self.dmg_boost = dmg_boost
        self.def_boost = def_boost
        self.duration = duration
        self.carry_over = carry_over


class Move:
    def __init__(self, name: str, dmg: int, speed: int, percent: bool = False, status: Status = None):
        self.name = name
        self.speed = speed
        self.dmg = dmg
        self.percent = percent
        self.status = status
        self.actor = Actor("moves/" + self.name)


class Character:
    def __init__(self, name: str, hp: int, moves: list[Move]):
        self.name = name
        self.hp_max = hp
        self.hp = self.hp_max
        self._moves = moves
        self.status: list[Status] = []
        self.actor = Actor("characters/" + self.name)

    @property
    def moves(self):
        random.shuffle(self._moves)
        return self._moves[0:3]

    def do_move(self, move: Move):
        if move.status:
            self.status.append(move.status)

    def take_dmg(self, move: Move, boost):
        dmg = self.hp_max * move.dmg/100 if move.percent else move.dmg
        final_dmg = dmg * boost * self.defense_boost
        self.hp -= final_dmg

        self.update_status()
        return self.alive

    def update_status(self):
        _status = []
        for status in self.status:
            status.duration -= 1
            if status.duration > 0:
                _status.append(status)
        self.status = _status

    @property
    def carry_status(self):
        _status = []
        for status in self.status:
            if status.carry_over:
                _status.append(status)
        return _status

    @property
    def damage_boost(self):
        boost = 100
        for status in self.status:
            boost += status.dmg_boost
        return boost/100

    @property
    def defense_boost(self):
        boost = 0
        for status in self.status:
            boost += status.def_boost
        return 1 - boost/100

    @property
    def alive(self):
        return self.hp > 0


class Deck:
    def __init__(self, characters: list[Character]):
        random.shuffle(characters)
        self.characters = characters
        self.pos = 0
        self.current_character = self.characters[0]

    def character_death(self):
        self.pos += 1
        carry = self.current_character.carry_status
        self.current_character = self.characters[self.pos]
        self.current_character.status = carry

    def attack(self, prompt_move, opponent: Character):
        moves = self.current_character.moves
        selected_move = prompt_move(moves)
        self.current_character.do_move(selected_move)
        opponent.take_dmg(selected_move, self.current_character.damage_boost)


class Player:
    def __init__(self, base_character: Character, bot=False):
        self.characters = [base_character]
        self.current_deck = Deck(self.characters)
        self.bot = bot

    def new_deck(self):
        random.shuffle(self.characters)
        self.current_deck = Deck(self.characters[:4])

    @property
    def current_action(self):
        return ""

