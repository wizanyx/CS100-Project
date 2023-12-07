characters = [
    { # Player Characters
        "name": "Man",
        "hp": 100,
        "moves": [
            {
                "name": "Punch",
                "dmg": 10,
                "speed": 2
            }, {
                "name": "Boink",
                "dmg": 30,
                "speed": 4,
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
                "speed": 2
            }, {
                "name": "Super Mushroom",
                "dmg": 0,
                "speed": 4,
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 30,
                    "duration": 1
                }
            }, {
                "name": "Clump",
                "dmg": 0,
                "speed": 3,
                "percent": False
            }
        ],
        "camp": 0
    }, {
        "name": "Jesus",
        "hp": 150,
        "moves": [
            {
                "name": "Jesus Kick",
                "dmg": 15,
                "speed": 2
            }, {
                "name": "Jesus Lightning",
                "dmg": 20,
                "speed": 4,
                "percent": True,
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 15,
                    "duration": 4
                }
            }, {
                "name": "Jesus Beam",
                "dmg": 30,
                "speed": 3,
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
                "speed": 2
            }, {
                "name": "Cope",
                "dmg": 0,
                "speed": 4,
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
                "speed": 2
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
                "speed": 3
            }, {
                "name": "Bark",
                "dmg": 1,
                "speed": 5,
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
                "speed": 3
            }, {
                "name": "Bark",
                "dmg": 1,
                "speed": 5,
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Holy Crap",
                "dmg": 10,
                "speed": 3,
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
                "speed": 3
            }, {
                "name": "Bark",
                "dmg": 1,
                "speed": 5,
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Unholy Crap",
                "dmg": 10,
                "speed": 3,
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
        "name": "Elder Dog",
        "hp": 140,
        "moves": [
            {
                "name": "Bite",
                "dmg": 30,
                "speed": 3
            }, {
                "name": "Bark",
                "dmg": 1,
                "speed": 5,
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Unknowable Crap",
                "dmg": 10,
                "speed": 3,
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
                "speed": 3
            }, {
                "name": "Quack",
                "dmg": 1,
                "speed": 5,
                "percent": True,
                "status": {
                    "dmg_boost": 30,
                    "def_boost": 10,
                    "duration": 3
                }
            }, {
                "name": "Bread Throw",
                "dmg": 20,
                "speed": 3,
                "percent": True,
                "status": {
                    "dmg_boost": 0,
                    "def_boost": 10,
                    "duration": 2
                }
            }, {
                "name": "Where is Mom",
                "dmg": 0,
                "speed": 3,
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
                "speed": 3
            }, {
                "name": "Kill Children",
                "dmg": 10,
                "speed": 5,
                "percent": True,
                "status": {
                    "def_boost": 0,
                    "dmg_boost": 40,
                    "duration": 1
                }
            }, {
                "name": "Ghostly Jazz",
                "dmg": 0,
                "speed": 3,
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
                "speed": 3
            }, {
                "name": "Monday Power",
                "dmg": 15,
                "speed": 5,
                "percent": True,
                "status": {
                    "dmg_boost": 50,
                    "def_boost": 0,
                    "duration": 2
                }
            }, {
                "name": "Good Meal",
                "dmg": 0,
                "speed": 3,
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
                "speed": 3
            }
        ],
        "camp": 1
    }
]
