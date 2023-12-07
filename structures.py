import random


class Status:
    def __init__(self, dmg_boost: int, def_boost: int, duration: int = 1, carry_over: bool = False):
        self.dmg_boost = dmg_boost
        self.def_boost = def_boost
        self.duration = duration
        self.carry_over = carry_over


class BaseMove:
    def __init__(self, name: str, dmg: int, camp, desc, percent: bool = False, status: Status = None):
        self.name = name
        self.dmg = dmg
        self.percent = percent
        self.status = status
        self.camp = camp
        self._desc = desc
        self.curr_desc = {
            "enemy": "",
            "damage": 0,
            "player": ""
        }

    @property
    def desc(self):
        return self._desc.format(**self.curr_desc)


class BaseCharacter:
    def __init__(self, name: str, hp: int, moves: list[BaseMove], camp: int):
        self.name = name
        self.hp_max = hp
        self.hp = self.hp_max
        self._moves = moves
        self.status: list[Status] = []
        self.camp = camp

    @property
    def moves(self):
        random.shuffle(self._moves)
        return self._moves[0:3]

    def do_move(self, move: BaseMove):
        if move.status:
            self.status.append(move.status)

    def take_dmg(self, move: BaseMove, boost):
        dmg = self.hp_max * move.dmg/100 if move.percent else move.dmg
        final_dmg = dmg * boost * self.defense_boost
        self.hp -= final_dmg

        self.update_status()
        move.curr_desc["damage"] = final_dmg
        move.curr_desc["enemy"] = self.name
        return self.alive

    def update_status(self):
        _status = []
        for status in self.status:
            status.duration -= 1
            if status.duration > 0:
                _status.append(status)
        self.status = _status

    @property
    def hp_bar(self):
        if self.hp > self.hp_max*2/3:
            return "health"
        elif self.hp > self.hp_max/3:
            return "health_some_dmg"
        else:
            return "health_dmg"

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
        return 1 - boost/100 if boost < 90 else 0.1

    @property
    def alive(self):
        return self.hp > 0


class Deck:
    def __init__(self, characters: list[BaseCharacter]):
        random.shuffle(characters)
        self.characters = characters
        self.pos = 0
        self.current_character = self.characters[0]

    def character_death(self):
        if self.pos == len(self.characters)-1:
            return True
        self.pos += 1
        carry = self.current_character.carry_status
        self.current_character = self.characters[self.pos]
        self.current_character.status = carry

    def attack(self, move: BaseMove, opponent: BaseCharacter):
        self.current_character.do_move(move)
        move.curr_desc["player"] = self.current_character.name
        alive = opponent.take_dmg(move, self.current_character.damage_boost)
        return [f"{self.current_character.name} used {move.name}!", move, (alive, opponent)]

    def bot_attack(self, opponent: BaseCharacter):
        return self.attack(random.choice(self.current_character.moves),opponent)


class Player:
    def __init__(self, base_character: BaseCharacter, bot=False):
        self.characters = [base_character]
        self.deck = Deck(self.characters)
        self.bot = bot

    def new_deck(self):
        random.shuffle(self.characters)
        self.deck = Deck(self.characters[:3])

    def restore_stats(self):
        for character in self.characters:
            character.hp = character.hp_max
            character.status = []

    @property
    def current_character(self):
        return self.deck.current_character

    @property
    def attack(self):
        return self.deck.bot_attack if self.bot else self.deck.attack


class ChoiceMenu:
    def __init__(self, choices: list[BaseMove], menu_type=1):
        self.choices = choices
        self.pos = 0
        self.type = menu_type
        self.denied = [False, False, False]

    def handle_input(self, key, keys):
        if key == keys.RIGHT:
            if self.type == 0:
                if self.pos < 3:
                    self.pos += 1
                else:
                    self.pos = 0
            else:
                if self.pos < len(self.choices)-1:
                    self.pos += 1
                else:
                    self.pos = 0
        elif key == keys.LEFT:
            if self.type == 0:
                if self.pos > 0:
                    self.pos -= 1
                else:
                    self.pos = 3
            else:
                if self.pos > 0:
                    self.pos -= 1
                else:
                    self.pos = len(self.choices)-1
        elif key == keys.SPACE:
            if self.type == 0:
                if self.pos > 0:
                    self.denied[self.pos-1] = True
                else:
                    return True
            else:
                return True

    @property
    def choice(self):
        if self.type == 0:
            return self.pos
        else:
            return self.choices[self.pos]
