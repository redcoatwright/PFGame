import world
import natMonsters
import weaponList
import caveFeatures
import ItemList

class Cavern(world.Map):

    def __init__(self):
        super().__init__(2, 5)

        rat = natMonsters.Rat()
        rock = weaponList.Rock()

        column = caveFeatures.Column()

        self.level[1, 4] = rat
        self.level[1, 1] = rock
        self.level[0, 0] = ItemList.BasicShirt()

        self.level[0, 5] = column
        self.level[2, 5] = column

