import weaponList

class newPC():

    char_name = "Defaulty McDefaultNameplate"
    current_xp = 0
    t_hp = 10
    c_hp = 10 #current hp
    ac = 10
    init = 0
    melee_attk = 0
    inventory = []

    equItem = weaponList.Fists()

    def equipItem(self, item):
        equItem = item

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
    
