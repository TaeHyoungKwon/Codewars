import random


class Ghost:
    def __init__(self):
        self.color_list = ['white', 'yellow', 'purple', 'red']

    @property
    def color(self):
        return random.choice(self.color_list)