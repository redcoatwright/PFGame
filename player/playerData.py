import data.weaponList
import player.playerMechs


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
