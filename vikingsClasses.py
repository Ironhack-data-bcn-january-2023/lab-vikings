import random
# Soldier


class Soldier():
    
    def __init__(self, health,strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    def receiveDamage(self,damage_input):
        self.health -= damage_input
        pass

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name

    def receiveDamage(self, damage_input):
        self.health-=damage_input
        if self.health>0:
            return f'{self.name} has received {damage_input} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        return 'Odin Owns You All!'
    
    

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receiveDamage(self, damage_input):
        self.health-=damage_input
        if self.health>0:
            return f'A Saxon has received {damage_input} points of damage'
        else:
            return f'A Saxon has died in combat'

# War


class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
        pass
    def addViking(self,viking):
        self.vikingArmy.append(viking)

    def addSaxon(self,saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        result_of_attack = random_saxon.receiveDamage(random_viking.strength)
        if random_saxon.health>0:
            return result_of_attack
        else:
            self.saxonArmy.remove(random_saxon)
            return result_of_attack
       
    
    def saxonAttack(self):
  

        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        result_of_attack=random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health>0:
            return result_of_attack
        else:
            self.vikingArmy.remove(random_viking)
            return result_of_attack
    
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy)==0:
            return 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy)==1 or len(self.vikingArmy)==1:
            return 'Vikings and Saxons are still in the thick of battle.'