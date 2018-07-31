class natMonster:

    def __init__(self, maxHealth, curHealth, armor, dmgDie, dmgMult, crit):
        self.max_health = maxHealth #max health
        self.current_health = curHealth #current health
        self.ac = armor #armor class
        self.dmg_die = dmgDie #the dice that's rolled for dmg
        self.dmg_mult = dmgMult #the number of dice rolled
        self.crit_hit = crit #the multipler applied for a critical hit


class Rat(natMonster):
    def __init__(Self):
        super().__init__(6, 6, 15, 3, 1, 2)
