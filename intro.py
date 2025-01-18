import time

# Definiera klassen för spelaren (aka main karaktären)
class Player:
    def __init__(self, name, strength=10, hp=100, level=1):
        self.name = name
        self.strength = strength  # Standard styrka
        self.hp = hp  # Standard HP
        self.inventory = []  # Startar tom, hoppas man hittar nåt nice lol
        self.level = level  # Spelarens nivå

    def __str__(self):
        # Typ "status"-grej för spelaren
        return f"Player: {self.name}, Strength: {self.strength}, HP: {self.hp}, Level: {self.level}, Inventory: {self.inventory}"
    
    def level_up(self):
        # När spelaren går upp en nivå
        self.level += 1
        self.strength += 5  # Lite extra gains varje gång
        print(f"{self.name} har levelat upp! Nu är du på level {self.level}, Styrka: {self.strength}")

    def add_item_to_inventory(self, item):
        # Lägg till grejer till inventoryt
        self.inventory.append(item)
        print(f"{item} är nu i din inventory. Soft!")

    def take_damage(self, damage):
        # Spelaren får skada (inte nice)
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name} blev slått ut! GG.")
        else:
            print(f"{self.name} har {self.hp} HP kvar. Håll ut!")

    def heal(self, healing_amount):
        # Någon eller nåt healar spelaren
        self.hp += healing_amount
        print(f"{self.name} blev healad med {healing_amount} HP. HP just nu: {self.hp}")

# Huvudkod för att interagera med spelaren

# Fråga om spelarens namn och skapa spelaren
name = input("Gammal gubbe: Hej där resenär, vad heter du? ")
player = Player(name)  # Ny spelare 

print(f"Kul att träffas, {name}. Legenden säger att ett av dessa dörrar leder till en bests rum. Ingen tid att förlora, vi drar till rustkammaren.")
time.sleep(5)

# Kör en annan fil med loot room inom samma process
with open('lootroom.py') as f:
    exec(f.read())