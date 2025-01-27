from enum import Enum

# A character's affinity
class AffinityEnum(Enum):
    EMPTY = 0x00
    FIRE = 0x01
    THUNDER = 0x02
    WIND = 0x03
    ICE = 0x04
    DARK = 0x05
    LIGHT = 0x06
    ANIMA = 0x07

    def __int__(self):
        return self.value
