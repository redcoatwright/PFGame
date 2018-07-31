class newPC():

    char_name = "Defaulty McDefaultNameplate"
    current_xp = 0
    total_hp = 10
    current_hp = 10
    armor_class = 10
    init = 0
    melee_attk = 0
    inventory = []

    equItem = ""

    def equipItem(self, item):
        equItem = item

    def add_to_inv(self, item):
        newPC.inventory.append(item)

    def add_xp(self, amt):
        newPC.current_xp += amt

    def sub_hp(self, amt):
        newPC.current_hp -= amt

    def add_hp(self, amt):
        newPC.current_hp += amt

    def add_tot_hp(self, amt):
        newPC.total_hp += amt

    def add_ac(self, amt):
        newPC.armor_class += amt

    def mel_atk(self, amt):
        newPC.melee_attk += amt

    def add_init(self, amt):
        newPC.init += amt

    def change_name(self, name):
        newPC.char_name = name
    
