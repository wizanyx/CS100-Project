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
                "percent": True
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
    }
]
