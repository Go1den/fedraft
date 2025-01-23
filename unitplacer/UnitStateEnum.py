from enum import Enum

# This is used to determine if the character needs to be automatically levelled
# Generally speaking, since we want the cast to carry their exp from map to map,
# we should always set players to PLAYER_DO_NOT_GROW.
# For enemies, the bosses tend to have a set level using ENEMY_DO_NOT_GROW,
# while their minions are often set to ENEMY_CLASS_DEPENDENT.

# I'm tempted to say we don't need to ever edit these if we swap characters correctly.

# The actual value is equal to:
# base value from the enum here + (8 * ((level assigned) - 1))

# So a level 5 NPC set to do not grow would have a unit state value of
# 0x0A + (4*8) = 0x32

class UnitStateEnum(Enum):
    PLAYER_DO_NOT_GROW = 0x08
    PLAYER_CLASS_DEPENDENT = 0x09
    NPC_DO_NOT_GROW = 0x0A
    NPC_CLASS_DEPENDENT = 0x0B
    ENEMY_DO_NOT_GROW = 0x0C
    ENEMY_CLASS_DEPENDENT = 0x0D
    DEFEAT_DO_NOT_GROW = 0x0E
    DEFEAT_CLASS_DEPENDENT = 0x0F

    def __int__(self):
        return self.value
