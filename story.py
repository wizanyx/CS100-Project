STORY = [[
    "You are a normal Human.",
    "And it was a normal day.",
    "And then you saw it.",
    "THAT BEAST",
    "You knew from one look...",
    "you were fated enemies.",
    "So you took the plunge",
    "And stood up to fight it",
    "To fight that beast... that dog.",
    "And everything changed forever..."
], [
    "You've done it...",
    "You've defeated your fated enemy.",
    "You killed the dog...",
    "'I'm sure it was evil...'",
    "'It has to be...'",
    "'But it's last whimper was so sad.'",
    "'NO!!! I won't fall for these petty tricks'",
    "'Trying to waver my resolve even at its last breath'",
    "'As expected on evil creature'",
    "You firm your gaze and step forward",
    "And then you hear it...",
    "That heavenly sound...",
    "As if to answer your resolve",
    '"ITZA MEE DARRIOOO"'
]
]


class Story:
    def __init__(self):
        self.stage = 0

    def next_line(self):
        if STORY[self.stage]:
            return STORY[self.stage].pop(0)

    def characters(self):
        if self.stage == 0:
            return [["Man"], ["Dog"]]
        elif self.stage == 1:
            return [["Man", "Dario"], ["Angel Dog", "Monald Muck"]]
