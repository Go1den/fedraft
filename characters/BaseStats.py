# These are the unit's base stats as they appear in the base game
# We can do math using this information and the GrowthRates of that character to alter these base stats in such a way
# that their growth is consistent with the base game, even if they start at a different level than they do in the base game.

class BaseStats:

    def __init__(self, level, hp, power, skill, speed, defense, resistance, luck, constitution):
        self.level = level
        self.hp = hp
        self.power = power
        self.skill = skill
        self.speed = speed
        self.defense = defense
        self.resistance = resistance
        self.luck = luck
        self.constitution = constitution
