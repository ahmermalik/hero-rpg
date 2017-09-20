#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

#4. This is a test.


class Character():
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

class Hero(Character):
    def __init__(self, name = 'Hero', health=10, power=5):
        self.name = name
        self.heath = health
        self.power = power


    def attack(self, enemy):
            # Hero attacks goblin
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))




class Goblin(Character):
    def ___init__(self, name = 'Goblin', health=6, power=2):
        self.name = name
        self.health = health
        self.power = power






def main():
    hero_health = 10
    hero_power = 5
    goblin_health = 6
    goblin_power = 2
    hero = Hero('Hero', 10, 5)
    goblin = Goblin('Goblin', 6, 2)

    while goblin_health > 0 and hero_health > 0:
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            # goblin_health -= hero_power
            # print("You do {} damage to the goblin.".format(hero_power))
            hero.attack(goblin)
            if goblin_health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            hero_health -= goblin_power
            print("The goblin does {} damage to you.".format(goblin_power))
            if hero_health <= 0:
                print("You are dead.")

main()
