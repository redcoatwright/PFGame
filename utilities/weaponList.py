class Weapon:

    def __init__(self, dmg_die, dmg_mult, crit, value, desc, hit, miss):
        self.die = dmg_die
        self.mult = dmg_mult
        self.crit = crit
        self.val = value
        self.desc = desc
        self.hit = hit
        self.miss = miss
        
"""
When generating a new weapon, fill in the 4 numbers under the constructor with the values of
the weapon as follows, number of sides of die, number of dice, crit multiplier and value of the
weapon in GP
"""

class Fists(Weapon):

    def __init__(self):
        super().__init__(3, 1, 2, 0, "You cock a fist back and swing forward at them...", "and the punch lands solidly!\n", "and your punch missed! You suck at this! *points at you* Hahahahaha... \n")

class Rock(Weapon):

    def __init__(self):
        super().__init__(4, 1, 1.5, 0, "You raise the rock up and bring it down on the enemy...", "and the rock smashes against them!\n", "and the strike misses entirely, shame!\n")

class Dagger(Weapon):

    def __init__(self):
        super().__init__(4, 1, 2, 2, "You lunge forward brandishing the dagger...", "and the dagger tears a hole in your opponent! They're bleeding so much!\n", "and the dagger strike misses! Damn!\n")

class LightMace(Weapon):

    def __init__(self):
        super().__init__(6, 1, 2, 5, "You whip the mace through the air at their head...", "and it connects solidly on their head, they stagger under the force!\n","and the mace misses the head by a hair, the enemy blinks at the near miss!\n")

class Club(Weapon):

    def __init__(self):
        super().__init__(6, 1, 2, 0, "You heavily swing the club at them...", "and it lands solidly on the enemy!\n", "and it misses entirely, why are you even using a club. Clubs suuccckkk! The music is always so loud.\n")

