from player import Player
from enemy import Enemy
from combat import fight
from utils import show_title

def main():
    show_title()
    player_name = input("Enter your name: ")

    player = Player(player_name)
    enemy = Enemy("Enemy Stickman")

    fight(player, enemy)

if __name__ == "__main__":
    main()
