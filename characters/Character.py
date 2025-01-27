from abc import ABC, abstractmethod
from typing import List

from characters.Abilities import Abilities
from characters.BaseStats import BaseStats
from characters.CharacterIDs import CharacterIDs
from characters.GrowthRates import GrowthRates
from characters.HeldItems import HeldItems
from characters.StatCalculator import StatCalculator
from characters.WeaponLevels import WeaponLevels

class Character:

    def __init__(self, name: str, startingAddress: str, statCalculator: StatCalculator, heldItems: HeldItems, data: List[int]):
        self.name = name
        self.startingAddress = startingAddress  # Where the character is stored
        self.data = data  # Do not use this for anything because the data may be modified later in our scripting
        self.baseStats = BaseStats(data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19])
        self.growthRates = GrowthRates(data[28], data[29], data[30], data[31], data[32], data[33], data[34])
        self.statCalculator = statCalculator
        self.weaponLevels = WeaponLevels(data[20], data[21], data[22], data[23], data[24], data[25], data[26], data[27])
        self.heldItems = heldItems
        self.abilities = Abilities(data[40], data[41], data[42], data[43])
        self.characterIDs = CharacterIDs(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[9],
                                         data[10], data[35], data[36], data[37], data[38], data[44], data[45],
                                         data[46], data[47], data[48])

    def getCharacterByteList(self) -> List[int]:
        return [
            self.characterIDs.nameIDSecondByte,
            self.characterIDs.nameIDFirstByte,
            self.characterIDs.detailsIDSecondByte,
            self.characterIDs.detailsIDFirstByte,
            self.characterIDs.characterID,
            self.characterIDs.supportClassID,
            self.characterIDs.portraitID,
            0x00,  # Might be NPC specific, leave at 00 for now
            0x00,  # Might be NPC specific, leave at 00 for now
            self.characterIDs.affinity,
            self.characterIDs.unitSortOrder,
            self.baseStats.level,
            self.baseStats.hp,
            self.baseStats.power,
            self.baseStats.skill,
            self.baseStats.speed,
            self.baseStats.defense,
            self.baseStats.resistance,
            self.baseStats.luck,
            self.baseStats.constitution,
            self.weaponLevels.sword,
            self.weaponLevels.lance,
            self.weaponLevels.axe,
            self.weaponLevels.bow,
            self.weaponLevels.staff,
            self.weaponLevels.anima,
            self.weaponLevels.light,
            self.weaponLevels.dark,
            self.growthRates.hp,
            self.growthRates.power,
            self.growthRates.skill,
            self.growthRates.speed,
            self.growthRates.defense,
            self.growthRates.resistance,
            self.growthRates.luck,
            self.characterIDs.baseBattlePalette,
            self.characterIDs.promoBattlePalette,
            self.characterIDs.uniqueBaseAnime,
            self.characterIDs.uniquePromoAnime,
            0x00,  # Unknown ID #1 (set to 00 for now)
            self.abilities.one,
            self.abilities.two,
            self.abilities.three,
            self.abilities.four,
            self.characterIDs.supportDataIDFourthByte,
            self.characterIDs.supportDataIDThirdByte,
            self.characterIDs.supportDataIDSecondByte,
            self.characterIDs.supportDataIDFirstByte,
            self.characterIDs.conversationGroupID,
            0x00,  # Unknown ID #2 (set to 00 for now)
            0x00,  # Unknown ID #3 (set to 00 for now)
            0x00  # Unknown ID #4 (set to 00 for now)
        ]
