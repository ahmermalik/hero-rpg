#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class
class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("You do {} SUPER-DUPER damage to the goblin.".format(self.power))

    def alive(self):
        if self.health > 0:
            return True
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))

    def alive(self):
        if self.health > 0:
            return True

    def print_status(self):
        print("The goblin has {} health and {} power.\n".format(self.health, self.power))


def main():
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
    while goblin.alive() and hero.alive():

        hero.print_status()
        goblin.print_status()

        print("What do you want to do?\n")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
            print("You do {} damage to the goblin.".format(hero.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
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