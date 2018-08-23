import itemList
import natMonsters

class Area:
    items = []
    enemies = []
    intro_text = "An area"

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Map:
    def __init__(self, x, y):
        self.size_x = x
        self.size_y = y        
        self.level = [[Area(i,j) for i in range(self.size_y)] for j in range(self.size_x)]

    def is_valid_area(self, x, y):
        if 0 <= x < self.size_x and 0 <= y < self.size_y:
            return True
        else:
            return False

    def print_invalid_area(self):
        raise NotImplementedError()

class Cavern(Map):
    def __init__(self):
        super().__init__(5, 5)
    
        rat = natMonsters.Rat()
        shirt = itemList.BasicShirt()
        self.level[1][1].enemies = [rat]
        self.level[1][1].intro_text = "Ah! A rat!"
        self.level[2][3].items = [shirt]

    def print_invalid_area(self):
        print ("You can't go that way. A stone wall blocks your way.")
