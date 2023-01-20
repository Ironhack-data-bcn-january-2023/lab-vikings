import random

# Soldier
class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength 
        pass

    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health -= damage


    pass

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
                    
        pass

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!" 
      
    pass

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return "A Saxon has died in combat"
    pass

# War

class War():

    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
        pass
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)
        pass

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        pass

    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        attackDamage = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
            return attackDamage
        elif saxon.health > 0:
            return attackDamage
        
        pass

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        attackDamage = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            return attackDamage
        elif viking.health > 0:
            return attackDamage 

        pass

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) != 0 or len(self.saxonArmy) != 0:
            return "Vikings and Saxons are still in the thick of battle."

        
            
            pass
