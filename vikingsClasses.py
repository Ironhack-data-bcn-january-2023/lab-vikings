import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
       self.health = health 
       self.strength = strength 
       pass
    def attack(self):
        return (self.strength)
    def receiveDamage(self, damage):
        self.health -= damage
        return
    pass

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

    def battleCry(self):
        return "Odin Owns You All!"
    pass

# Saxon

class Saxon(Soldier):
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"
            pass
 

# War


class War(Viking, Saxon):
    def __init__(self):
        self.saxoAarmy = []
        self.vikingArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        

def vikingAttack(self):
    if self.saxonArmy:
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = viking.attack()
        result = saxon.receiveDamage(damage)
    if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
    return result
     

def xaxonAttack(self):
    if self.saxonArmy:
        viking_1 = random.choice(self.vikingArmy)
        saxon_1 = random.choice(self.saxonArmy)

        damage = viking_1.attack()
        result = saxon_1.receiveDamage(damage)
        if saxon_1.health <= 0:
            self.saxonArmy.remove(saxon_1)
        return result

def saxonAttack(self):
    if len(self.vikingArmy) > 0 and len(self.saxonArmy) > 0:
        saxon_1 = random.choice(self.saxonArmy)
        viking_1= random.choice(self.vikingArmy)
        damage = saxon_1.attack()
        result = viking_1.receiveDamage(damage)
        if viking_1.health <= 0:
            self.vikingArmy.remove(viking_1)
        return result
    else:
        return None