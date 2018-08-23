class natMonster:

    def __init__(self, cmdName, dispName, maxHealth, curHealth, armor, dmgDie, dmgMult, crit):
        self.cmdName = cmdName #name provided by player
        self.dispName = dispName #display name of the monster
        self.max_health = maxHealth #max health
        self.current_health = curHealth #current health
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
        super().__init__('rat', 'Rat', 6, 6, 15, 3, 1, 2)
