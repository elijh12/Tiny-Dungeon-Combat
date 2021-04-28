import random

def rollTest(min, max, num):
    wasSuccess = False

    roll_1 = random.randint(min, max) # will always roll at least once, but only once is disadvantage
    roll_2 = 0
    roll_3 = 0

    if num == 2: # normal number of times to roll
        roll_2 = random.randint(min, max)

    elif num == 3: # advantage
        roll_2 = random.randint(min, max)
        roll_3 = random.randint(min, max)

    if roll_1 == 3 or roll_2 == 3 or roll_3 == 3:
        wasSuccess = True

    return wasSuccess


class Player:
    def __init__(self, heritage, trait1, trait2):
        if heritage == "human":
            self.health = 7
            self.healthmax = 7
            self.weapon = 1
            self.numTraits = 2
            self.heal = 2
        elif heritage == "dwarf":
            self.health = 8
            self.healthmax = 8
            self.weapon = 2
            self.numTraits = 1
            self.heal = 2
        elif heritage == "fey":
            self.health = 6
            self.healthmax = 6
            self.weapon = 2
            self.numTraits = 1
            self.heal = 4

        self.heritage = heritage
        if trait1 == 1 or trait2 == 1: # Armor Master
            self.health += 2
        if trait1 == 2 or trait2 == 2: # Healer
            self.heal += 1
        if trait1 == 3 or trait2 == 3: # Brutal
            self.weapon += 1
        

class Enemy:
    def __init__(self, health, weapon, heal):
        self.health = health
        self.healthmax = health
        self.weapon = weapon
        self.heal = heal

    def determineAction(self, enemy, hasDisadv):
        chance = random.randint(1, 3)
        if self.health < 2 and chance == 3:
            print("It licks its wounds!")
            heal(self, False)
        else:
            print("It attacks you!")
            attack(self, enemy, False, hasDisadv, False)


def attack(attacker, enemy, adv, disadv, isPlayer):
    if adv:
        didHit = rollTest(1, 3, 3)
    elif disadv:
        print("Rolling with Disadvantage...")
        didHit = rollTest(1, 3, 1)
    else:
        didHit = rollTest(1, 3, 2)

    if didHit:
        enemy.health -= attacker.weapon

    if isPlayer and didHit:
        print("Nice hit! :)\n")
    elif isPlayer and not didHit:
        print("Oop! You missed :(\n")
    elif not isPlayer and didHit:
        print("Oh no! It got you! :(\n")
    else:
        print("You dodged it! :)\n")

def heal(person, isPlayer):
    if person.health + person.heal > person.healthmax:
        person.health = person.healthmax
    else:
        person.health += person.heal

    if isPlayer:
        print("You healed {} HP!\n".format(person.heal))
    else:
        print("They healed {} HP!\n".format(person.heal))

def displayStats(person):
    print("\n---------------------------")
    print("Your Stats:")
    print("Max Health: {}".format(person.health))
    print("Damage: {}".format(person.weapon))
    print("Heal Power: {}".format(person.heal))
    print("---------------------------\n")


def main():
    print("Welcome!")
    print("Character Customization:")
    print("Human: Extra Health and Extra Increase!")
    print("Dwarf: Extra Health and Extra Damage!")
    print("Fey: Extra Damage and Extra Heal!")
    heri = ""
    while heri != "human" and heri != "dwarf" and heri != "fey":
        heri = str(input("Please enter your chosen heritage (human, dwarf, or fey): "))

    print("Please select your trait(s):")
    print("1: Armor Master (Bonus to Defense)")
    print("2: Healer (Bonus to Heal)")
    print("3: Brutal (Bonus to Damage)")
    trait_1 = int(input(": "))

    if heri == "human":
        trait_2 = int(input("Please enter your second trait: "))
    else:
        trait_2 = 0

    player1 = Player(heri, trait_1, trait_2)

    print("Would you like to play on:\n1. Easy\n2. Normal\n3. Hard")
    diff = int(input(": "))
    if diff == 1:
        enemy1 = Enemy(4, 1, 2)
    elif diff == 2:
        enemy1 = Enemy(8, 2, 3)
    else:
        enemy1 = Enemy(15, 3, 4)

    displayStats(player1)

    while player1.health > 0 and enemy1.health > 0:
        hasDisadv = False
        print("It's your turn!")
        print("You can: \n1. Attack!\n2. Heal\n3. Dodge!")
        choice = int(input(": "))

        print("")

        if choice == 1:
            hit = attack(player1, enemy1, False, False, True)
        elif choice == 2:
            heal(player1, True)
        else:
            hasDisadv = True

        if enemy1.health > 0:
            print("Enemy's turn!\n")
            enemy1.determineAction(player1, hasDisadv)
            print("---------------------------")
            print("Your current health: {}".format(player1.health))
            print("Enemy's current health: {}".format(enemy1.health))
            print("---------------------------\n")

    if player1.health == 0:
        print("Ha, you ded.")
    if enemy1.health == 0:
        print("Congrats! You are victorious!")


main()
