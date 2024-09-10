import random


class Character:
    def __init__(self, name, magic_power, strength, health, armor, fatigue):
        self.name = name
        self.magic_power = magic_power
        self.strength = strength
        self.health = health
        self.armor = armor
        self.fatigue = fatigue
        self.items = {'Food': 5}

    def rest(self):
        self.health += 70
        self.fatigue -= 60
        print(f"{self.name} rested and fatigue decreased, health increased")

    def use_item(self, item):
        if item in self.items and self.items[item] > 0:
            if item == 'Food':
                self.health += 20
                self.items[item] -= 1
                print(f"{self.name} ate food and health increased!")
        else:
            print(f"No {item} left!")

    def attack(self, enemy):
        if self.name == "Wizard":
            damage = self.magic_power - (enemy.armor // 2)
            enemy.health -= damage
            print(f"{self.name} dealt {damage} damage to {enemy.name}")
        else:
            damage = self.strength - (enemy.armor // 2)
            enemy.health -= damage
            print(f"{self.name} dealt {damage} damage to {enemy.name}")

    def __str__(self):
        return f"name: {self.name}, health: {self.health}, strength: {self.strength}, magic power: {self.magic_power}, armor: {self.armor}, fatigue: {self.fatigue}"


class Human(Character):
    def __init__(self):
        super().__init__("Human", magic_power=0, strength=random.randrange(50,100), health=400, armor=40, fatigue=0)


class Elf(Character):
    def __init__(self):
        super().__init__("Elf", magic_power=10, strength=random.randrange(50,100), health=400, armor=20, fatigue=0)


class Wizard(Character):
    def __init__(self):
        super().__init__("Wizard", magic_power=random.randrange(75,100), strength=10, health=400, armor=25, fatigue=0)


class Dwarf(Character):
    def __init__(self):
        super().__init__("Dwarf", magic_power=0, strength=random.randrange(50,100), health=400, armor=50, fatigue=0)


class Enemy:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, character):
        character.health -= self.damage
        print(f"{self.name} attacked {character.name} and dealt {self.damage} damage!")


locations = [
    {'name': 'Forest', 'enemies': [Enemy('Goblin', 100, random.randrange(10,30), 10)]},
    {'name': 'Cave', 'enemies': [Enemy('Goblin', 100, random.randrange(10,30), 10), Enemy('Giant Goblin', 100, random.randrange(20,30), 20)]},
    {'name': 'Orc Camp', 'enemies': [Enemy('Orc', 100, random.randrange(25,30), 20)]},
    {'name': 'Uruk-hai Territory', 'enemies': [Enemy('Uruk-hai', 100, random.randrange(30,35), 35)]},
    {'name': 'Mountain Pass', 'enemies': [Enemy('Uruk-hai', 100, random.randrange(30,35), 35), Enemy('Giant Orc', 150, random.randrange(30,35), 40)]},
]


def select_character():
    probabilities = [35, 25, 15, 30]
    choice = random.choices(['Human', 'Elf', 'Wizard', 'Dwarf'], weights=probabilities, k=1)[0]

    if choice == 'Human':
        return Human()
    elif choice == 'Elf':
        return Elf()
    elif choice == 'Wizard':
        return Wizard()
    elif choice == 'Dwarf':
        return Dwarf()


def game_loop():
    hero = select_character()
    print(f"Your character is {hero}")
    days_remaining = 10

    for i, location in enumerate(locations):
        print(f"\n{i + 1}. Location: {location['name']}")
        for enemy in location['enemies']:
            while enemy.health > 0 and hero.health > 0:
                hero.attack(enemy)
                if enemy.health > 0:
                    enemy.attack(hero)
                else:
                    hero.fatigue -= 10
                    print(f"{enemy.name} died and our character's fatigue is: {hero.fatigue}")

                if hero.health <= 0:
                    print("Your hero has died. Game Over.")
                    return

        if i < len(locations) - 1:
            print(f"{location['name']} is completed. Hero: {hero}")
            choice = input("Do you want to rest? (yes/no): ").lower()
            if choice == 'yes':
                hero.rest()
                days_remaining -= 1

            if days_remaining <= 0:
                print("The days have finished. You could not achieve it.")
                return

    print("Congrats! You won.")


game_loop()


