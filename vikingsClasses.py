
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

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
        pass
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
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        if self.health > damage:
            self.health -= damage
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.vikingArmy= []
        self.saxonArmy = []

    def addViking(self, *Viking):
        if Viking:
            self.vikingArmy.append(Viking)

    def addSaxon(self,*Saxon):
        if Saxon:
            self.saxonArmy.append(Saxon)
            

    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        attack = saxon.receiveDamage(viking.strength)
        if saxon.health >= 0 :
            self.saxonArmy.remove(saxon)
        else:
            return attack

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        attackDamage = viking.receiveDamage(viking.strength)
        if viking.health >= 0 :
            self.vikingArmy.remove(viking)
        elif viking.health < 0:


    def showStatus(self):
        if len(saxonArmy)== 0:
            return "Vikings have won the war of the century!"
        elif len(vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(saxonArmy) and len(vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."

