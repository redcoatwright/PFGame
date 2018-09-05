class feature:

    def __init__(self, desc, trav, rough=None, open=None, lock=None, search=None, contain=None, breakable=None):

        self.desc = desc #description of the feature in question
        self.trav = trav #a flag which decides if a feature is traversable
        self.rough = rough #a flag which decides if the terrain is rough
        self.open = open #a flag which decides if the feature is openable
        self.lock = lock #a flag which decides if the feature is locked
        self.search = search #a flag which decides if the feature is searchable
        self.contain = contain #variable to hold what the object contains (if it can)
        self.breakable = breakable #a flag which decides if the feature can be smashed


class Column(feature):

    def __init__(self):
        super().__init__("A rough stone column rises from the floor to the ceiling", False)


class SmallRocks(feature):

    def __init__(self):
        super().__init__("Some small rocks cover the ground, you step over them easily however", True, False)


class LargeRocks(feature):

    def __init__(self):
        super().__init__("Large rocks cover the ground here making the terrain difficult to traverse",True,True)


class LoWoodDoor(feature):

    def __init__(self):
        super().__init__("A wooden door bars your way, you try the handle but it doesn't turn", False, False, True)


class OpWoodDoor(feature):

    def __init__(self):
        super().__init__("A wooden door bars your way, you try the handle and it turns easily in your hand", False, False, False)


class Candles(feature):

    def __init__(self):
        super().__init__("A pool of flickering light surrounds three candles sitting on the floor", True)


class BrokenBarrel(feature):

    def __init__(self):
        super().__init__("A smashed barrel lies on the ground, the contents of which spilled out onto the floor", True, search=True)

class Barrel(feature):

    def __init__(self):
        super().__init__("A large barrel blocks your way", False, breakable=True)


class Wall(feature):

    def __init__(self):
        super().__init__("You come up to a wall, blocking your path", False)


class ArmorRack(feature):

    def __init__(self):
        super().__init__("An armor rack stands here, maybe it holds something good", True, search=True)


class Stalagmite(feature):

    def __init__(self):
        super().__init__("A small rock mound rises from the ground, making it hard to walk through", True, True)


class OrnateChest(feature):

    def __init__(self):
        super().__init__("A large chest emblazoned with gold and embedded gem stones stands before you, a large keyhole lies on the front", True, search=True, lock=True, breakable=True)


class LargeChest(feature):

    def __init__(self):
        super().__init__("A large wooden chest banded with steel stands before you, a large keyhole lies on the front", True, search=True, lock=True, breakable=True)


