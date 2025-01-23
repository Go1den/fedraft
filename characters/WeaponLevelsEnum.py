from enum import Enum

# Determines starting weapon EXP based on the proficiency level
class WeaponLevelsEnum(Enum):
    A = 0xB5  # 181
    B = 0x79  # 121
    C = 0x47  # 71
    D = 0x1F  # 31
    E = 0x01  # 1

    def __int__(self):
        return self.value
