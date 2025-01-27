# Stores several character-specific IDs that don't really belong in any other grouping

class CharacterIDs:
    def __init__(self, nameIDSecondByte, nameIDFirstByte, detailsIDSecondByte, detailsIDFirstByte,
                 characterID, supportClassID, portraitID, affinity, unitSortOrder, baseBattlePalette,
                 promoBattlePalette, uniqueBaseAnime, uniquePromoAnime, supportDataIDFourthByte,
                 supportDataIDThirdByte, supportDataIDSecondByte, supportDataIDFirstByte,
                 conversationGroupID):
        self.nameIDSecondByte = nameIDSecondByte
        self.nameIDFirstByte = nameIDFirstByte
        self.detailsIDSecondByte = detailsIDSecondByte
        self.detailsIDFirstByte = detailsIDFirstByte
        self.characterID = characterID
        self.supportClassID = supportClassID
        self.portraitID = portraitID
        self.affinity = affinity
        self.unitSortOrder = unitSortOrder
        self.baseBattlePalette = baseBattlePalette
        self.promoBattlePalette = promoBattlePalette
        self.uniqueBaseAnime = uniqueBaseAnime
        self.uniquePromoAnime = uniquePromoAnime
        self.supportDataIDFourthByte = supportDataIDFourthByte
        self.supportDataIDThirdByte = supportDataIDThirdByte
        self.supportDataIDSecondByte = supportDataIDSecondByte
        self.supportDataIDFirstByte = supportDataIDFirstByte
        self.conversationGroupID = conversationGroupID


