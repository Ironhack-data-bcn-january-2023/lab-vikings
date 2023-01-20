
# Soldier


class Soldier:
    def __init__(self, health, strength): 
        self.health = health
        self.strength = strength

    def attack(self):
        return(self.strength)
        

    def receiveDamage(self,damage):
        self.health -= damage
        pass

    



# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health,strength)



    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return f"Odin Owns You All!"
     
    

    
        

    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

    
# War
import random

class War(Viking,Soldier):
    def __init__(self):
        self.vikingarmy = []
        self.saxonarmy = []

    def addViking(self, viking):
        self.vikingarmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonarmy.append(saxon)
    
    def vikingAttack(self):
        sample = random.choice(self.saxonarmy)
        result_viking_attack = sample.receiveDamage(random.choice(self.vikingarmy).strength)
        if result_viking_attack >= sample.health:
            return  self.saxonarmy.remove(sample)
    
    def saxonAttack(self):
        sample_2 = random.choice(self.vikingarmy)
        result_saxon_attack = sample_2.receiveDamage(random.choice(self.saxonarmy).strength)
        if result_saxon_attack >= sample_2.health:
            return self.vikingarmy.remove(sample_2)

    def showStatus(self):
        if len(self.saxonarmy) <= 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingarmy) <= 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle"

    
    



        

    



        
        
    
