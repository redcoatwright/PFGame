import mechanics.diceRolling

mechs = mechanics.diceRolling

def move(new_pc, noun):
    if not noun:
        print("Move where?")
    elif noun == 'north':
        _move_north()
    elif noun == 'south':
        _move_south()
    elif noun == 'east':
        _move_east()
    elif noun == 'west':
        _move_west()
    else:
        print("I don't understand that direction. Try again.")

    print("You are currently at: ", new_pc.pos_x, new_pc.pos_y)
    print(new_pc.current_level.level[new_pc.pos_x][new_pc.pos_y].intro_text)


def fight(new_pc, noun):
    did_fight = False
    for enemy in new_pc.current_level.level[new_pc.pos_x][new_pc.pos_y].enemies:
        if enemy.cmdName == noun:
            print("You fight the %s. Good work." % noun)
            did_fight = True
            break
    if not did_fight:
        print("There's no %s here to fight." % noun)


def _move_self(new_pc, dx, dy):
    new_x = new_pc.pos_x + dx
    new_y = new_pc.pos_y + dy

    if new_pc.current_level.is_valid_area(new_x, new_y):
        new_pc.pos_x = new_x
        new_pc.pos_y = new_y
    else:
        new_pc.current_level.print_invalid_area()


def _move_north(new_pc):
    _move_self(new_pc, -1, 0)


def _move_south(new_pc):
    _move_self(new_pc, 1, 0)


def _move_east(new_pc):
    _move_self(new_pc, 0, 1)


def _move_west(new_pc):
    _move_self(new_pc, 0, -1)


def equipItem(new_pc, item):
    new_pc.equItem = item


def add_to_inv(new_pc, item):
    new_pc.inventory.append(item)


def add_xp(new_pc, amt):
    new_pc.current_xp += amt


def sub_hp(new_pc, amt):
    new_pc.c_hp -= amt


def add_hp(new_pc, amt):
    new_pc.c_hp += amt


def add_tot_hp(new_pc, amt):
    new_pc.t_hp += amt


def add_ac(new_pc, amt):
    new_pc.ac += amt


def mel_atk(new_pc, amt):
    new_pc.melee_attk += amt


def add_init(new_pc, amt):
    new_pc.init += amt


def change_name(new_pc, name):
    new_pc.char_name = name

def rand_ab_score():
    rolls = []

    for i in range(6):
        rolls.append(mechs.roll_d6())

    rolls.sort(reverse=True)

    total = 0

    for i in range(4):
        total += rolls[i]

    return total

