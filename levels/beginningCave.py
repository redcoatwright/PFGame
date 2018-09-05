import world
import utilities.natMonsters
import utilities.weaponList
import utilities.caveFeatures
import utilities.ItemList

monsters = utilities.natMonsters
weapons = utilities.weaponList
cave_features = utilities.caveFeatures
items = utilities.ItemList

class Cavern(world.Map):

    def __init__(self):
        super().__init__(2, 5)

        rat = monsters.Rat()
        rock = weapons.Rock()

        column = cave_features.Column()

        self.level[1, 4] = rat
        self.level[1, 1] = rock
        self.level[0, 0] = items.BasicShirt()

        self.level[0, 5] = column
        self.level[2, 5] = column

