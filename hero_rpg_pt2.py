#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


import random


class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        if enemy.health <= 0:
            return

        enemy.health -= self.power
        print("{} did {} SUPER-DUPER damage to the {}.\n".format(self.name, self.power, enemy.name))

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print("{} has {} health and {} power.\n".format(self.name, self.health, self.power))

class Hero(Character):

    def __init__(self, name, health, power, special):
        self.special = special
        super().___init___(name, health, power)

    def attack_multiplier(self):
        bonus_attack = random.randint(1, 5)
        if 1 == str(bonus_attack):
            print(bonus_attack)
            return True



class Goblin(Character):

    pass
class Zambie(Character):

    pass


def main():
    hero = Hero('Hero', 10, 5)
    goblin = Goblin('Gobblez',6, 2)
    zambie = Zambie('Mr.Zambie',9001,9001)
    while goblin.alive() and hero.alive():

        hero.print_status()
        goblin.print_status()

        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight zambie")
        print("3. do nothing")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            zambie.attack(hero)

        elif raw_input == "3":
            pass

        elif raw_input=="4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)

        if hero.health <= 0:
            print("You are dead.")

main()