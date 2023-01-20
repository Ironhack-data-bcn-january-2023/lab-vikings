import random
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking
class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self): 
        return f"Odin Owns You All!"

    pass

# Saxon
class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

    pass

# War
class War ():

    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking) 
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        Saxon_person = random.choice(self.saxonArmy)
        Viking_person = random.choice(self.vikingArmy)

        result_attack = Saxon_person.receiveDamage(Viking_person.strength) 
       
        if Saxon_person.health == 0:
            self.saxonArmy.remove(Saxon_person)
        else:
            return result_attack

    def saxonAttack(self):
        Saxon_person = random.choice(self.saxonArmy)
        Viking_person = random.choice(self.vikingArmy) 

        result_attack =  Viking_person.receiveDamage(Saxon_person.strength)    
        
        if Viking_person.health == 0:
            self.viking_Army.remove(Viking_person)
        else:
            return result_attack
    pass
