class natMonster:

    def __init__(self, maxHealth, curHealth, armor, dmgDie, dmgMult, crit, init, melee_attk):
        self.t_hp = maxHealth #max health
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
    def __init__(Self):
        super().__init__(6, 6, 12, 3, 1, 2, 2, 1)
