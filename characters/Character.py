from characters.SupportClassEnum import SupportClassEnum

class Character:

    def __init__(self, name, supportClass, baseStats, growthRates):
        self.name = name
        self.supportClass = supportClass
        self.baseStats = baseStats
        self.growthRates = growthRates
