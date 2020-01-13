import world
import data.natMonsters
import data.weaponList
import data.caveFeatures
import data.ItemList

monsters = data.natMonsters
weapons = data.weaponList
cave_features = data.caveFeatures
items = data.ItemList

#          4,2
# [][][][][|]
# [][#][][$][@]
# [#][][][][|]
# 0,0
#
# | = non-traversable feature
# @ = exit
# # = item
# $ = monster
class Cavern1(world.Map):

    start = (0, 1)

    def __init__(self):
        super().__init__(5, 3)

        column = cave_features.Column()

        self.level[4][1] = monsters.Rat()
        self.level[1][1] = weapons.Rock()
        self.level[0][0] = items.BasicShirt()
        self.level[0][1] = items.FlinTin()

        self.level[4][0] = column
        self.level[4][2] = column

        

