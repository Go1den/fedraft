# For a given character, a StatCalculator object tells us what we can anticipate their stats being at a specified level
# We can use this information to balance a character's base stats based on their assigned starting level
# The aim is to keep a character's growth consistent with the base game no matter what actual level they start at

class StatCalculator:

    def __init__(self, level, hp, power, skill, speed, defense, resistance, luck):
        self.level = level # At this level, we expect to see the following stat values (default level is 40)
        self.hp = hp
        self.power = power
        self.skill = skill
        self.speed = speed
        self.defense = defense
        self.resistance = resistance
        self.luck = luck

