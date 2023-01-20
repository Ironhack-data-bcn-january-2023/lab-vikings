
# Soldier
import random

class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength 

    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        if self.health > 0:
             self.health -= damage




# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self,damage):  
        if self.health > 0 and damage < self.health:
             self.health -= damage
             return f"{self.name} has received {damage} points of damage"
        else:
             return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health, strength)

    def receiveDamage(self,damage):  
        if self.health > 0 and damage < self.health:
             self.health -= damage
             return f"A Saxon has received {damage} points of damage"
        else:
             return f"A Saxon has died in combat"        


    

# War


class War(Viking,Saxon):
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        viking_i = random.choice(self.vikingArmy)
        saxon_i  = random.choice(self.saxonArmy)
        #viking_i = self.vikingArmy[random.randint(1,len(self.vikingArmy))]

        if saxon_i.health > 0 and viking_i.strength < saxon_i.health:
            saxon_i.receiveDamage(viking_i.strength)
            return saxon_i.receiveDamage(viking_i.strength)
        else:
            saxon_i.receiveDamage(viking_i.strength)
            self.saxonArmy.remove(saxon_i)
            return saxon_i.receiveDamage(viking_i.strength)     

    def saxonAttack(self):
        viking_i = random.choice(self.vikingArmy)
        saxon_i  = random.choice(self.saxonArmy)
        #viking_i = self.vikingArmy[random.randint(1,len(self.vikingArmy))]

        if viking_i.health > 0 and saxon_i.strength < viking_i.health:
            return viking_i.receiveDamage(saxon_i.strength)
        else:
            saxon_i.receiveDamage(viking_i.strength)
            return self.vikingArmy.remove(viking_i)

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)>0 or len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."




        
        

        


