class natMonster:

    def __init__(self, cmdName, dispName, maxHealth, curHealth, armor, dmgDie, dmgMult, crit, init, melee_attk):
        self.cmdName = cmdName #name provided by player
        self.dispName = dispName #display name of the monster
        self.t_hp = maxHealth #total health
        self.c_hp = curHealth #current health
        self.ac = armor #armor class
        self.dmg_die = dmgDie #the dice that's rolled for dmg
        self.dmg_mult = dmgMult #the number of dice rolled
        self.crit_hit = crit #the multipler applied for a critical hit
        self.init = init #the init of the rat
        self.melee_attk = melee_attk #melee attack bonus for the creature


    def sub_hp(self, amt):
        self.c_hp -= amt


class Rat(natMonster):
    def __init__(self):
        super().__init__('rat', 'Rat', 6, 6, 15, 3, 1, 2, 1, 1)
