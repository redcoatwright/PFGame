def move(self, noun):
    if not noun:
        print("Move where?")
    elif noun == 'north':
        self._move_north()
    elif noun == 'south':
        self._move_south()
    elif noun == 'east':
        self._move_east()
    elif noun == 'west':
        self._move_west()
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


def _move_north(self):
    self._move_self(-1, 0)


def _move_south(self):
    self._move_self(1, 0)


def _move_east(self):
    self._move_self(0, 1)


def _move_west(self):
    self._move_self(0, -1)


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

