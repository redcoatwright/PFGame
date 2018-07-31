class Weapon:

    def __init__(self, dmg_die, dmg_mult, crit, value):
        self.wep_dmg_die = dmg_die
        self.wep_dmg_mult = dmg_mult
        self.crit_mult = crit
        self.wep_val = value

"""
When generating a new weapon, fill in the 4 numbers under the constructor with the values of
the weapon as follows, number of sides of die, number of dice, crit multiplier and value of the
weapon in GP
"""

class Rock(Weapon):

    def __init__(self):
        super().__init__(3, 1, 1.5, 0)

class Dagger(Weapon):

    def __init__(self):
        super().__init__(4, 1, 2, 2)

class LightMace(Weapon):

    def __init__(self):
        super().__init__(6, 1, 2, 5)

class Club(Weapon):

    def __init__(self):
        super().__init__(6, 1, 2, 0)

