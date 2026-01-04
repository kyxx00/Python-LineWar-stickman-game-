import random

class Player:
    def __init__(self):
        self.name = "Player"
        self.hp = 20

    def attack(self):
        return random.randint(3, 6)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
