class BasicFeat():

    def __init__(self, desc, att=None, att_bon=None, skill=None, skill_bon=None, atk=None, dmg=None):

        self.desc = desc
        self.att = att
        self.att_bon = att_bon
        self.skill = skill
        self.skill_bon = skill_bon
        self.atk = atk
        self.dmg = dmg


class AccomplishedSneakAttacker(BasicFeat):

    super().__init__("Accomplished Sneak Attacker. You sneak attack real good, plus 1d6 to damage from sneak attack", dmg=[1, 6])


class Acrobatic(BasicFeat):

    super().__init__("Acrobatics. You're really acrobatic, +2 to acrobatics and flying!", att=["acrobatics", "fly"], att_bon=2)
    

class Alertness(BasicFeat):

    super().__init__("Alertness. You've drank tons of coffee and now you're so alert, nothing sneaks up on you.", att=["perception", "sense motive"], att_bon=2)


class AltitudeAffinity(BasicFeat):

    super().__init__("Altitude Affinity. No fear of heights for you! Better survival in heights.", att="survival", att_bon=4)



