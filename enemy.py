import random

class Enemy:
    def __init__(self):
        self.name = "Enemy"
        self.hp = 15

    def attack(self):
        return random.randint(2, 5)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
