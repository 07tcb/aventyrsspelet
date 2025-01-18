import random

# Item
class Item:
    def __init__(self, name, strength_bonus):
        self.name = name
        self.strength_bonus = strength_bonus

    def __str__(self):
        return f"{self.name} (+{self.strength_bonus} STR)"

# Player
class Player:
    def __init__(self, hp=10, strength=5, level=1):
        self.hp = hp
        self.strength = strength
        self.level = level
        self.inventory = []

    def show_stats(self):
        print(f"HP: {self.hp}, STR: {self.strength}, LVL: {self.level}")

    def show_inventory(self):
        if self.inventory:
            print("Inventory:")
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item}")
        else:
            print("Inventory: Tomt")

    def add_item(self, item):
        if len(self.inventory) < 5:
            self.inventory.append(item)
            self.strength += item.strength_bonus
            print(f"Du lade till {item} i din inventory.")
        else:
            print("Din inventory är full! Vill du byta ut ett föremål? (ja/nej)")
            choice = input().strip().lower()
            if choice == "ja":
                self.show_inventory()
                index = int(input("Ange numret på föremålet du vill byta ut: ")) - 1
                if 0 <= index < len(self.inventory):
                    removed_item = self.inventory.pop(index)
                    self.strength -= removed_item.strength_bonus
                    self.inventory.append(item)
                    self.strength += item.strength_bonus
                    print(f"Du bytte ut {removed_item} mot {item}.")
                else:
                    print("Ogiltigt val.")
            else:
                print("Du lämnade föremålet.")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"Du förlorade {damage} HP.")

    def gain_level(self):
        self.level += 1
        print("Du gick upp i level!")

# Events eeee

def fight_monster(player):
    monster_strength = random.randint(3, 10)
    print(f"Du möter ett monster med STR {monster_strength}!")

    if monster_strength > player.strength:
        print("Monstret besegrar dig!")
        player.take_damage(1)
    elif player.strength > monster_strength:
        print("Du besegrar monstret!")
        player.gain_level()
    else:
        print("Det blev oavgjort. Ingen tar skada.")

    if player.hp <= 0:
        print("Du har förlorat! Spelet är över.")
        return False

    if player.level >= 10:
        print("Grattis! Du har nått LVL 10 och vunnit spelet.")
        return False

    return True

def find_chest(player):
    item_name = random.choice(["Svärd", "Sköld", "Ring", "Hjälm", "Rustning"])
    strength_bonus = random.randint(1, 3)
    new_item = Item(item_name, strength_bonus)
    print(f"Du hittar en kista! Den innehåller {new_item}.")
    player.add_item(new_item)

def trigger_trap(player):
    damage = random.randint(1, 3)
    print(f"Du fastnar i en fälla och tar {damage} skada!")
    player.take_damage(damage)

    if player.hp <= 0:
        print("Du har förlorat! Spelet är över.")
        return False

    return True

def door_event(player):
    event = random.choice(["monster", "chest", "trap"])
    if event == "monster":
        return fight_monster(player)
    elif event == "chest":
        find_chest(player)
    elif event == "trap":
        return trigger_trap(player)
    return True

# loopar

def main():
    print("Välkommen till äventyret!")
    player = Player()
    running = True

    while running:
        print("\nVad vill du göra?")
        print("1. Visa egenskaper")
        print("2. Visa inventory")
        print("3. Välj en dörr")
        choice = input("Ditt val: ").strip()

        if choice == "1":
            player.show_stats()
        elif choice == "2":
            player.show_inventory()
        elif choice == "3":
            print("Du står framför tre dörrar: framåt (1), höger (2), vänster (3).")
            door_choice = input("Vilken dörr vill du öppna? (1/2/3): ").strip()
            if door_choice in ["1", "2", "3"]:
                print(f"Du öppnar dörr {door_choice}...")
                running = door_event(player)
            else:
                print("Ogiltigt val. Välj 1, 2 eller 3.")
        else:
            print("Ogiltigt val. Försök igen.")

        if not running:
            print("Spelet är slut.")

if __name__ == "__main__":
    main()
