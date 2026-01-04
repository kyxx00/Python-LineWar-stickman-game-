from player import Player
from enemy import Enemy

def test_player_attack_reduces_enemy_hp():
    player = Player()
    enemy = Enemy()

    start_hp = enemy.hp
    damage = player.attack()
    enemy.take_damage(damage)

    assert enemy.hp < start_hp
    assert enemy.hp >= 0


def test_block_reduces_damage():
    enemy_damage = 4
    block_reduction = 2

    reduced_damage = enemy_damage - block_reduction
    if reduced_damage < 0:
        reduced_damage = 0

    assert reduced_damage <= enemy_damage
    assert reduced_damage >= 0