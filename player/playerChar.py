import data.weaponList

class newPC():

    char_name = "Defaulty McDefaultNameplate"
    current_xp = 0
    t_hp = 10
    c_hp = 10 #current hp
    ac = 10
    init = 0
    melee_attk = 0

    pos_x = 0
    pos_y = 0

    einventory = []
    inventory = []

    equItem = data.weaponList.Fists()

    def __init__(self, current_level):
        self.current_level = current_level

    def set_level(self, current_level):
        self.current_level = current_level

    def move(self, noun):
        if not noun:
            print("Move where?")
        elif noun == 'north':
            self.move_north()
        elif noun == 'south':
            self.move_south()
        elif noun == 'east':
            self.move_east()
        elif noun == 'west':
            self.move_west()
        else:
            print("I don't understand that direction. Try again.")

        print("You are currently at: ", self.pos_x, self.pos_y)
        print(self.current_level.level[self.pos_x][self.pos_y].intro_text)

    def fight(self, noun):
        didFight = False
        for enemy in self.current_level.level[self.pos_x][self.pos_y].enemies:
            if enemy.cmdName == noun:
                print("You fight the %s. Good work." % noun)
                didFight = True
                break
        if not didFight:
            print("There's no %s here to fight." % noun)

    def _move_self(self, dx, dy):
        newX = self.pos_x + dx
        newY = self.pos_y + dy

        if self.current_level.is_valid_area(newX, newY):
            self.pos_x = newX
            self.pos_y = newY
        else:
            self.current_level.print_invalid_area()

    def move_north(self):
        self._move_self(0, 1)

    def move_south(self):
        self._move_self(0, -1)

    def move_east(self):
        self._move_self(1, 0)

    def move_west(self):
        self._move_self(-1, 0)

    def equipItem(self, item):
        newPC.equItem = item

    def add_to_inv(self, item):
        newPC.inventory.append(item)

    def add_xp(self, amt):
        newPC.current_xp += amt

    def sub_hp(self, amt):
        newPC.c_hp -= amt

    def add_hp(self, amt):
        newPC.c_hp += amt

    def add_tot_hp(self, amt):
        newPC.t_hp += amt

    def add_ac(self, amt):
        newPC.ac += amt

    def mel_atk(self, amt):
        newPC.melee_attk += amt

    def add_init(self, amt):
        newPC.init += amt

    def change_name(self, name):
        newPC.char_name = name
    
    def search_ground(self, level):
        if not level[self.pos_x][self.pos_y].items:
            print("You do not find anything on the ground!")
        else:
            print("You find something! Yay!")
            print("You've found...")


            count = 0
            for x in level[self.pos_x][self.pos_y].items:
                print("- " + x.name + "\n")

                print()
                print("Do you wish to take this item? \n")

                user_input = input("\n >>> ").lower().split(" ")

                if user_input == "yes" or user_input == "y" or user_input == "yeah" or user_input == "yea" or user_input == "yeet ma geet":
                    self.inventory.append(level[self.pos_x][self.pos_y].items.pop(count))
                    print("You took the " + x.name + "\n")
                    
                elif user_input == "no" or user_input == "n" or user_input == "nope" or user_input == "get fucked you loser":
                    print("You did not take the " + x.name + "\n")
                    

    def take_item(self, item):
        self.inventory.append(item)
        ## unused right now 1/14/2020