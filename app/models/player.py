class Player():
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice.lower()

    def set_choice(self, choice):
        self.choice = choice.lower()

