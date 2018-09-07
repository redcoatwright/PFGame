import mechanics.diceRolling
import time
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

def choose_class(new_pc):

    print("Hey, it's now time for you to choose a class! Woo hoo, that's so fun /n")
    print("Here are the options:/n")
    print("Fighter")
    print("Paladin")
    print("Druid")
    print("Sorcerer")
    print("Ranger")
    print("Rogue/n")

    user_choice = input("Type 'help class_name' for more information or /n'choose class_name' to choose a class/n >>> ")

    user_choice.lower().split(" ")

    if user_choice[0] == "help":

        if user_choice[1] == "fighter":

            print("Okay, so you want to be a FIGHTER./nFighters are all around badasses, they use weapons to slice, stab or generally physically destroy their opponents.")
            print("The name of the game for you is to use your strength and your dexterity to win any fight./n")
            print("Your preferred ability traits are: Strength, Intelligence, Charisma, Dexterity and a bit of Wisdom.")
            print("But let us be honest here, fighting requires strength, you won't win any fights as a weakling./n")
            print("Here are your class skills: /nClimb, Craft, Handle Animal, Intimidate, Knowledge (Dungeoneering), Knowledge (Engineering), Ride, Survival and Swim")
            print("The first point you put into each class skill counts as 4 points (wow, that's CRAZY)!")
            print("Also, each level you get 2 + your intelligence modifier worth of skill points to assign.")

        elif user_choice[1] == "paladin":

            print("Okay, so you want to be a PALADIN. /nPaladins are like that guy you know who always does the right thing no matter what./n")
            print("They're a little annoying but they're also powerful, especially against anything evil./nThey are empowered with their beliefs to destroy evil./n")
            print("Your preferred ability traits are: Intelligence, Charisma, Wisdom and Dexterity.")
            print("A lot of your abilities are based on charisma./n")
            print("Here are your class skills: /nCraft, Diplomacy, Handle Animal, Heal, Knowledge (Nobility), Knowledge (Religion), Ride, Sense Motive and Spellcraft.")
            print("The first point you put into each class skill counts as 4 points (wow, that's CRAZY)!")
            print("Also, each level you get 2 + your intelligence modifier worth of skill points to assign.")

        elif user_choice[1] == "druid":

            print("Okay, so you want to be a DRUID. /nDruids are hippies. End of story./n")
            time.sleep(2)
            print(".")
            time.sleep(1)
            print("..")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("....")
            time.sleep(1)
            print("...../n")
            time.sleep(2)
            print("Fine, fine. Druids ARE hippies, though, I stand by that statement.")
            print("They also can be useful. They work with nature to solve their problems and defeat their enemies.")
            print("They can even heal themselves or others and cast spells. I mean, I guess they're cool.")
            print("Oh, also they get an animal companion. It will follow you everywhere and fight right after you do./n")
            print("Your preferred ability traits are: Strength, Intelligence, Dexterity, Charisma and Wisdom.")
            print("A high wisdom is useful for Druids./n")
            print("Here are your class skills: /nClimb, Craft, Fly, Handle Animal, Heal, Knowledge (Geography), Knowledge (Nature), Perception, Ride, Spellcraft, Survival and Swim.")
            print("The first point you put into each class skill counts as 4 points (wow, that's CRAZY)!")
            print("Also, each level you get 4 + your intelligence modifier worth of skill points to assign.")

        elif user_choice[1] == "sorcerer":

            print("Okay, so you want to be a SORCERER. /nVery cool, I feel like I don't have to explain this one much.")
            print("I can't, for you know copyright reasons, say exactly what I'm thinking but imagine a certain wizard from a famous book series. /nRhymes with...band...alf?")
            print("Okay, enough fooling around. You cast spells, you're a bad ass magic user, fireballs, lightning, magic armor, really cool shit.")
            print("What else do I need to say? Oh wait, you also get a blood line power! Holy Shit!!/n")
            print("Your preferred ability traits are: Intelligence, Charisma, Dexterity and a touch of Wisdom")
            print("You get extra spells for a high intelligence!/n")
            print("Here are your class skills: /nAppraise, Bluff, Craft, Fly, Intimidate, Knowledge (Arcana), Spellcraft and Use Magic Device.")
            print("The first point you put into each class skill counts as 4 points (wow, that's CRAZY)!/n")
            print("Oh, also you can summon monsters. Like how cool is that.")
            print("Also, each level you get 2 + your intelligence modifier worth of skill points to assign.")

        elif user_choice[1] == "ranger":

            print("Okay, so you want to be a RANGER. /nShooting arrows REALLY well, like eventually you can shoot multiple arrows at once.")
            print("Probably wearing green and having a band of merry men, I mean what do I know, I'm a program. Still seems cool.")
            print("Or maybe you have a dwarven best friend...?/n")
            print("Your preferred ability traits are: Strength, Intelligence, Charisma, Wisdom and Dexterity.")
            print("Dexterity helps you shoot better, Strength makes your arrows hit harder./n")
            print("Here are your class skills: /nClimb, Craft, Handle Animal, Heal, Intimidate, Knowledge (Dungeoneering), Knowledge (Geography), Knowledge (Nature), Perception, Ride, Spellcraft, Stealth, Survival and Swim.")
            print("Damn, that's a lot of class skills.")
            print("The first point you put into each class skill counts as 4 points (wow, that's CRAZY)!")
            print("Also, each level you get 6 + your intelligence modifier worth of skill points to assign.")

        elif user_choice[1] == "rogue":

            print("Okay, so you want to be a ROGUE. /nRogues are kind of a wild card in my book. They're stealthy, tricksy, tons of skills, did I mention tricksy?")
            print("I usually imagine a cross between an assassin and a bard. They can sneak up behind, stab you in the back but do it with a song in their heart.")
            print("I don't know, Rogues are rogues. Maybe like Han Solo? Or Lara Croft?/n")
            print("Your preferred ability traits are: Dexterity, Intelligence, Charisma, Strength and Wisdom.")
            print("Dexterity is your key, though, helps with being stealthy./n")
            print("Here are your class skills: /nAcrobatics, Appraise, Bluff, Climb, Craft, Diplomacy, Disable Device, Disguise, Escape Artist, Intimidate, Knowledge (Dungeoneering), Knowledge (Local), Linguistics, Perception, Perform, Sense Motive, Sleight of Hand, Stealth, Swim and Use Magic Device")
            print("Wow, and I thought rangers had a lot class skills, holy Moses./n")
            print("The first point you put into each class skill counts as 4 points (wow, that's CRAZY)!")
            print("Also, each level you get 8 + your intelligence modifier worth of skill points to assign. That's so much, so so much.")

        print("/n /n In case you weren't aware (maybe you're new to pathfinder), skills will allow you to resolve situations in the game in different ways.")
        print("For instance, if you're trying to get information from someone, you can try to intimidate them or use diplomacy.")
        print("Need to cross a broken bridge? Maybe you can jump over using your acrobatics skill.")
        print("Point being, don't underestimate your skills! Oh also, you can put points into non class skills, FYI.")

    elif user_choice[0] == "choose":

        if user_choice[1] == "fighter":
            None

