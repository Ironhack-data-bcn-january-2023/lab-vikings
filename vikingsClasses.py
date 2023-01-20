
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
          
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        if self.health > 0:
            self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        
        self.name = name
        
    def receiveDamage(self, damage):
        if self.health > 0 and damage < self.health:
            self.health -= damage
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        
    def receiveDamage(self, damage):
        if self.health > 0 and damage < self.health:
            self.health -= damage
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War


import random
class War(Viking, Saxon):
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        if Viking: 
            self.vikingArmy.append(Viking)
                   
    def addSaxon(self, Saxon):
        if Saxon:
            self.saxonArmy.append(Saxon)
               
    def vikingAttack(self):
        viking_1 = random.choice(self.vikingArmy)
        saxon_1 = random.choice(self.saxonArmy)
        
        if saxon_1.health > 0 and viking_1.strength < saxon_1.health:
            saxon_1.receiveDamage(viking_1.strength)
            
        else:
            saxon_1.receiveDamage(viking_1.strength)
            self.saxonArmy.remove(saxon_1)
        
    
    def saxonAttack(self):
        viking_1 = random.choice(self.vikingArmy)
        saxon_1 = random.choice(self.saxonArmy)
        
        if viking_1.health > 0 and saxon_1.strength < viking_1.health:
            viking_1.receiveDamage(saxon_1.strength)
            
        else:
            viking_1.receiveDamage(saxon_1.strength)
            self.vikingArmy.remove(viking_1)


    def showStatus(self):
        if len(self.vikingArmy) > len(self.saxonArmy):
            return "Vikings have won the war of the century!"
        
        elif len(self.saxonArmy) > len(self.vikingArmy):
            return "Saxons have fought for their lives and survive another day..."
        
        else: 
            return "Vikings and Saxons are still in the thick of battle."




