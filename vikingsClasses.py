


# Soldier


class Soldier ():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack (self):
        return self.strength


    def receiveDamage (self, the_damage):
        self.health -= the_damage
        pass

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage (self, the_damage):
        self.health -= the_damage
        if self.health > 0:
            return f"{self.name} has received {the_damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def attack (self):
        return self.strength

    def receiveDamage (self, the_damage):
        self.health -= the_damage
        if self.health > 0:
            return f"A Saxon has received {the_damage} points of damage"
        elif self.health <= 0:
            return "A Saxon has died in combat"


import random

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking (self, Viking):
        if Viking:
            self.vikingArmy.append(Viking)
        pass

    def addSaxon(self, Saxon):
        if Saxon:
            self.saxonArmy.append(Saxon)
        pass
    
    def vikingAttack(self):
        random_Saxon = random.choice(self.saxonArmy)
        random_Viking = random.choice(self.vikingArmy)
        random_Saxon.receiveDamage(random_Viking.strength)
        if random_Saxon.health <= 0:
            self.saxonArmy.remove(random_Saxon)
            return "A Saxon has died in combat"
    
    def saxonAttack(self):
        random_Saxon = random.choice(self.saxonArmy)
        random_Viking = random.choice(self.vikingArmy)
        result = random_Viking.receiveDamage(random_Saxon.strength)
        if random_Viking.health <= 0:
            self.vikingArmy.remove(random_Viking)
        return result
    
    def showStatus(self):
        
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy) <= 0:
            return "Vikings have won the war of the century!"
        else:
            return "Saxons have fought for their lives and survive another day..."



