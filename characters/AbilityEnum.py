from enum import Enum

# Defines special characteristics of a character
class AbilityEnum(Enum):
    EMPTY = 0x00

    def __int__(self):
        return self.value