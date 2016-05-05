import random
creatureHealth=(random.randint(1,100))
print("You found a creature with {} Health".format(creatureHealth))
while creatureHealth > 0:
    attackDice_1=(random.randint(1,20))
    attackDice_2=(random.randint(1,20))
    attackDiceTotal = attackDice_1 + attackDice_1
    print("The creature gets hit for {} Hitpoints".format(attackDiceTotal))
    damage_1= creatureHealth - attackDiceTotal
    print("The creature is down to {} Health".format(damage_1))
    creatureHealth = damage_1
else:
    print("You killed it!")
