import diceRolling

def melee_attack(attk_mod):
    return diceRolling.roll_d20 + attk_mod

def ranged_attack(attk_mod):
    return diceRolling.roll_d20 + attk_mod

