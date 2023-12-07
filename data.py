characters = [
    { # Player Characters
        "name": "Man",
        "hp": 100,
        "moves": [
            {
                "name": "Punch",
                "dmg": 10,
                "desc": "You punch {enemy} and do {damage} damage.",
            }, {
                "name": "Boink",
                "dmg": 30,
                "desc": "You hit {enemy} with a club and do {damage} damage.",
                "percent": True
            }
        ],
        "camp": 0
    }, {
        "name": "Dario",
        "hp": 120,
        "moves": [
            {
                "name": "Jump",
                "dmg": 30,
                "desc": "Dario jumps on {enemy} and does {damage} damage.",
            }, {
                "name": "Super Mushroom",
                "dmg": 0,
                "desc": "Dario eats a Super Mushroom and is powered up!",
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 30,
                    "duration": 3
                }
            }, {
                "name": "Clump",
                "dmg": 0,
                "desc": "Dario makes a... clump?",
                "percent": False
            }
        ],
        "camp": 0
    }, {
        "name": "Fesus",
        "hp": 150,
        "moves": [
            {
                "name": "Jesus Kick",
                "dmg": 15,
                "desc": "Fesus uses his ancient judo training to deliver a devestating kick that does {damage} damage."
            }, {
                "name": "Jesus Lightning",
                "dmg": 20,
                "desc": "Holy crap! That awesome lightning just did {damage} damage.",
                "percent": True,
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 15,
                    "duration": 4
                }
            }, {
                "name": "Jesus Beam",
                "dmg": 30,
                "desc": "Jesus uses all of his chi to create a powerful blast of energy that does {damage} damage.",
                "percent": False
            }
        ],
        "camp": 0
    }, {
        "name": "Wojak",
        "hp": 100,
        "moves": [
            {
                "name": "Mald",
                "dmg": 25,
                "desc": "Wojak malds harder than he has ever malded before. {enemy} is worried and takes {damage} damage."
            }, {
                "name": "Cope",
                "dmg": 0,
                "desc": "Wojak takes a swig of copium, and feels a little stronger.",
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 30,
                    "duration": 2
                }
            }
        ],
        "camp": 0
    }, {
        "name": "Saitama",
        "hp": 250,
        "moves": [
            {
                "name": "Normal Punch",
                "dmg": 2000,
                "desc": "Saitama does a normal punch, doing {damage} damage."
            }
        ],
        "camp": 0
    }, { # Bot Characters
        "name": "Dog",
        "hp": 80,
        "moves": [
            {
                "name": "Bite",
                "dmg": 30,
                "desc": "The dog bites you and you take {damage} damage."
            }, {
                "name": "Bark",
                "dmg": 1,
                "desc": "What an annoying dog.",
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 2
                }
            }
        ],
        "camp": 1
    }, {
        "name": "Angel Dog",
        "hp": 100,
        "moves": [
            {
                "name": "Bite",
                "dmg": 30,
                "desc": "The dog bites you and you take {damage} damage."
            }, {
                "name": "Bark",
                "dmg": 1,
                "desc": "What an annoying dog.",
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Holy Crap",
                "dmg": 10,
                "desc": "The dog takes a crap, but it looks somehow... glorius!",
                "percent": True,
                "status": {
                    "dmg_boost": 10,
                    "def_boost": 40,
                    "duration": 2
                }
            }
        ],
        "camp": 1
    }, {
        "name": "Devil Dog",
        "hp": 120,
        "moves": [
            {
                "name": "Bite",
                "dmg": 30,
                "desc": "The dog bites you and you take {damage} damage."
            }, {
                "name": "Bark",
                "dmg": 1,
                "desc": "What an annoying dog.",
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Unholy Crap",
                "dmg": 10,
                "desc": "Call an exorcist, this crap is gross!",
                "percent": True,
                "status": {
                    "dmg_boost": 40,
                    "def_boost": 10,
                    "duration": 2
                }
            }
        ],
        "camp": 1
    }, {
        "name": "Eldritch Dog",
        "hp": 140,
        "moves": [
            {
                "name": "Bite",
                "dmg": 30,
                "desc": "The dog bites you and you take {damage} damage."
            }, {
                "name": "Bark",
                "dmg": 1,
                "desc": "What an annoying dog.",
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Unknowable Crap",
                "dmg": 10,
                "desc": "This crap is beyond your comprehension.",
                "percent": True,
                "status": {
                    "dmg_boost": 40,
                    "def_boost": 40,
                    "duration": 2
                }
            }
        ],
        "camp": 1
    }, {
        "name": "Monal Muck",
        "hp": 130,
        "moves": [
            {
                "name": "Shlong Swipe",
                "dmg": 35,
                "desc": "Uhh, you take {damage} damage, I guess..."
            }, {
                "name": "Quack",
                "dmg": 1,
                "desc": "What an annoying duck.",
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 3
                }
            }, {
                "name": "Bread Throw",
                "dmg": 20,
                "desc": "He just threw bread at you... how rude...",
                "percent": True,
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Where is Mom",
                "dmg": 0,
                "desc": "Where did that cooked duck come from...",
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 40,
                    "duration": 2
                }
            }
        ],
        "camp": 1
    }, {
        "name": "Jreddy Jazzbear",
        "hp": 150,
        "moves": [
            {
                "name": "Bite of 87",
                "dmg": 40,
                "desc": "WAS THAT THE BITE OF 87? Take {damage} damage."
            }, {
                "name": "Kill Children",
                "dmg": 10,
                "desc": "Jreddy kills children in front of {enemy}. {enemy} takes {damage} damage from sadness.",
                "percent": True,
                "status": {
                    "def_boost": 0,
                    "dmg_boost": 40,
                    "duration": 1
                }
            }, {
                "name": "Ghostly Jazz",
                "dmg": 0,
                "desc": "Jreddy's soulful tunes will haunt you forever.",
                "percent": True,
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 50,
                    "duration": 2
                }
            }
        ],
        "camp": 1
    }, {
        "name": "Garfield",
        "hp": 180,
        "moves": [
            {
                "name": "Cat Attack",
                "dmg": 35,
                "desc": "Garfield uses his underground cat empire to deal {damage} damage."
            }, {
                "name": "Monday Power",
                "dmg": 15,
                "desc": "Garfield channels his rage for the day monday to deal {damage} damage.",
                "percent": True,
                "status": {
                    "dmg_boost": 50,
                    "def_boost": 0,
                    "duration": 2
                }
            }, {
                "name": "Good Meal",
                "dmg": 0,
                "desc": "He's gotta have a good meal",
                "percent": True,
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 50,
                    "duration": 2
                }
            }
        ],
        "camp": 1
    }, {
        "name": "Professor Guarnera",
        "hp": 1000,
        "moves": [
            {
                "name": "Fail",
                "dmg": 2000,
                "desc": "Professor Guarnera gives {enemy} a failing grade in cs102."
            }
        ],
        "camp": 1
    }
]
