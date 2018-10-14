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


class BurnBurnBurn(BasicFeat):

    super().__init__("Burn! Burn! Burn! Torches and alchemical fire give +1d4 damage. Avoiding burning or checks to extinguish yourself give +4", dmg=[1, 4], skill="reflex", skill_bon=4)


class CarefulSneak(BasicFeat):

    super().__init__("Careful Sneak. No armor penalties on stealth checks.", pre=["stealth", 10])


class CarefulSpeaker(BasicFeat):

    super().__init__("Careful Speaker. You speak so well, you can bluff more easily +2 on bluff.", skill="bluff", skill_bon=2, pre=["wisdom", 13])


class ImprovedChannel(BasicFeat):

    super().__init__("Improved Channel. Bonus when channeling positive energy, +2 to dmg/heal.", dmg=2, pre=["paladin", 1])


class Childlike(BasicFeat):

    super().__init__("Childlike. You are better able to disguise yourself as a child, +2 on disguise checks to look like a kid. Fuckin weirdo if you use this, though.", skill="disguise", skill_bon=2)


class CommandAnimals(BasicFeat):

    super().__init__("Command Animals. You can attempt to control animals by suggestion.", pre=["handle animal", 15])


class CommandPlants(BasicFeat):

    super().__init__("Command Plants. You can control plants.", pre=[["druid", 3], ["nature", 15]])


class Confabulist(BasicFeat):

    super().__init__("Confabulist. Hey, if you fail a bluff check and have this feat, you can bluff again for a -5 penalty!", skill="bluff", skill_bon=-5, pre=[["bluff", 8], ["charisma", 14]])


class Conviction(BasicFeat):

    super().__init__("Conviction. Your conviction empowers your channeling, +2 to dmg/heal when channeling positive energy.", dmg=2, pre=["paladin", 5])


class Cosmopolitan(BasicFeat):

    super().__init__("Cosmopolitan. Read and speak two additional languges.")


class CriminalReputation(BasicFeat):

    super().__init__("Criminal Reputation. You're evil, you play well with criminals and gain bonuses when interacting with them.", skill=["bluff", "intimidate", "sense motive"], pre=["evil", 6])


class CuttingHumiliation(BasicFeat):

    super().__init__("Cutting Humiliation. Sticks and stones and all that business, +3 on intimidation checks.", skill="intimidate", skill_bon=3)


class CypherMagic(BasicFeat):

    super().__init__("Cypher Magic. Add 1/4 your caster level to spells from scrolls.", pre=["CL", 4])


class DeadlyDealer(BasicFeat):

    super().__init__("Deadly Dealer. You're fucking Gambit, bro. You throw cards with deadly accuracy.", pre=[["dexterity", 15], ["neutral", "chaotic"]])


class Deceitful(BasicFeat):

    super().__init__("Deceitful. You're not...a great guy. +2 on bluff and disguise checks.", skill=["bluff", "disguise"], skill_bon=2, pre=[["bluff", 5], ["disguise", 5]])


class DeepDiver(BasicFeat):

    super().__init__("Deep Diver. You're a fish! You can swim down deep and hold you breath for a long time.", pre=[["constitution", 16], ["swim", 12]])


class DeepDrinker(BasicFeat):

    super().__init__("Deep Drinker. You can take a lot of drinks before you get drunk.", pre=["constitution", 17])


class DeftHands(BasicFeat):

    super().__init__("Deft Hands. You're good with your hands *wink* *wink*. No but actually, +2 to Disable Device and Sleight of Hand checks", skill=["disable device", "sleight of hand"], skill_bon=2, pre=[["disable device", 5], ["sleight of hand", 5]])


class DisableDweomer(BasicFeat):

    super().__init__("Disable Dweomer. You can disable magical devices, just like the Dweomer could, whoever they were.", pre=["disable device", 15])


class Dislocate(BasicFeat):

    super().__init__("Dislocate. You can take 1d8 damage to pop your joint out of socket.", pre=[["dexterity", 14], ["constitution", 14]])

    dmg_taken = [1, 8]


class DivineProtection(BasicFeat):

    super().__init__("Divine Protection. Gain a bonus equal to your charisma bonus to saving throws. Pretty cool!", att="charisma", pre=[["charisma", 15], ["religion", 10]])


class EagleEyed(BasicFeat):

    super().__init__("Eagle Eyed. Your eyes work real good. +3 on perception checks.", skill="perception", skill_bon=3, pre=[["perception", 10], ["druid", 3]])


class Empath(BasicFeat):

    super().__init__("Empath. You can read a person like a book, know their emotions instinctively, it's like anti-autism.", pre=[["sense motive", 10], ["perception", 5]])


class EnergyChannel(BasicFeat):

    super().__init__("Energy Channel. Channel your divine energy into a weapon dealing extra damage.", pre=["paladin", 5])


class ExpandedPreparation(BasicFeat):

    super().__init__("Expanded Preparation. You're basically a magic nerd, you spent a lot of time studying and because of that gain extra spell slots.", pre=[["sorcerer", 3], ["druid", 3]])


class ExperiencedVagabond(BasicFeat):

    super().__init__("Experienced Vagabond. You're scum, but you're really good at being scum. You gain bonuses when interacting with criminals and lowlifes. +5 to bluff and intimidate.", skill=["bluff", "intimidate"], skill_bon=5, pre_feat="criminal reputation", pre=["evil", 8])













