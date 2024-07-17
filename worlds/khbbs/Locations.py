from typing import Dict, NamedTuple, Optional, Set
import typing


from BaseClasses import Location


class KHBBSLocation(Location):
    game: str = "Kingdom Hearts Birth by Sleep"


class KHBBSLocationData(NamedTuple):
    category: str
    type: str
    code: Optional[int] = None
    address: str = None
    forced_remote: bool = False


def get_locations_by_category(category: str) -> Dict[str, KHBBSLocationData]:
    location_dict: Dict[str, KHBBSLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: Dict[str, KHBBSLocationData] = {
    # Terra Chests
    "(T) Dwarf Woodlands Vault Balloon Letter Chest":                          KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200025, address = "version_choice({0x0, 0xD7555E}, game_version)"),
    "(T) Dwarf Woodlands Vault Ether Chest":                                   KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200026, address = "version_choice({0x0, 0xD75566}, game_version)"),
    "(T) Dwarf Woodlands Vault Potion Chest":                                  KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200027, address = "version_choice({0x0, 0xD7556E}, game_version)"),
    "(T) Dwarf Woodlands Vault Flame Salvo Chest":                             KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200028, address = "version_choice({0x0, 0xD75576}, game_version)"),
    "(T) Dwarf Woodlands Underground Waterway Potion Chest":                   KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200031, address = "version_choice({0x0, 0xD7557E}, game_version)"),
    "(T) Dwarf Woodlands Underground Waterway Block Recipe Chest":             KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200032, address = "version_choice({0x0, 0xD75586}, game_version)"),
    "(T) Dwarf Woodlands Underground Waterway Poison Edge Chest":              KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200033, address = "version_choice({0x0, 0xD7558E}, game_version)"),
    "(T) Dwarf Woodlands Courtyard Fission Firaga Chest":                      KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200034, address = "version_choice({0x0, 0xD75596}, game_version)"),
    "(T) Dwarf Woodlands Courtyard Potion Chest":                              KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200035, address = "version_choice({0x0, 0xD7559E}, game_version)"),
    "(T) Dwarf Woodlands Flower Glade Hungry Crystal Chest":                   KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200036, address = "version_choice({0x0, 0xD755A6}, game_version)"),
    "(T) Dwarf Woodlands Courtyard Map Chest":                                 KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200037, address = "version_choice({0x0, 0xD755AE}, game_version)", forced_remote = True),
    "(T) Dwarf Woodlands Underground Waterway Fire Chest":                     KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200038, address = "version_choice({0x0, 0xD755B6}, game_version)"),
    "(T) Castle of Dreams Palace Courtyard Pulsing Crystal Chest":             KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200051, address = "version_choice({0x0, 0xD755C6}, game_version)"),
    "(T) Castle of Dreams Palace Courtyard Wellspring Crystal Chest":          KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200052, address = "version_choice({0x0, 0xD755CE}, game_version)"),
    "(T) Castle of Dreams Palace Courtyard Slow Chest":                        KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200053, address = "version_choice({0x0, 0xD755D6}, game_version)"),
    "(T) Castle of Dreams Ballroom Fleeting Crystal Chest":                    KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200054, address = "version_choice({0x0, 0xD755DE}, game_version)"),
    "(T) Castle of Dreams Foyer Strike Raid Chest":                            KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200055, address = "version_choice({0x0, 0xD755E6}, game_version)"),
    "(T) Castle of Dreams Foyer Potion Chest":                                 KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200056, address = "version_choice({0x0, 0xD755EE}, game_version)"),
    "(T) Castle of Dreams Foyer Hi-Potion Chest":                              KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200057, address = "version_choice({0x0, 0xD755F6}, game_version)"),
    "(T) Castle of Dreams Foyer Soothing Crystal Chest":                       KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200058, address = "version_choice({0x0, 0xD755FE}, game_version)"),
    "(T) Castle of Dreams Antechamber Thunder Chest":                          KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200061, address = "version_choice({0x0, 0xD75606}, game_version)"),
    "(T) Castle of Dreams Palace Courtyard Map Chest":                         KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200062, address = "version_choice({0x0, 0xD7560E}, game_version)", forced_remote = True),
    "(T) Castle of Dreams Chateau Thunderstorm Chest":                         KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200063, address = "version_choice({0x0, 0xD75616}, game_version)"),
    "(T) Enchanted Dominion Waterside Potion Chest":                           KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200075, address = "version_choice({0x0, 0xD7550E}, game_version)"),
    "(T) Enchanted Dominion Forest Clearing Blizzard Chest":                   KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200076, address = "version_choice({0x0, 0xD75516}, game_version)"),
    "(T) Enchanted Dominion Audience Chamber Zero Gravity Chest":              KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200077, address = "version_choice({0x0, 0xD7551E}, game_version)"),
    "(T) Enchanted Dominion Audience Chamber Ether Chest":                     KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200078, address = "version_choice({0x0, 0xD75526}, game_version)"),
    "(T) Enchanted Dominion Audience Chamber Potion Chest":                    KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200081, address = "version_choice({0x0, 0xD7552E}, game_version)"),
    "(T) Enchanted Dominion Hallway Ether Chest":                              KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200082, address = "version_choice({0x0, 0xD75536}, game_version)"),
    "(T) Enchanted Dominion Aurora's Chamber Map Chest":                       KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200083, address = "version_choice({0x0, 0xD7553E}, game_version)", forced_remote = True),
    "(T) Enchanted Dominion Tower Room Sleep Chest":                           KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200084, address = "version_choice({0x0, 0xD75546}, game_version)"),
    "(T) Enchanted Dominion Waterside Pulsing Crystal Chest":                  KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200085, address = "version_choice({0x0, 0xD7554E}, game_version)"),
    "(T) Enchanted Dominion Tower Room Attack Recipe Chest":                   KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200086, address = "version_choice({0x0, 0xD75556}, game_version)"),
    "(T) Mysterious Tower Mysterious Tower Pulsing Crystal Chest":             KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200101, address = "version_choice({0x0, 0xD7561E}, game_version)"),
    "(T) Mysterious Tower Mysterious Tower Balloon Letter Chest":              KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200102, address = "version_choice({0x0, 0xD75626}, game_version)"),
    "(T) Mysterious Tower Mysterious Tower Cure Chest":                        KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200103, address = "version_choice({0x0, 0xD7562E}, game_version)"),
    "(T) Mysterious Tower Tower Entrance Magic Recipe Chest":                  KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200104, address = "version_choice({0x0, 0xD75636}, game_version)"),
    "(T) Radiant Garden Aqueduct Esuna Chest":                                 KHBBSLocationData("Radiant Garden",     "Chest",   227_1200125, address = "version_choice({0x0, 0xD7563E}, game_version)"),
    "(T) Radiant Garden Aqueduct Blackout Chest":                              KHBBSLocationData("Radiant Garden",     "Chest",   227_1200126, address = "version_choice({0x0, 0xD75646}, game_version)"),
    "(T) Radiant Garden Aqueduct Hi-Potion Chest":                             KHBBSLocationData("Radiant Garden",     "Chest",   227_1200127, address = "version_choice({0x0, 0xD7566E}, game_version)"),
    "(T) Radiant Garden Outer Gardens Fira Chest":                             KHBBSLocationData("Radiant Garden",     "Chest",   227_1200128, address = "version_choice({0x0, 0xD75656}, game_version)"),
    "(T) Radiant Garden Outer Gardens Pulsing Crystal Chest":                  KHBBSLocationData("Radiant Garden",     "Chest",   227_1200131, address = "version_choice({0x0, 0xD7565E}, game_version)"),
    "(T) Radiant Garden Central Square Potion Chest":                          KHBBSLocationData("Radiant Garden",     "Chest",   227_1200132, address = "version_choice({0x0, 0xD75666}, game_version)"),
    "(T) Radiant Garden Central Square Hi-Potion Chest":                       KHBBSLocationData("Radiant Garden",     "Chest",   227_1200133, address = "version_choice({0x0, 0xD7564E}, game_version)"),
    "(T) Radiant Garden Purification Facility Mega-Potion Chest":              KHBBSLocationData("Radiant Garden",     "Chest",   227_1200134, address = "version_choice({0x0, 0xD75676}, game_version)"),
    "(T) Radiant Garden Purification Facility Chaos Crystal Chest":            KHBBSLocationData("Radiant Garden",     "Chest",   227_1200135, address = "version_choice({0x0, 0xD7567E}, game_version)"),
    "(T) Radiant Garden Castle Town Map Chest":                                KHBBSLocationData("Radiant Garden",     "Chest",   227_1200136, address = "version_choice({0x0, 0xD75686}, game_version)", forced_remote = True),
    "(T) Radiant Garden Fountain Court Thunder Surge Chest":                   KHBBSLocationData("Radiant Garden",     "Chest",   227_1200137, address = "version_choice({0x0, 0xD7568E}, game_version)"),
    "(T) Radiant Garden Fountain Court Fleeting Crystal Chest":                KHBBSLocationData("Radiant Garden",     "Chest",   227_1200138, address = "version_choice({0x0, 0xD75696}, game_version)"),
    "(T) Radiant Garden Fountain Court Panacea Chest":                         KHBBSLocationData("Radiant Garden",     "Chest",   227_1200141, address = "version_choice({0x0, 0xD7569E}, game_version)"),
    "(T) Radiant Garden Merlin's House Shimmering Crystal Chest":              KHBBSLocationData("Radiant Garden",     "Chest",   227_1200142, address = "version_choice({0x0, 0xD756A6}, game_version)"),
    "(T) Olympus Coliseum Coliseum Gates Fire Strike Chest":                   KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200151, address = "version_choice({0x0, 0xD7572E}, game_version)"),
    "(T) Olympus Coliseum Coliseum Gates Mega Attack Recipe Chest":            KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200152, address = "version_choice({0x0, 0xD75736}, game_version)"),
    "(T) Olympus Coliseum Coliseum Gates Mega-Potion Chest":                   KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200153, address = "version_choice({0x0, 0xD7573E}, game_version)"),
    "(T) Olympus Coliseum Vestibule Map Chest":                                KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200154, address = "version_choice({0x0, 0xD75746}, game_version)", forced_remote = True),
    "(T) Deep Space Turo Prison Block High Jump Chest":                        KHBBSLocationData("Deep Space",         "Chest",   227_1200175, address = "version_choice({0x0, 0xD7574E}, game_version)"),
    "(T) Deep Space Durgon Transporter Hi-Potion Chest":                       KHBBSLocationData("Deep Space",         "Chest",   227_1200176, address = "version_choice({0x0, 0xD75756}, game_version)"),
    "(T) Deep Space Ship Corridor Ether Chest":                                KHBBSLocationData("Deep Space",         "Chest",   227_1200177, address = "version_choice({0x0, 0xD7575E}, game_version)"),
    "(T) Deep Space Ship Corridor Hi-Potion Chest":                            KHBBSLocationData("Deep Space",         "Chest",   227_1200178, address = "version_choice({0x0, 0xD75766}, game_version)"),
    "(T) Deep Space Ship Corridor Pulsing Crystal Chest":                      KHBBSLocationData("Deep Space",         "Chest",   227_1200181, address = "version_choice({0x0, 0xD7576E}, game_version)"),
    "(T) Deep Space Ship Corridor Warp Chest":                                 KHBBSLocationData("Deep Space",         "Chest",   227_1200182, address = "version_choice({0x0, 0xD75776}, game_version)"),
    "(T) Deep Space Control Room Hi-Potion Chest":                             KHBBSLocationData("Deep Space",         "Chest",   227_1200183, address = "version_choice({0x0, 0xD7577E}, game_version)"),
    "(T) Deep Space Turo Prison Block Brutal Blast Chest":                     KHBBSLocationData("Deep Space",         "Chest",   227_1200184, address = "version_choice({0x0, 0xD75786}, game_version)"),
    "(T) Deep Space Turo Prison Block Pulsing Crystal Chest":                  KHBBSLocationData("Deep Space",         "Chest",   227_1200185, address = "version_choice({0x0, 0xD7578E}, game_version)"),
    "(T) Deep Space Turo Prison Block Mega-Ether Chest":                       KHBBSLocationData("Deep Space",         "Chest",   227_1200186, address = "version_choice({0x0, 0xD75796}, game_version)"),
    "(T) Deep Space Ship Hub Hungry Crystal Chest":                            KHBBSLocationData("Deep Space",         "Chest",   227_1200187, address = "version_choice({0x0, 0xD7579E}, game_version)"),
    "(T) Deep Space Machinery Bay Access Mine Square Chest":                   KHBBSLocationData("Deep Space",         "Chest",   227_1200188, address = "version_choice({0x0, 0xD757A6}, game_version)"),
    "(T) Deep Space Turo Prison Block Mega-Potion Chest":                      KHBBSLocationData("Deep Space",         "Chest",   227_1200191, address = "version_choice({0x0, 0xD757AE}, game_version)"),
    "(T) Deep Space Launch Deck Thundara Chest":                               KHBBSLocationData("Deep Space",         "Chest",   227_1200192, address = "version_choice({0x0, 0xD757B6}, game_version)"),
    "(T) Deep Space Turo Transporter Map Chest":                               KHBBSLocationData("Deep Space",         "Chest",   227_1200193, address = "version_choice({0x0, 0xD757BE}, game_version)", forced_remote = True),
    "(T) Deep Space Launch Deck Abounding Crystal Chest":                      KHBBSLocationData("Deep Space",         "Chest",   227_1200195, address = "version_choice({0x0, 0xD757C6}, game_version)"),
    "(T) Deep Space Launch Deck Wellspring Crystal Chest":                     KHBBSLocationData("Deep Space",         "Chest",   227_1200196, address = "version_choice({0x0, 0xD757CE}, game_version)"),
    "(T) Deep Space Ship Hub Mega-Potion Chest":                               KHBBSLocationData("Deep Space",         "Chest",   227_1200197, address = "version_choice({0x0, 0xD757D6}, game_version)"),
    "(T) Deep Space Ship Hub Fleeting Crystal Chest":                          KHBBSLocationData("Deep Space",         "Chest",   227_1200198, address = "version_choice({0x0, 0xD757DE}, game_version)"),
    "(T) Neverland Gully Map Chest":                                           KHBBSLocationData("Neverland",          "Chest",   227_1200201, address = "version_choice({0x0, 0xD757E6}, game_version)", forced_remote = True),
    "(T) Neverland Gully Hi-Potion Chest":                                     KHBBSLocationData("Neverland",          "Chest",   227_1200202, address = "version_choice({0x0, 0xD757EE}, game_version)"),
    "(T) Neverland Cove Ether Chest":                                          KHBBSLocationData("Neverland",          "Chest",   227_1200203, address = "version_choice({0x0, 0xD757F6}, game_version)"),
    "(T) Neverland Cliff Path Hi-Potion Chest":                                KHBBSLocationData("Neverland",          "Chest",   227_1200204, address = "version_choice({0x0, 0xD757FE}, game_version)"),
    "(T) Neverland Cliff Path Mega-Potion Chest":                              KHBBSLocationData("Neverland",          "Chest",   227_1200205, address = "version_choice({0x0, 0xD75806}, game_version)"),
    "(T) Neverland Cliff Path Firaga Chest":                                   KHBBSLocationData("Neverland",          "Chest",   227_1200206, address = "version_choice({0x0, 0xD7580E}, game_version)"),
    "(T) Neverland Mermaid Lagoon Dark Haze Chest":                            KHBBSLocationData("Neverland",          "Chest",   227_1200207, address = "version_choice({0x0, 0xD75816}, game_version)"),
    "(T) Neverland Mermaid Lagoon Geo Impact Chest":                           KHBBSLocationData("Neverland",          "Chest",   227_1200208, address = "version_choice({0x0, 0xD7581E}, game_version)"),
    "(T) Neverland Mermaid Lagoon Elixir Chest":                               KHBBSLocationData("Neverland",          "Chest",   227_1200211, address = "version_choice({0x0, 0xD75826}, game_version)"),
    "(T) Neverland Peter's Hideout Shimmering Crystal Chest":                  KHBBSLocationData("Neverland",          "Chest",   227_1200212, address = "version_choice({0x0, 0xD7582E}, game_version)"),
    "(T) Neverland Peter's Hideout Mega Magic Recipe Chest":                   KHBBSLocationData("Neverland",          "Chest",   227_1200213, address = "version_choice({0x0, 0xD75836}, game_version)"),
    "(T) Neverland Jungle Clearing Hi-Potion Chest":                           KHBBSLocationData("Neverland",          "Chest",   227_1200214, address = "version_choice({0x0, 0xD7583E}, game_version)"),
    "(T) Neverland Rainbow Falls: Crest Abounding Crystal Chest":              KHBBSLocationData("Neverland",          "Chest",   227_1200215, address = "version_choice({0x0, 0xD75846}, game_version)"),
    "(T) Neverland Skull Rock: Entrance Panacea Chest":                        KHBBSLocationData("Neverland",          "Chest",   227_1200216, address = "version_choice({0x0, 0xD7584E}, game_version)"),
    "(T) Neverland Skull Rock: Cavern Megalixir Chest":                        KHBBSLocationData("Neverland",          "Chest",   227_1200217, address = "version_choice({0x0, 0xD75856}, game_version)"),
    "(T) Neverland Skull Rock: Cavern Ars Solum Chest":                        KHBBSLocationData("Neverland",          "Chest",   227_1200218, address = "version_choice({0x0, 0xD7585E}, game_version)"),
    "(T) Neverland Skull Rock: Cavern Chaos Crystal Chest":                    KHBBSLocationData("Neverland",          "Chest",   227_1200221, address = "version_choice({0x0, 0xD75866}, game_version)"),
    "(T) Neverland Rainbow Falls: Base Megalixir Chest":                       KHBBSLocationData("Neverland",          "Chest",   227_1200222, address = "version_choice({0x0, 0xD7586E}, game_version)"),
    "(T) Neverland Rainbow Falls: Base Zero Graviga Chest":                    KHBBSLocationData("Neverland",          "Chest",   227_1200223, address = "version_choice({0x0, 0xD75876}, game_version)"),
    "(T) Neverland Cove Hi-Potion Chest":                                      KHBBSLocationData("Neverland",          "Chest",   227_1200224, address = "version_choice({0x0, 0xD7587E}, game_version)"),
    "(T) Disney Town Main Plaza Map Chest":                                    KHBBSLocationData("Disney Town",        "Chest",   227_1200225, address = "version_choice({0x0, 0xD756AE}, game_version)", forced_remote = True),
    "(T) Disney Town Main Plaza Potion Chest":                                 KHBBSLocationData("Disney Town",        "Chest",   227_1200226, address = "version_choice({0x0, 0xD756B6}, game_version)"),
    "(T) Disney Town Raceway Abounding Crystal Chest":                         KHBBSLocationData("Disney Town",        "Chest",   227_1200227, address = "version_choice({0x0, 0xD756BE}, game_version)"),
    "(T) Disney Town Raceway Payback Fang Chest":                              KHBBSLocationData("Disney Town",        "Chest",   227_1200228, address = "version_choice({0x0, 0xD756C6}, game_version)"),
    "(T) Disney Town Raceway Slot Edge Chest":                                 KHBBSLocationData("Disney Town",        "Chest",   227_1200231, address = "version_choice({0x0, 0xD756CE}, game_version)"),
    "(T) Disney Town Gizmo Gallery Panacea Chest":                             KHBBSLocationData("Disney Town",        "Chest",   227_1200234, address = "version_choice({0x0, 0xD756D6}, game_version)"),
    "(T) Disney Town Gizmo Gallery Action Recipe Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200235, address = "version_choice({0x0, 0xD756DE}, game_version)"),
    "(T) Disney Town Gizmo Gallery Chaos Crystal Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200236, address = "version_choice({0x0, 0xD756E6}, game_version)"),
    "(T) Disney Town Gizmo Gallery Thunder Chest 1":                           KHBBSLocationData("Disney Town",        "Chest",   227_1200237, address = "version_choice({0x0, 0xD756EE}, game_version)"),
    "(T) Disney Town Gizmo Gallery Thunder Chest 2":                           KHBBSLocationData("Disney Town",        "Chest",   227_1200238, address = "version_choice({0x0, 0xD756F6}, game_version)"),
    "(T) Disney Town Pete's Rec Room Zero Gravira Chest":                      KHBBSLocationData("Disney Town",        "Chest",   227_1200241, address = "version_choice({0x0, 0xD756FE}, game_version)"),
    "(T) Disney Town Pete's Rec Room Aerial Slam Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200242, address = "version_choice({0x0, 0xD75706}, game_version)"),
    "(T) Disney Town Gizmo Gallery Absolute Zero Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200243, address = "version_choice({0x0, 0xD7570E}, game_version)"),
    "(T) Disney Town Pete's Rec Room Break Time Chest":                        KHBBSLocationData("Disney Town",        "Chest",   227_1200244, address = "version_choice({0x0, 0xD75716}, game_version)"),
    "(T) Disney Town Pete's Rec Room Chaos Crystal Chest":                     KHBBSLocationData("Disney Town",        "Chest",   227_1200245, address = "version_choice({0x0, 0xD7571E}, game_version)"),
    "(T) Disney Town Gizmo Gallery Mega-Potion Chest":                         KHBBSLocationData("Disney Town",        "Chest",   227_1200246, address = "version_choice({0x0, 0xD75726}, game_version)"),
    "(T) Keyblade Graveyard Twister Trench Windcutter Chest":                  KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200251, address = "version_choice({0x0, 0xD75886}, game_version)"),
    "(T) Keyblade Graveyard Twister Trench Mega-Potion Chest":                 KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200252, address = "version_choice({0x0, 0xD758AE}, game_version)"),
    "(T) Keyblade Graveyard Twister Trench Mega-Ether Chest":                  KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200253, address = "version_choice({0x0, 0xD75896}, game_version)"),
    "(T) Keyblade Graveyard Twister Trench Megalixir Chest":                   KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200254, address = "version_choice({0x0, 0xD7589E}, game_version)"),
    "(T) Keyblade Graveyard Seat of War Elixir Chest":                         KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200255, address = "version_choice({0x0, 0xD758A6}, game_version)"),
    "(T) Keyblade Graveyard Seat of War Mega-Potion Chest":                    KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200256, address = "version_choice({0x0, 0xD758AE}, game_version)"),
    "(T) Keyblade Graveyard Seat of War Map Chest":                            KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200257, address = "version_choice({0x0, 0xD758B6}, game_version)", forced_remote = True),

    # Terra Stickers
    "(T) Enchanted Dominion Forest Clearing Balloon Sticker":                  KHBBSLocationData("Enchanted Dominion", "Sticker", 227_1210002, address = "version_choice({0x0, 0xD7548E}, game_version)"),
    "(T) Enchanted Dominion Audience Chamber Huey Sticker":                    KHBBSLocationData("Enchanted Dominion", "Sticker", 227_1210003, address = "version_choice({0x0, 0xD75436}, game_version)"),
    "(T) Enchanted Dominion Tower Room Flying Balloon Sticker":                KHBBSLocationData("Enchanted Dominion", "Sticker", 227_1210004, address = "version_choice({0x0, 0xD7546E}, game_version)"),
    "(T) Castle of Dreams Chateau Traffic Cone Sticker":                       KHBBSLocationData("Castle of Dreams",   "Sticker", 227_1210005, address = "version_choice({0x0, 0xD7549E}, game_version)"),
    "(T) Castle of Dreams Passage Flying Balloon Sticker":                     KHBBSLocationData("Castle of Dreams",   "Sticker", 227_1210006, address = "version_choice({0x0, 0xD75476}, game_version)"),
    "(T) Dwarf Woodlands Underground Waterway Louie Sticker":                  KHBBSLocationData("Dwarf Woodlands",    "Sticker", 227_1210007, address = "version_choice({0x0, 0xD75446}, game_version)"),
    "(T) Dwarf Woodlands Flower Glade Balloon Sticker":                        KHBBSLocationData("Dwarf Woodlands",    "Sticker", 227_1210008, address = "version_choice({0x0, 0xD75496}, game_version)"),
    "(T) Mysterious Tower Sorcerer's Chamber Balloon Sticker":                 KHBBSLocationData("Mysterious Tower",   "Sticker", 227_1210011, address = "version_choice({0x0, 0xD754B6}, game_version)"),
    "(T) Radiant Garden Outer Gardens Airplane Sticker":                       KHBBSLocationData("Radiant Garden",     "Sticker", 227_1210012, address = "version_choice({0x0, 0xD75456}, game_version)"),
    "(T) Radiant Garden Central Square Flying Balloon Sticker":                KHBBSLocationData("Radiant Garden",     "Sticker", 227_1210013, address = "version_choice({0x0, 0xD7547E}, game_version)"),
    "(T) Radiant Fountain Court Dale Sticker":                                 KHBBSLocationData("Radiant Garden",     "Sticker", 227_1210014, address = "version_choice({0x0, 0xD75466}, game_version)"),
    "(T) Olympus Coliseum Coliseum Gates Balloon Sticker":                     KHBBSLocationData("Olympus Coliseum",   "Sticker", 227_1210015, address = "version_choice({0x0, 0xD754BE}, game_version)"),
    "(T) Deep Space Turo Prison Block Flying Balloon Sticker":                 KHBBSLocationData("Deep Space",         "Sticker", 227_1210016, address = "version_choice({0x0, 0xD75486}, game_version)"),
    "(T) Deep Space Ship Corridor UFO Sticker":                                KHBBSLocationData("Deep Space",         "Sticker", 227_1210017, address = "version_choice({0x0, 0xD754C6}, game_version)"),
    "(T) Neverland Peter's Hideout Dewey Sticker":                             KHBBSLocationData("Neverland",          "Sticker", 227_1210018, address = "version_choice({0x0, 0xD7543E}, game_version)"),
    "(T) Neverland Rainbow Falls: Base Rainbow Sticker":                       KHBBSLocationData("Neverland",          "Sticker", 227_1210021, address = "version_choice({0x0, 0xD7544E}, game_version)"),
    "(T) Neverland Skull Rock: Entrance Chip Sticker":                         KHBBSLocationData("Neverland",          "Sticker", 227_1210022, address = "version_choice({0x0, 0xD7545E}, game_version)"),
    "(T) Disney Town Gizmo Gallery Pete Sticker":                              KHBBSLocationData("Disney Town",        "Sticker", 227_1210023, address = "version_choice({0x0, 0xD7542E}, game_version)"),
    "(T) Disney Town Raceway Traffic Cone Sticker":                            KHBBSLocationData("Disney Town",        "Sticker", 227_1210024, address = "version_choice({0x0, 0xD754A6}, game_version)"),
    "(T) Keyblade Graveyard Twister Trench Traffic Cone Sticker":              KHBBSLocationData("Keyblade Graveyard", "Sticker", 227_1210025, address = "version_choice({0x0, 0xD754AE}, game_version)"),
    
    # Terra Story Rewards
    "(T) Land of Departure Orbs Defeated Max HP Increase":                     KHBBSLocationData("Land of Departure",  "Event",   227_1220000),
    "(T) Land of Departure Orbs Defeated Critical Impact":                     KHBBSLocationData("Land of Departure",  "Event",   227_1220001),
    "(T) Land of Departure Orbs Defeated Ventus D-Link":                       KHBBSLocationData("Land of Departure",  "Event",   227_1220002),
    "(T) Land of Departure Orbs Defeated Aqua D-Link":                         KHBBSLocationData("Land of Departure",  "Event",   227_1220003),
    "(T) Land of Departure Eraqus Defeated Max HP Increase":                   KHBBSLocationData("Land of Departure",  "Event",   227_1220004),
    "(T) Land of Departure Eraqus Defeated Chaos Ripper":                      KHBBSLocationData("Land of Departure",  "Event",   227_1220005),
    "(T) Land of Departure Eraqus Defeated Xehanort's Report 8":               KHBBSLocationData("Land of Departure",  "Event",   227_1220006),
    "(T) Dwarf Woodlands Unversed Group Defeated Air Slide":                   KHBBSLocationData("Dwarf Woodlands",    "Event",   227_1220100),
    "(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Max HP Increase": KHBBSLocationData("Dwarf Woodlands",    "Event",   227_1220101),
    "(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Firestorm":       KHBBSLocationData("Dwarf Woodlands",    "Event",   227_1220102),
    "(T) Dwarf Woodlands Spirit of the Magic Mirror Defeated Treasure Trove":  KHBBSLocationData("Dwarf Woodlands",    "Event",   227_1220103),
    "(T) Castle of Dreams Cinderella Escorted Counter Hammer":                 KHBBSLocationData("Castle of Dreams",   "Event",   227_1220200),
    "(T) Castle of Dreams Symphony Master Defeated Max HP Increase":           KHBBSLocationData("Castle of Dreams",   "Event",   227_1220201),
    "(T) Castle of Dreams Symphony Master Defeated Deck Capacity Increase":    KHBBSLocationData("Castle of Dreams",   "Event",   227_1220202),
    "(T) Castle of Dreams Symphony Master Defeated Cinderella D-Link":         KHBBSLocationData("Castle of Dreams",   "Event",   227_1220203),
    "(T) Castle of Dreams Symphony Master Defeated Stroke of Midnight":        KHBBSLocationData("Castle of Dreams",   "Event",   227_1220204),
    "(T) Castle of Dreams Symphony Master Defeated Royal Board":               KHBBSLocationData("Castle of Dreams",   "Event",   227_1220205),
    "(T) Enchanted Dominion Unlock Aurora's Heart Maleficent D-Link":          KHBBSLocationData("Enchanted Dominion", "Event",   227_1220300),
    "(T) Enchanted Dominion Wheel Master Defeated Deck Capacity Increase":     KHBBSLocationData("Enchanted Dominion", "Event",   227_1220301),
    "(T) Enchanted Dominion Wheel Master Defeated Diamond Dust":               KHBBSLocationData("Enchanted Dominion", "Event",   227_1220302),
    "(T) Enchanted Dominion Wheel Master Defeated Fairy Stars":                KHBBSLocationData("Enchanted Dominion", "Event",   227_1220303),
    "(T) Radiant Garden Examine Pooh's Story Book Honey Pot Board":            KHBBSLocationData("Radiant Garden",     "Event",   227_1220500),
    "(T) Radiant Garden Defeat Trinity Armor Max HP Increase":                 KHBBSLocationData("Radiant Garden",     "Event",   227_1220501),
    "(T) Radiant Garden Defeat Trinity Armor Rockbreaker":                     KHBBSLocationData("Radiant Garden",     "Event",   227_1220502),
    "(T) Radiant Garden Defeat Trinity Armor Disney Town Pass":                KHBBSLocationData("Radiant Garden",     "Event",   227_1220503),
    "(T) Radiant Garden Defeat Braig Deck Capacity Increase":                  KHBBSLocationData("Radiant Garden",     "Event",   227_1220504),
    "(T) Radiant Garden Defeat Braig Dark Volley":                             KHBBSLocationData("Radiant Garden",     "Event",   227_1220505),
    "(T) Radiant Garden Defeat Braig Xehanort's Report 2":                     KHBBSLocationData("Radiant Garden",     "Event",   227_1220506),
    "(T) Olympus Coliseum Tournament Complete Max HP Increase":                KHBBSLocationData("Olympus Coliseum",   "Event",   227_1220700),
    "(T) Olympus Coliseum Tournament Complete Sonic Impact":                   KHBBSLocationData("Olympus Coliseum",   "Event",   227_1220701),
    "(T) Olympus Coliseum Defeat Zack Deck Capacity Increase":                 KHBBSLocationData("Olympus Coliseum",   "Event",   227_1220702),
    "(T) Olympus Coliseum Defeat Zack Zack D-Link":                            KHBBSLocationData("Olympus Coliseum",   "Event",   227_1220703),
    "(T) Olympus Coliseum Defeat Zack Mark of a Hero":                         KHBBSLocationData("Olympus Coliseum",   "Event",   227_1220704),
    "(T) Deep Space Defeat Unversed in Space Max HP Increase":                 KHBBSLocationData("Deep Space",         "Event",   227_1220800),
    "(T) Deep Space Defeat Experiment 221 Thunderbolt":                        KHBBSLocationData("Deep Space",         "Event",   227_1220801),
    "(T) Deep Space Defeat Experiment 221 Experiment 626 D-Link":              KHBBSLocationData("Deep Space",         "Event",   227_1220802),
    "(T) Deep Space Defeat Experiment 221 Hyperdrive":                         KHBBSLocationData("Deep Space",         "Event",   227_1220803),
    "(T) Deep Space Defeat Experiment 221 Spaceship Board":                    KHBBSLocationData("Deep Space",         "Event",   227_1220804),
    "(T) Destiny Islands Scene Ends of the Earth":                             KHBBSLocationData("Destiny Islands",    "Event",   227_1220900),
    "(T) Neverland Defeat Peter Pan Bladecharge":                              KHBBSLocationData("Neverland",          "Event",   227_1221000),
    "(T) Neverland Defeat Peter Pan Peter Pan D-Link":                         KHBBSLocationData("Neverland",          "Event",   227_1221001),
    "(T) Neverland Defeat Countless Unversed Deck Capacity Increase":          KHBBSLocationData("Neverland",          "Event",   227_1221002),
    "(T) Neverland Defeat Countless Unversed Pixie Petal":                     KHBBSLocationData("Neverland",          "Event",   227_1221003),
    "(T) Neverland Defeat Countless Unversed Skull Board":                     KHBBSLocationData("Neverland",          "Event",   227_1221004),
    "(T) Disney Town Complete Rumble Racing Hi-Potion":                        KHBBSLocationData("Disney Town",        "Event",   227_1221100),
    "(T) Disney Town Complete Rumble Racing Toon Board":                       KHBBSLocationData("Disney Town",        "Event",   227_1221101),
    "(T) Keyblade Graveyard Meet With Xehanort Dark Impulse":                  KHBBSLocationData("Keyblade Graveyard", "Event",   227_1221200),
    "(T) Keyblade Graveyard Xehanort Defeated Max HP Increase":                KHBBSLocationData("Keyblade Graveyard", "Event",   227_1221201),
    "(T) Keyblade Graveyard Defeat Terranort":                                 KHBBSLocationData("Keyblade Graveyard", "Event",   227_1221202),
}

event_location_table: Dict[str, KHBBSLocationData] = {}
lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in location_table.items() if data.code}

location_name_groups: Dict[str, Set[str]]

# Make location categories
location_name_groups: Dict[str, Set[str]] = {}
for location in location_table.keys():
    category = location_table[location].category
    if category not in location_name_groups.keys():
        location_name_groups[category] = set([])
    location_name_groups[category].add(location)