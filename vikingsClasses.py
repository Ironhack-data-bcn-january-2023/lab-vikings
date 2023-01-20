import random
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        pass
    def attack(self):
        return (self.strength)
    def receiveDamage(self, damage):
        self.health=self.health-damage
        return
    pass


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
        pass
    def attack(self):
        return (self.strength)
    def receiveDamage(self, damage):
        if self.health>damage:
            self.health=self.health-damage
            return f"{self.name} has received {damage} points of damage"
            pass
        else:
            return f"{self.name} has died in act of combat"
            pass
        pass
    def battleCry (self):
        return "Odin Owns You All!"
    pass

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        pass
    def attack(self):
        return (self.strength)
    def receiveDamage(self, damage):
        if self.health>damage:
            self.health=self.health-damage
            return f"A Saxon has received {damage} points of damage"
            pass
        else:
            return f"A Saxon has died in combat"
            pass
        pass
    pass

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        pass

    def addViking (self, Viking):
        self.vikingArmy.append(Viking)
        pass
    def addSaxon (self, Saxon):
        self.saxonArmy.append(Saxon)
        pass
    
    def vikingAttack(self):
        viking=random.choice(self.vikingArmy)
        saxon=random.choice(self.saxonArmy)
        attac=saxon.receiveDamage(viking.strength)
        if saxon.health <=0:
            self.saxonArmy.remove(saxon)
            return attac
        elif saxon.health > 0:
            return attac
        pass
    


    def saxonAttack(self):
        viking=random.choice(self.vikingArmy)
        saxon=random.choice(self.saxonArmy)
        attacks=viking.receiveDamage(saxon.strength)
        if viking.health <=0:
            self.vikingArmy.remove(viking)
            return attacks
        elif viking.health > 0:
            return attacks 
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)!= 0 or len(self.vikingArmy)!=0:
            return "Vikings and Saxons are still in the thick of battle."
