class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.attack_power = 5

    def attack(self):
        return self.attack_power

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
