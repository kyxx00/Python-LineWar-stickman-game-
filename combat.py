import time
from utils import show_fight, show_win, show_lose

def fight(player, enemy):
    print("\nA fight has started!")

    while player.hp > 0 and enemy.hp > 0:
        show_fight()
        print(f"{player.name} HP: {player.hp}")
        print(f"{enemy.name} HP: {enemy.hp}")

        print("\nChoose an action:")
        print("1. Attack")
        print("2. Block")

        choice = input("> ")

        if choice == "1":
            damage = player.attack()
            enemy.take_damage(damage)
            print(f"You attack for {damage} damage!")
            print(f"Enemy HP is now {enemy.hp}")
            time.sleep(1)

        elif choice == "2":
            print("You block and reduce damage this turn.")

        else:
            print("Invalid choice. You lose your turn.")

        if enemy.hp > 0:
            enemy_damage = enemy.attack()

            if choice == "2":
                enemy_damage -= 2
                if enemy_damage < 0:
                    enemy_damage = 0

            player.take_damage(enemy_damage)
            print(f"Enemy attacks for {enemy_damage} damage!")
            print(f"Your HP is now {player.hp}")
            time.sleep(1)

    if player.hp > 0:
        show_win()
        print("You won the fight!")
    else:
        show_lose()
        print("You lost the fight...")

    again = input("Play again? (y/n): ").lower()
    if again == "y":
        player.hp = 20
        enemy.hp = 15
        fight(player, enemy)
    else:
        print("Thanks for playing!")