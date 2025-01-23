# For a given character, a GrowthRates object tells us the % chance each stat will increase on a level up
# We can use this information along with StatCalculator and BaseStats to balance a character to their assigned starting level
# The aim is to keep a character's growth consistent with the base game no matter what actual level they start at

class GrowthRates:

    def __init__(self, hp, power, skill, speed, defense, resistance, luck):
        self.hp = hp
        self.power = power
        self.skill = skill
        self.speed = speed
        self.defense = defense
        self.resistance = resistance
        self.luck = luck

    def getSum(self):
        return self.hp + self.power + self.skill + self.speed + self.defense + self.resistance + self.luck
