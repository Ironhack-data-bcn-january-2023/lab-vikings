import random

# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength 


    def receiveDamage(self,damage):
        if damage >= 0:
            self.health -= damage
            pass


# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
        
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        if self.health > damage:
            self.health -= damage
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry (self):
        return "Odin Owns You All!"
    
# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        pass

    def attack(self):
        return self.strength
        pass

    def receiveDamage(self, damage):
        if self.health > damage:
            self.health -= damage
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
            pass

# War
class War:
    def __init__(self):
        self.vikingArmy = [] 
        self.saxonArmy = []
        pass

    def addViking(self, Viking):
        if Viking:
            self.vikingArmy.append(Viking)
            pass

    def addSaxon(self, Saxon):
        if Saxon:
            self.saxonArmy.append(Saxon)
            pass


    def vikingAttack(self):
        sax_1= random.choice(self.saxonArmy)
        vik_1= random.choice(self.vikingArmy)
        att_1 = vik_1.receiveDamage(sax_1.strength)
        if (sax_1.health > 0) and (sax_1.health > vik_1.strength): 
                return att_1
        else:
            self.saxonArmy.remove(sax_1)
            return att_1
            pass

    def saxonAttack (self):
        sax_2 = random.choice(self.saxonArmy)
        vik_2 = random.choice(self.vikingArmy)
        att_2 = vik_2.receiveDamage(sax_2.strength)
        if (vik_2.health > 0) and (vik_2.health > sax_2.strength):
            return att_2
        else:
            self.vikingArmy.remove(vik_2)
            return att_2
            pass

    def showStatus(self):
        if (len(self.saxonArmy) == 0):
            return "Vikings have won the war of the century!"
        if (len(self.vikingArmy) == 0):
            return  "Saxons have fought for their lives and survive another day..."
        if (len(self.vikingArmy) == 1) and (len(self.saxonArmy) == 1):
            return "Vikings and Saxons are still in the thick of battle."
            pass