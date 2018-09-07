import data.weaponList
import player.playerMechs

mechs = player.playerMechs

class NewPC():

    char_name = "Defaulty McDefaultNameplate"
    current_xp = 0
    t_hp = 10
    c_hp = 10 #current hp
    ac = 10
    init = 0
    melee_attk = 0

    pc_class = None

    # ability scores dict, first # is the score, second # is a temp modifier
    ab_scores = {
        "Charisma": [10, 0],
        "Strength": [10, 0],
        "Wisdom": [10, 0],
        "Constitution": [10, 0],
        "Intelligence": [10, 0],
        "Dexterity": [10, 0]
    }


    # skills, dictionary key: skill name, value: list containing skill level and if it's a class skill
    skills = {
        "Acrobatics": [0, False],
        "Appraise": [0, False],
        "Bluff": [0, False],
        "Climb": [0, False],
        "Craft": [0, False],
        "Diplomacy": [0, False],
        "Disable Device": [0, False],
        "Disguise": [0, False],
        "Escape Artist": [0, False],
        "Fly": [0, False],
        "Handle Animal": [0, False],
        "Heal": [0, False],
        "Intimidate": [0, False],
        "Knowledge (Arcana)": [0, False],
        "Knowledge (Dungeoneering)": [0, False],
        "Knowledge (Engineering)": [0, False],
        "Knowledge (Geography)": [0, False],
        "Knowledge (History)": [0, False],
        "Knowledge (Local)": [0, False],
        "Knowledge (Nature)": [0, False],
        "Knowledge (Nobility)": [0, False],
        "Knowledge (Planes)": [0, False],
        "Knowledge (Religion)": [0, False],
        "Linguistics": [0, False],
        "Perception": [0, False],
        "Perform": [0, False],
        "Profession": [0, False],
        "Ride": [0, False],
        "Sense Motive": [0, False],
        "Sleight of Hand": [0, False],
        "Spellcraft": [0, False],
        "Stealth": [0, False],
        "Survival": [0, False],
        "Swim": [0, False],
        "Use Magic Device": [0, False],

    }

    # current position on the map
    pos_x = 0
    pos_y = 0

    # equippable inventory and regular inventory
    e_inventory = []
    inventory = []

    equItem = data.weaponList.Fists()

    def __init__(self, current_level):
        self.current_level = current_level


    def set_level(self, current_level):
        self.current_level = current_level

    def set_ab_scores(self, cha, str, wis, con, int, dex):
        self.ab_scores["Charisma"][0] = cha
        self.ab_scores["Strength"][0] = str
        self.ab_scores["Wisdom"][0] = wis
        self.ab_scores["Constitution"][0] = con
        self.ab_scores["Intelligence"][0] = int
        self.ab_scores["Dexterity"][0] = dex

    def set_rand_abs(self):
        self.ab_scores["Charisma"][0] = mechs.rand_ab_score()
        self.ab_scores["Strength"][0] = mechs.rand_ab_score()
        self.ab_scores["Wisdom"][0] = mechs.rand_ab_score()
        self.ab_scores["Constitution"][0] = mechs.rand_ab_score()
        self.ab_scores["Intelligence"][0] = mechs.rand_ab_score()
        self.ab_scores["Dexterity"][0] = mechs.rand_ab_score()

