from typing import Dict, NamedTuple, Optional, Set
import typing


from BaseClasses import Location


class KHBBSLocation(Location):
    game: str = "Kingdom Hearts Birth by Sleep"


class KHBBSLocationData(NamedTuple):
    category: str
    characters: str = "TVA"
    code: Optional[int] = None
    


def get_locations_by_category(category: str) -> Dict[str, KHBBSLocationData]:
    location_dict: Dict[str, KHBBSLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: Dict[str, KHBBSLocationData] = {
    # Terra Chests
    "Dwarf Woodlands Vault Balloon Letter Chest":                 KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200025),
    "Dwarf Woodlands Vault Ether Chest":                          KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200026),
    "Dwarf Woodlands Vault Potion Chest":                         KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200027),
    "Dwarf Woodlands Vault Flame Salvo Chest":                    KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200028),
    "Dwarf Woodlands Underground Waterway Potion Chest":          KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200031),
    "Dwarf Woodlands Underground Waterway Block Recipe Chest":    KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200032),
    "Dwarf Woodlands Underground Waterway Poison Edge Chest":     KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200033),
    "Dwarf Woodlands Courtyard Fission Firaga Chest":             KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200034),
    "Dwarf Woodlands Courtyard Potion Chest":                     KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200035),
    "Dwarf Woodlands Flower Glade Hungry Crystal Chest":          KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200036),
    "Dwarf Woodlands Courtyard Map Chest":                        KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200037),
    "Dwarf Woodlands Underground Waterway Fire Chest":            KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1200038),
    "Castle of Dreams Palace Courtyard Pulsing Crystal Chest":    KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200051),
    "Castle of Dreams Palace Courtyard Wellspring Crystal Chest": KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200052),
    "Castle of Dreams Palace Courtyard Slow Chest":               KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200053),
    "Castle of Dreams Ballroom Fleeting Crystal Chest":           KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200054),
    "Castle of Dreams Foyer Strike Raid Chest":                   KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200055),
    "Castle of Dreams Foyer Potion Chest":                        KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200056),
    "Castle of Dreams Foyer Hi-Potion Chest":                     KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200057),
    "Castle of Dreams Foyer Soothing Crystal Chest":              KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200058),
    "Castle of Dreams Antechamber Thunder Chest":                 KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200061),
    "Castle of Dreams Palace Courtyard Map Chest":                KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200062),
    "Castle of Dreams Chateau Thunderstorm Chest":                KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1200063),
    "Enchanted Dominion Waterside Potion Chest":                  KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200075),
    "Enchanted Dominion Forest Clearing Blizzard Chest":          KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200076),
    "Enchanted Dominion Audience Chamber Zero Gravity Chest":     KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200077),
    "Enchanted Dominion Hallway Ether Chest":                     KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200078),
    "Enchanted Audience Chamber Potion Chest":                    KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200081),
    "Enchanted Audience Chamber Ether Chest":                     KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200082),
    "Enchanted Aurora's Chamber Map Chest":                       KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200083),
    "Enchanted Tower Room Sleep Chest":                           KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200084),
    "Enchanted Waterside Pulsing Crystal Chest":                  KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200085),
    "Enchanted Tower Room Attack Recipe Chest":                   KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1200086),
    "Mysterious Tower Mysterious Tower Pulsing Crystal Chest":    KHBBSLocationData("Mysterious Tower",   characters = "T  ", 227_1200101),
    "Mysterious Tower Mysterious Tower Balloon Letter Chest":     KHBBSLocationData("Mysterious Tower",   characters = "T  ", 227_1200102),
    "Mysterious Tower Mysterious Tower Cure Chest":               KHBBSLocationData("Mysterious Tower",   characters = "T  ", 227_1200103),
    "Mysterious Tower Tower Entrance Magic Recipe Chest":         KHBBSLocationData("Mysterious Tower",   characters = "T  ", 227_1200104),
    "Radiant Garden Aqueduct Esuna Chest":                        KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200125),
    "Radiant Garden Aqueduct Blackout Chest":                     KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200126),
    "Radiant Garden Aqueduct Hi-Potion Chest":                    KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200127),
    "Radiant Garden Outer Gardens Fira Chest":                    KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200128),
    "Radiant Garden Outer Gardens Pulsing Crystal Chest":         KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200131),
    "Radiant Garden Central Square Potion Chest":                 KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200132),
    "Radiant Garden Central Square Hi-Potion Chest":              KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200133),
    "Radiant Garden Purification Facility Mega-Potion Chest":     KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200134),
    "Radiant Garden Purification Facility Chaos Crystal Chest":   KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200135),
    "Radiant Castle Town Map Chest":                              KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200136),
    "Radiant Fountain Court Thunder Surge Chest":                 KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200137),
    "Radiant Fountain Court Fleeting Crystal Chest":              KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200138),
    "Radiant Fountain Court Panacea Chest":                       KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200141),
    "Radiant Merlin's House Shimmering Crystal Chest":            KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1200142),
    "Olympus Coliseum Coliseum Gates Fire Strike Chest":          KHBBSLocationData("Olympus Coliseum",   characters = "T  ", 227_1200151),
    "Olympus Coliseum Coliseum Gates Mega Attack Recipe Chest":   KHBBSLocationData("Olympus Coliseum",   characters = "T  ", 227_1200152),
    "Olympus Coliseum Coliseum Gates Mega-Potion Recipe Chest":   KHBBSLocationData("Olympus Coliseum",   characters = "T  ", 227_1200153),
    "Olympus Coliseum Vestibule Map Chest":                       KHBBSLocationData("Olympus Coliseum",   characters = "T  ", 227_1200154),
    "Deep Space Turo Prison Block High Jump Chest":               KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200175),
    "Deep Space Durgon Transporter Hi-Potion Chest":              KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200176),
    "Deep Space Ship Corridor Ether Chest":                       KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200177),
    "Deep Space Ship Corridor Hi-Potion Chest":                   KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200178),
    "Deep Space Ship Corridor Pulsing Crystal Chest":             KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200181),
    "Deep Space Ship Corridor Warp Chest":                        KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200182),
    "Deep Space Control Room Hi-Potion Chest":                    KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200183),
    "Deep Space Turo Prison Block Brutal Blast Chest":            KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200184),
    "Deep Space Turo Prison Block Pulsing Crystal Chest":         KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200185),
    "Deep Space Turo Prison Block Mega-Ether Chest":              KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200186),
    "Deep Space Ship Hub Hungry Crystal Chest":                   KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200187),
    "Deep Space Machinery Bay Access Mine Square Chest":          KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200188),
    "Deep Space Turo Prison Block Mega-Potion Chest":             KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200191),
    "Deep Space Launch Deck Thundara Chest":                      KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200192),
    "Deep Space Turo Transporter Map Chest":                      KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200193),
    "Deep Launch Deck Abounding Crystal Chest":                   KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200195),
    "Deep Launch Deck Wellspring Crystal Chest":                  KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200196),
    "Deep Ship Hub Mega-Potion Chest":                            KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200197),
    "Deep Ship Hub Fleeting Crystal Chest":                       KHBBSLocationData("Deep Space",         characters = "T  ", 227_1200198),
    "Neverland Gully Map Chest":                                  KHBBSLocationData("Neverland",          characters = "T  ", 227_1200201),
    "Neverland Gully Hi-Potion Chest":                            KHBBSLocationData("Neverland",          characters = "T  ", 227_1200202),
    "Neverland Cove Ether Chest":                                 KHBBSLocationData("Neverland",          characters = "T  ", 227_1200203),
    "Neverland Cliff Path Hi-Potion Chest":                       KHBBSLocationData("Neverland",          characters = "T  ", 227_1200204),
    "Neverland Cliff Path Mega-Potion Chest":                     KHBBSLocationData("Neverland",          characters = "T  ", 227_1200205),
    "Neverland Cliff Path Firaga Chest":                          KHBBSLocationData("Neverland",          characters = "T  ", 227_1200206),
    "Neverland Mermaid Lagoon Dark Haze Chest":                   KHBBSLocationData("Neverland",          characters = "T  ", 227_1200207),
    "Neverland Mermaid Lagoon Geo Impact Chest":                  KHBBSLocationData("Neverland",          characters = "T  ", 227_1200208),
    "Neverland Mermaid Lagoon Elixir Chest":                      KHBBSLocationData("Neverland",          characters = "T  ", 227_1200211),
    "Neverland Peter's Hideout Shimmering Crystal Chest":         KHBBSLocationData("Neverland",          characters = "T  ", 227_1200212),
    "Neverland Peter's Hideout Mega Magic Recipe Chest":          KHBBSLocationData("Neverland",          characters = "T  ", 227_1200213),
    "Neverland Jungle Clearing Hi-Potion Chest":                  KHBBSLocationData("Neverland",          characters = "T  ", 227_1200214),
    "Neverland Rainbow Falls: Crest Abounding Crystal Chest":     KHBBSLocationData("Neverland",          characters = "T  ", 227_1200215),
    "Neverland Skull Rock: Entrance Panacea Chest":               KHBBSLocationData("Neverland",          characters = "T  ", 227_1200216),
    "Neverland Skull Rock: Cavern Megalixir Chest":               KHBBSLocationData("Neverland",          characters = "T  ", 227_1200217),
    "Neverland Skull Rock: Cavern Ars Solum Chest":               KHBBSLocationData("Neverland",          characters = "T  ", 227_1200218),
    "Neverland Skull Rock: Cavern Chaos Crystal Chest":           KHBBSLocationData("Neverland",          characters = "T  ", 227_1200221),
    "Neverland Rainbow Falls: Base Megalixir Chest":              KHBBSLocationData("Neverland",          characters = "T  ", 227_1200222),
    "Neverland Rainbow Falls: Base Zero Graviga Chest":           KHBBSLocationData("Neverland",          characters = "T  ", 227_1200223),
    "Neverland Cove Hi-Potion Chest":                             KHBBSLocationData("Neverland",          characters = "T  ", 227_1200224),
    "Disney Town Main Plaza Map Chest":                           KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200225),
    "Disney Town Main Plaza Potion Chest":                        KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200226),
    "Disney Town Raceway Abounding Crystal Chest":                KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200227),
    "Disney Town Raceway Payback Fang Chest":                     KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200228),
    "Disney Town Raceway Slot Edge Chest":                        KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200231),
    "Disney Town Gizmo Gallery Panacea Chest":                    KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200234),
    "Disney Town Gizmo Gallery Action Recipe Chest":              KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200235),
    "Disney Town Gizmo Gallery Chaos Crystal Chest":              KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200236),
    "Disney Town Gizmo Gallery Thunder Chest 1":                  KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200237),
    "Disney Town Gizmo Gallery Thunder Chest 2":                  KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200238),
    "Disney Town Pete's Rec Room Zero Graviga Chest":             KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200241),
    "Disney Town Pete's Rec Room Aerial Slam Chest":              KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200242),
    "Disney Town Gizmo Gallery Absolute Zero Chest":              KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200243),
    "Disney Town Pete's Rec Room Break Time Chest":               KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200244),
    "Disney Town Pete's Rec Room Chaos Crystal Chest":            KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200245),
    "Disney Town Gizmo Gallery Mega-Potion Chest":                KHBBSLocationData("Disney Town",        characters = "T  ", 227_1200246),
    "Keyblade Graveyard Twister Trench Windcutter Chest":         KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1200251),
    "Keyblade Graveyard Twister Trench Mega-Potion Chest":        KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1200252),
    "Keyblade Graveyard Twister Trench Mega-Ether Chest":         KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1200253),
    "Keyblade Graveyard Twister Trench Megalixir Chest":          KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1200254),
    "Keyblade Graveyard Seat of War Elixir Chest":                KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1200255),
    "Keyblade Graveyard Seat of War Mega-Potion Chest":           KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1200256),
    "Keyblade Graveyard Seat of War Map Chest":                   KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1200257),

    # Terra Stickers
    "Enchanted Dominion Forest Clearing Balloon Sticker":         KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1210002),
    "Enchanted Dominion Audience Chamber Huey Sticker":           KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1210003),
    "Enchanted Dominion Tower Room Flying Balloon Sticker":       KHBBSLocationData("Enchanted Dominion", characters = "T  ", 227_1210004),
    "Castle of Dreams Chateau Traffic Cone Sticker":              KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1210005),
    "Castle of Dreams Passage Flying Balloon Sticker":            KHBBSLocationData("Castle of Dreams",   characters = "T  ", 227_1210006),
    "Dwarf Woodlands Underground Waterway Louie Sticker":         KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1210007),
    "Dwarf Woodlands Flower Glade Balloon Sticker":               KHBBSLocationData("Dwarf Woodlands",    characters = "T  ", 227_1210008),
    "Mysterious Tower Sorcerer's Chamber Balloon Sticker":        KHBBSLocationData("Mysterious Tower",   characters = "T  ", 227_1210011),
    "Radiant Garden Outer Gardens Airplane Sticker":              KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1210012),
    "Radiant Garden Central Square Flying Balloon Sticker":       KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1210013),
    "Radiant Fountain Court Dale Sticker":                        KHBBSLocationData("Radiant Garden",     characters = "T  ", 227_1210014),
    "Olympus Coliseum Coliseum Gates Balloon Sticker":            KHBBSLocationData("Olympus Coliseum",   characters = "T  ", 227_1210015),
    "Deep Space Turo Prison Block Flying Balloon Sticker":        KHBBSLocationData("Deep Space",         characters = "T  ", 227_1210016),
    "Deep Space Ship Corridor UFO Sticker":                       KHBBSLocationData("Deep Space",         characters = "T  ", 227_1210017),
    "Neverland Peter's Hideout Dewey Sticker":                    KHBBSLocationData("Neverland",          characters = "T  ", 227_1210018),
    "Neverland Rainbow Falls: Base Rainbow Sticker":              KHBBSLocationData("Neverland",          characters = "T  ", 227_1210021),
    "Neverland Skull Rock: Entrance Chip Sticker":                KHBBSLocationData("Neverland",          characters = "T  ", 227_1210022),
    "Disney Town Gizmo Gallery Pete Sticker":                     KHBBSLocationData("Disney Town",        characters = "T  ", 227_1210023),
    "Disney Town Raceway Traffic Cone Sticker":                   KHBBSLocationData("Disney Town",        characters = "T  ", 227_1210024),
    "Keyblade Graveyard Twister Trench Traffic Cone Sticker":     KHBBSLocationData("Keyblade Graveyard", characters = "T  ", 227_1210025),
    
    # Terra Story Rewards
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