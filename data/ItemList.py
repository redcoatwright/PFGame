class Item:
    
    def __init__(self, desc, value, name):
        self.item_desc = desc
        self.item_val = value
        self.item_name = name

class FlinTin(Item):
    def __init__(self):
        super().__init__("This is a flint and tinder box capable of making a small fire or lighting a much larger conflagration, very handy indeed.", 2, "Flint and Tinder")

class BasicShirt(Item):
    def __init__(self):
        super().__init__("This is a very basic shirt, you were wearing it when you woke up in the cave, it's pretty tattered at the moment.", 0, "Basic Shirt")

class BasicPants(Item):
    def __init__(self):
        super().__init__("These are very basic pants, you were wearing them when you woke up in the cave, they're pretty tattered at the moment.", 0, "Basic Pants")

class BasicBoots(Item):
    def __init__(self):
        super().__init__("These are very basic boots, you were wearing them when you woke up in the cave, they're pretty tattered at the moment.", 0, "Basic Boots")

