import random

#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            input = int(input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                hero.buy(item)

class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def take_damage(self, attacker, damage): #self, attacker, and damage are arguments to 'take_damage'

        self.health -= damage
        print("{} did {} damage to the {}.\n".format(attacker, damage, self.name))

    def attack(self, enemy):
        if enemy.health <= 0:
            return

        enemy.take_damage(self.name, self.power)


    def alive(self):
        return self.health > 0

    def print_status(self):
        print("{} has {} health and {} power.\n".format(self.name, self.health, self.power))

class Hero(Character):
    def attack(self, enemy): #you are overriding the base (Character) class' attack function
        if self.attack_multiplier():
            enemy.take_damage(self.name, self.power*2)
            print("{} did {} critical damage to the {}.\n".format(self.name, self.power*2, enemy.name))
        else:
            super().attack(enemy)


    def attack_multiplier(self):
        bonus_attack = random.randint(1, 5)
        return bonus_attack == 1

class Medic(Character):
    def take_damage(self, attacker, damage):
        super().take_damage(attacker, damage)
        if self.health_multiplier():
            #self.health + 2 # wrong

            self.health += 2
            print("{} recovered {} health".format(self.name, 2))

    def health_multiplier(self):
        recovery = random.randint(1, 1)
        return recovery == 1

class Goblin(Character):

    pass
class Zambie(Character):

    pass


def main():

    # 4 instantiations
    hero = Hero('Hero', 10, 5)
    goblin = Goblin('Gobblez', 6, 2)
    zombie = Zambie('Zambie', 90, 99)
    medic = Medic('Medic', 50, 3)

    while goblin.alive() and hero.alive() and zombie.alive() and medic.alive():

        hero.print_status()
        goblin.print_status()
        zombie.print_status()
        medic.print_status()

        print("What character do you choose?")
        choice = input("Choose Hero or Medic")
        if choice == "medic":
            char = medic
            print("chose medic")
        else:
            char = hero
            print("chose hero")

        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight zambie")
        print("3. do nothing")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()

        if raw_input == "1":
            # Hero attacks goblin
            char.attack(goblin)
            goblin.attack(char)
            if goblin.health <= 0:
                print("The goblin is dead.")

        elif raw_input == "2":
            char.attack(zombie)
            zombie.attack(char)

        elif raw_input == "3":
            goblin.attack(char)

        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if char.health <= 0:
            print("You are dead.")
            break

if __name__ == "__main__":
    main()


