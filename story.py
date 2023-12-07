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
    "'As expected of on evil creature'",
    "You firm your gaze and step forward",
    "And then you hear it...",
    "That heavenly sound...",
    "As if to answer your resolve",
    '"ITZA MEE DARRIOOO"'
], [
    "#@$%! THEY CAME OUTTA NOWHERE!!!",
    "But that holy halo...",
    "NO!!! That evil creature is at it again.",
    "Trying to waver my resolve...",
    "It underestimates me too much.",
    "But I never expected he would have help...",
    "Thankfully Dario was there to help me.",
    "But I need to be vigilant.",
    "Who knows if the beast has any other tricks up his sleeve?",
    "What if he finds more helpers?",
    "This won't do. I need to set off immediately.",
    "....................",
    "A FEW MOMENTS LATER",
    "....................",
    "You suddenly hear the sounds of fighting and rush over.",
    "But after seeing the person in front of you...",
    "You can't believe your eyes.",
    "It is he, the chosen one, the lover and the saviour",
    "IT IS FESUS!!!",
    "Fesus turns around and looks at you...",
    "You faintly hear a sigh escape his mouth.",
    "For sure it must have been your imagination..."
    "But suddenly, you dont have time to think anymore.",
    "For you see it once again..."
], [
    "You gain another victory...",
    "But this time remains not the triumph...",
    "But just a hollowness.",
    "You don't understand what is happening...",
    "But you know this isn't good.",
    "And Fesus just looks at you with pity",
    "As if he is aware of your impending doom.",
    "** A Random Wojak has spwaned. **",
    "You look at the man in front you...",
    "And you somehow feel a sense of camaraderie.",
    "So you extend to him your friendship.",
    "Just as wojak accepts to become your teammate.",
    "You see an orange cat and have a bad premonition..."
], [
    "What was that horrifying creature?",
    "And why is this happening?",
    "As you feel you mind being eroded,",
    "You suddenly hear a surprised Fesus",
    "'What is he doing here?'",
    "He turns to looks at you and sighs,",
    "'Looks like you may have some chance after all...",
    "Just hope RNG God is on your side.'",
    "'You need to get ready...'",
    "'We are running out of time.'",
    "'Oh, looks like he is here.'",
    "He says looking over your  shoulder.",
    "You look back and can't help but be startled..,",
    "'PROFRESSOR!!??'",
    "'....'",
    "'Oh no, please don't fail me'"
]
]


class Story:
    def __init__(self):
        self.stage = 0

    def next_line(self):
        if STORY[self.stage]:
            return STORY[self.stage].pop(0)

    @property
    def stage_lines(self):
        return STORY[self.stage]

    @property
    def characters(self):
        if self.stage == 0:
            return [["Man"], ["Dog"]]
        elif self.stage == 1:
            return [["Man", "Dario"], ["Angel Dog", "Monal Muck"]]
        elif self.stage == 2:
            return [["Man", "Dario", "Fesus"], ["Devil Dog", "Monal Muck", "Jreddy Jazbear"]]
        elif self.stage == 3:
            return [["Man", "Dario", "Fesus", "Wojak"], ["Eldritch Dog", "Jreddy Jazbear", "Garfield"]]
        elif self.stage == 4:
            return [["Man", "Dario", "Fesus", "Wojak", "Saitama"], ["Professor Guarnera"]]

