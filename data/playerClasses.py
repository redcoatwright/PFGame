class GameClasses:

    def __init__(self, skills, skills_rank, alignment, advance):

        self.skills = skills
        self. skills_rank = skills_rank
        self.alignment = alignment
        self.advance = advance




class Fighter(GameClasses):

    def __init__(self):

        # list of class skills
        f_skills = [

            "Climb",
            "Craft",
            "Handle Animal",
            "Intimidate",
            "Knowledge (Dungeoneering)",
            "Knowledge (Engineering)",
            "Ride",
            "Survival",
            "Swim"
        ]

        # BAB, Fort Save, Ref Save, Will Save
        # BAB can be split, multiple BABs mean multiple attacks
        f_advance = [

            [1, 2, 0, 0],  # lvl 1
            [2, 3, 0, 0],  # lvl 2
            [3, 3, 1, 1],  # lvl 3
            [4, 4, 1, 1],  # lvl 4
            [5, 4, 1, 1],  # lvl 5
            [[6, 1], 5, 2, 2],  # lvl 6
            [[7, 2], 5, 2, 2],  # lvl 7
            [[8, 3], 6, 2, 2],  # lvl 8
            [[9, 4], 6, 3, 3],  # lvl 9
            [[10, 5], 7, 3, 3],  # lvl 10
            [[11, 6, 1], 7, 3, 3],  # lvl 11
            [[12, 7, 2], 8, 4, 4],  # lvl 12
            [[13, 8, 3], 8, 4, 4],  # lvl 13
            [[14, 9, 4], 9, 4, 4],  # lvl 14
            [[15, 10, 5], 9, 5, 5],  # lvl 15
            [[16, 11, 6, 1], 10, 5, 5],  # lvl 16
            [[17, 12, 7, 2], 10, 5, 5],  # lvl 17
            [[18, 13, 8, 3], 11, 6, 6],  # lvl 18
            [[19, 14, 9, 4], 11, 6, 6],  # lvl 19
            [[20, 15, 10, 5], 12, 6, 6],  # lvl 20

        ]

        super().__init__(f_skills, 2, "any", f_advance)



class Paladin(GameClasses):

    def __init__(self):

        # list of class skills
        p_skills = [

            "Craft",
            "Diplomacy",
            "Handle Animal",
            "Heal",
            "Knowledge (Nobility)",
            "Knowledge (Religion)",
            "Ride",
            "Sense Motive",
            "Spellcraft"

        ]

        # BAB, Fort Save, Ref Save, Will Save
        # BAB can be split, multiple BABs mean multiple attacks
        p_advance = [

            [1, 2, 0, 2],  # lvl 1
            [2, 3, 0, 3],  # lvl 2
            [3, 3, 1, 3],  # lvl 3
            [4, 4, 1, 4],  # lvl 4
            [5, 4, 1, 4],  # lvl 5
            [[6, 1], 5, 2, 5],  # lvl 6
            [[7, 2], 5, 2, 5],  # lvl 7
            [[8, 3], 6, 2, 6],  # lvl 8
            [[9, 4], 6, 3, 6],  # lvl 9
            [[10, 5], 7, 3, 7],  # lvl 10
            [[11, 6, 1], 7, 3, 7],  # lvl 11
            [[12, 7, 2], 8, 4, 8],  # lvl 12
            [[13, 8, 3], 8, 4, 8],  # lvl 13
            [[14, 9, 4], 9, 4, 9],  # lvl 14
            [[15, 10, 5], 9, 5, 9],  # lvl 15
            [[16, 11, 6, 1], 10, 5, 10],  # lvl 16
            [[17, 12, 7, 2], 10, 5, 10],  # lvl 17
            [[18, 13, 8, 3], 11, 6, 11],  # lvl 18
            [[19, 14, 9, 4], 11, 6, 11],  # lvl 19
            [[20, 15, 10, 5], 12, 6, 12],  # lvl 20

        ]

        super().__init__(p_skills, 2, "LawfulGood", p_advance)


class Druid(GameClasses):

    def __init__(self):

        # list of class skills
        d_skills = [

            "Climb",
            "Craft",
            "Fly",
            "Handle Animal",
            "Heal",
            "Knowledge (Geography)",
            "Knowledge (Nature)",
            "Perception",
            "Ride",
            "Spellcraft",
            "Survival",
            "Swim"

        ]

        # BAB, Fort Save, Ref Save, Will Save
        # BAB can be split, multiple BABs mean multiple attacks
        d_advance = [

            [0, 2, 0, 2],  # lvl 1
            [1, 3, 0, 3],  # lvl 2
            [2, 3, 1, 3],  # lvl 3
            [3, 4, 1, 4],  # lvl 4
            [3, 4, 1, 4],  # lvl 5
            [4, 5, 2, 5],  # lvl 6
            [5, 5, 2, 5],  # lvl 7
            [[6, 1], 6, 2, 6],  # lvl 8
            [[6, 1], 6, 3, 6],  # lvl 9
            [[7, 2], 7, 3, 7],  # lvl 10
            [[8, 3], 7, 3, 7],  # lvl 11
            [[9, 4], 8, 4, 8],  # lvl 12
            [[9, 4], 8, 4, 8],  # lvl 13
            [[10, 5], 9, 4, 9],  # lvl 14
            [[11, 6, 1], 9, 5, 9],  # lvl 15
            [[12, 7, 2], 10, 5, 10],  # lvl 16
            [[12, 7, 2], 10, 5, 10],  # lvl 17
            [[13, 8, 3], 11, 6, 11],  # lvl 18
            [[14, 9, 4], 11, 6, 11],  # lvl 19
            [[15, 10, 5], 12, 6, 12],  # lvl 20

        ]

        super().__init__(d_skills, 4, "AnyNeutral", d_advance)


class Sorcerer(GameClasses):

    def __init__(self):

        # list of class skills
        s_skills = [

            "Appraise",
            "Bluff",
            "Craft",
            "Fly",
            "Intimidate",
            "Knowledge (Arcana)",
            "Spellcraft",
            "Use Magic Device"

        ]

        # BAB, Fort Save, Ref Save, Will Save
        # BAB can be split, multiple BABs mean multiple attacks
        s_advance = [

            [0, 2, 0, 2],  # lvl 1
            [1, 3, 0, 3],  # lvl 2
            [1, 3, 1, 3],  # lvl 3
            [2, 4, 1, 4],  # lvl 4
            [2, 4, 1, 4],  # lvl 5
            [3, 5, 2, 5],  # lvl 6
            [3, 5, 2, 5],  # lvl 7
            [4, 6, 2, 6],  # lvl 8
            [4, 6, 3, 6],  # lvl 9
            [5, 7, 3, 7],  # lvl 10
            [5, 7, 3, 7],  # lvl 11
            [[6, 1], 8, 4, 8],  # lvl 12
            [[6, 1], 8, 4, 8],  # lvl 13
            [[7, 2], 9, 4, 9],  # lvl 14
            [[7, 2], 9, 5, 9],  # lvl 15
            [[8, 3], 10, 5, 10],  # lvl 16
            [[8, 3], 10, 5, 10],  # lvl 17
            [[9, 4], 11, 6, 11],  # lvl 18
            [[9, 4], 11, 6, 11],  # lvl 19
            [[10, 5], 12, 6, 12],  # lvl 20

        ]
