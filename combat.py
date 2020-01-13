import mechanics.diceRolling as diceRolling

def melee_attack(attk_mod):
    return diceRolling.roll_d20() + attk_mod

def ranged_attack(attk_mod):
    return diceRolling.roll_d20() + attk_mod

def dmg(dmg_dice, dmg_add):

    if dmg_dice == 10:
        return diceRolling.roll_d10() + dmg_add
    elif dmg_dice == 8:
        return diceRolling.roll_d8() + dmg_add
    elif dmg_dice == 6:
        return diceRolling.roll_d6() + dmg_add
    elif dmg_dice == 4:
        return diceRolling.roll_d4() + dmg_add
    elif dmg_dice == 3:
        return diceRolling.roll_d3() + dmg_add

def larger_num(num1, num2):
    if num1 < num2:
        return 0
    elif num2 < num1:
        return 1
    else:
        return -1
