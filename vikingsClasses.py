import random
class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
        #self.damage= 0
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage 
        return

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry (self):
            return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        
# War
class War():

    def __init__(self):
        self.saxonArmy = []
        self.vikingArmy = []
    
    def addViking (self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon (self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack (self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        saxon.receiveDamage(viking.strength)

        if saxon.health <= 0:
            del saxon
                
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        viking.receiveDamage(saxon.strenght)

        if viking.health <= 0:
            del viking

    def showStatus (self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."