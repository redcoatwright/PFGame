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

    # ability scores
    cha = 10
    str = 10
    wis = 10
    con = 10
    int = 10
    dex = 10

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
        self.cha = cha
        self.str = str
        self.wis = wis
        self.con = con
        self.int = int
        self.dex = dex

    def set_rand_abs(self):
        
        self.cha = mechs.rand_ab_score()
        self.str = mechs.rand_ab_score()
        self.wis = mechs.rand_ab_score()
        self.con = mechs.rand_ab_score()
        self.int = mechs.rand_ab_score()
        self.dex = mechs.rand_ab_score()

