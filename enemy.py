import random

class Enemy:
    def __init__(self, name):
        self.name = name
        self.hp = 15

    def attack(self):
        return random.randint(1, 4)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0