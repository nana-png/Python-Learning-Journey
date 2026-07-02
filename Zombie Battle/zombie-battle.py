class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    


class Player(Character):
    def __init__(self, name, health, damage, heal):
        super().__init__(name, health, damage)
        self.heal = heal

    
    def attack(self, target):
        target.health -= self.damage
        
        print("\n"f"{self.name} attacked {target.name}, dealing {self.damage} damage⚔️!")
        print("\n"f"{target.name} now has {target.health} HP!💥")


    def healPlayer(self):
        self.health += self.heal
        print("\n" f"{self.name} healed {self.heal} and now has {self.health} HP!\n")


    def introduce(self):
        print(f"Player \n Name: {self.name}\n Health: {self.health}\n Damage: {self.damage}\n Heal: {self.heal} \n ")
    

class Zombie(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
    
    def bite(self, opp):
        opp.health -= self.damage
        print("\n" f"{self.name} bit {opp.name}, dealing {self.damage} damage😋")
        print("\n" f"{opp.name} now has {opp.health} HP!😰")

    def introduce(self):
        print(f" Zombie \n Name: {self.name}\n Health: {self.health}\n Damage: {self.damage}\n ")

Bloodbottler = Zombie('Bloodbottler', 120, 30)
Nana = Player('Nana', 100, 20, 20)

Nana.introduce()

Bloodbottler.introduce()

Nana.attack(Bloodbottler)

Bloodbottler.bite(Nana)

Nana.healPlayer()
