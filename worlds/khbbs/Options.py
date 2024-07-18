from dataclasses import dataclass

from Options import Range, NamedRange, PerGameCommonOptions

class StartingWorlds(Range):
    """
    Number of random worlds to start with.
    """
    display_name = "Starting Worlds"
    default = 0
    range_start = 0
    range_end = 11

class EXPMultiplier(NamedRange):
    """
    Determines the multiplier to apply to EXP gained
    """
    display_name = "EXP Multiplier"
    default = 16
    range_start = default / 4
    range_end = 160
    special_range_names = {
        "0.25x": default / 4,
        "0.5x":  default / 2,
        "1x":    default,
        "2x":    default * 2,
        "3x":    default * 3,
        "4x":    default * 4,
        "8x":    default * 8,
        "10x":   default * 10,
    }

class Character(NamedRange):
    """
    Determines the expected player character.
    0: Ventus
    1: Aqua
    2: Terra
    """
    display_name = "Character"
    default = 2
    range_start = 0
    range_end = 2
    special_range_names = {
        "ventus": 0,
        "aqua":   1,
        "terra":  2,
    }
    

@dataclass
class KHBBSOptions(PerGameCommonOptions):
    character:       Character
    starting_worlds: StartingWorlds
    exp_multiplier:  EXPMultiplier
