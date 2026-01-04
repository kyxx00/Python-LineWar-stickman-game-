from player import Player
from enemy import Enemy
from combat import fight

def main():
    print("=== Stickman Fight ===")

    player = Player()
    enemy = Enemy()

    fight(player, enemy)

if __name__ == "__main__":
    main()
