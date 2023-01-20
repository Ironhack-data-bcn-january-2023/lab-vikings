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
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)

        result_of_atack = random_saxon.receiveDamage(random_viking.strength)

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
            return result_of_atack
        
        else:
            return result_of_atack

                
    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        result_of_atack = random_viking.receiveDamage(random_saxon.strength)

        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
            return result_of_atack
        
        return result_of_atack

    def showStatus (self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.vikingArmy) >= 1 or len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."