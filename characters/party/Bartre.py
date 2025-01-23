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

class Bartre():

    def __init__(self):
        self.id = 0x09
        self.supportClass = SupportClassEnum.FIGHTER
        self.baseStats = BaseStats(2, 9, 4, 3, -1, 2, 0, 4, 2)
        self.growthRates = GrowthRates(85, 50, 35, 40, 30, 25, 30)
        self.statCalculator = StatCalculator(40, 61, 28, 18, 18, 15, 10, 15)
        self.weaponLevels = WeaponLevels(0, 0, WeaponLevelsEnum.D, 0, 0, 0, 0, 0)
        self.heldItems = HeldItems(ItemEnum.IRON_AXE, ItemEnum.HAND_AXE, ItemEnum.EMPTY, ItemEnum.EMPTY)
        self.abilities = Abilities(AbilityEnum.EMPTY, AbilityEnum.EMPTY, AbilityEnum.EMPTY, AbilityEnum.EMPTY)
