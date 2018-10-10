class BasicFeat():

    def __init__(self, desc, att=None, att_bon=None, skill=None, skill_bon=None, atk=None, dmg=None, pre=None, pre_feat=None):

        self.desc = desc  # a description of the feat
        self.att = att  # what attribute gets a bonus
        self.att_bon = att_bon  # how much attribute bonus
        self.skill = skill  # what skill gets a bonus
        self.skill_bon = skill_bon  # how much skill bonus granted by feat
        self.atk = atk  # attack bonus granted in format of a list w/ [#dice, dice#] so for 1d6 it's [1,6]
        self.dmg = dmg  # damange bonus, formatted the same as the atk bonus
        self.pre = pre  # general prereqs like skills and attributes necessary to take feat, takes format of a list of lists
        self.pre_feat = pre_feat  # if there is a feat prereq then specify it here


class AccomplishedSneakAttacker(BasicFeat):

    super().__init__("Accomplished Sneak Attacker. You sneak attack real good, plus 1d6 to damage from sneak attack", dmg=[1, 6], pre=["rogue", 1])


class Acrobatic(BasicFeat):

    super().__init__("Acrobatics. You're really acrobatic, +2 to acrobatics and flying!", skill=["acrobatics", "fly"], skill_bon=2)


class Alertness(BasicFeat):

    super().__init__("Alertness. You've drank tons of coffee and now you're so alert, nothing sneaks up on you.", skill=["perception", "sense motive"], skill_bon=2)


class AltitudeAffinity(BasicFeat):

    super().__init__("Altitude Affinity. No fear of heights for you! Better survival in heights.", skill="survival", skill_bon=4)


class AnimalAffinity(BasicFeat):

    super().__init__("Animal Affinity. You reaallly like animals, but not in a weird way, don't worry.", skill=["handle animal", "ride"], skill_bon=2)


class AnimalAlly(BasicFeat):

    super().__init__("Animal Ally. You gain an animal companion, wow, that's super cool.")

    # player.gainAnimalCompanion()


class AnimalCall(BasicFeat):

    super().__init__("Animal Call. Wowee, you can make convincing animal calls as bluff checks.", pre=[["bluff", 1], ["nature", 1]])


class AnimalDisguise(BasicFeat):

    super().__init__("Animal Disguise. You can play dress up as an animal...convincingly", pre=[["disguise", 6], ["nature", 6]], pre_feat="animal call")


class Athletic(BasicFeat):

    super().__init__("Athletic. You're athletic, what more can I say. +2 on climb and swim checks", skill=["climb", "swim"], skill_bon=2)


class BelieversHands(BasicFeat):

    super().__init__("Believer's Hands. Extra use of lay on hands! Nifty.", pre=["paladin", 1])


class BigGameHunter(BasicFeat):

    super().__init__("Big Game Hunter. You +1 on attack and +2 on damage against big creatures (Large and up)", atk=1, dmg=2)


class BlightSurvivalist(BasicFeat):

    super().__init__("Blight Survivalist. You have learned to survive in dangerous environments.", pre=["survival", 10])


class BraveryInAction(BasicFeat):

    super().__init__("Bravery in Action. You are oh so brave, add your bravery bonus to initiative checks", pre=["fighter", 1])


class BreadthOfExperience(BasicFeat):

    super().__init__("Breadth of Experience. You've been many places and due to that get bonuses, +2 on knowledge checks", skill=["nature", "religion", "arcana", "dungeoneering", "nobility", "engineering", "geography", "history", "local", "planes"], skill_bon=2)












