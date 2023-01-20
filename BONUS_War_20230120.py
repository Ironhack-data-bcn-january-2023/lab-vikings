# new_file.py

from vikingsClasses import Soldier, Viking, Saxon, War

def createVikingTeam():
    #create a team of Vikings
    viking1 = Viking("Eirik", 100, 25)
    viking2 = Viking("Olaf", 150, 30)
    viking3 = Viking("Bjorn", 120, 20)
    return [viking1, viking2, viking3]

def createSaxonTeam():
    #create a team of Saxons
    saxon1 = Saxon(80, 15)
    saxon2 = Saxon(90, 20)
    saxon3 = Saxon(70, 10)
    return [saxon1, saxon2, saxon3]

def startWar(vikingTeam, saxonTeam):
    war = War()
    for viking in vikingTeam:
        war.addViking(viking)
    for saxon in saxonTeam:
        war.addSaxon(saxon)
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        war.vikingAttack()
        war.saxonAttack()
    print(war.showStatus())

vikingTeam = createVikingTeam()
saxonTeam = createSaxonTeam()
startWar(vikingTeam, saxonTeam)

# the createVikingTeam() 
# function creates a team of Viking objects 
# with different set attributes and returns a list 
# of those objects. Similarly, the createSaxonTeam() 
# function creates a team of Saxon objects 
# with comparable attributes and returns a list of those objects. 
# The startWar() function creates a War object 
# and adds the Viking and Saxon teams to it. 
# It then enters a loop that repeatedly calls 
# the vikingAttack() and saxonAttack() methods of the War object 
# until the showStatus() method returns something other 
# than "Vikings and Saxons are still in the thick of battle." 
# Finally, the showStatus() method is called 
# one last time and its result is printed.
