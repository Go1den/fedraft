from characters.Abilities import Abilities
from characters.AbilityEnum import AbilityEnum
from characters.BaseStats import BaseStats
from characters.GrowthRates import GrowthRates
from characters.HeldItems import HeldItems
from characters.StatCalculator import StatCalculator
from characters.SupportClassEnum import SupportClassEnum
from characters.WeaponLevels import WeaponLevels
from characters.WeaponLevelsEnum import WeaponLevelsEnum
from items.ItemEnum import ItemEnum

class Eliwood():

    def __init__(self):
        self.id = 0x01
        self.supportClass = SupportClassEnum.LORD_ELIWOOD
        self.baseStats = BaseStats(1, 0, 0, 0, 0, 0, 0, 7, 0)
        self.growthRates = GrowthRates(80, 45, 50, 40, 30, 35, 45)
        self.statCalculator = StatCalculator(40,49, 23, 25, 23, 17, 14, 25)
        self.weaponLevels = WeaponLevels(WeaponLevelsEnum.C, 0, 0, 0, 0, 0, 0, 0)
        self.heldItems = HeldItems(ItemEnum.RAPIER, ItemEnum.VULNERARY, ItemEnum.EMPTY, ItemEnum.EMPTY)
        self.abilities = Abilities(AbilityEnum.EMPTY, AbilityEnum.EMPTY, AbilityEnum.EMPTY, AbilityEnum.EMPTY)
