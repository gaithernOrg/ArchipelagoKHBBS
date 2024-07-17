from typing import Dict, NamedTuple, Optional, Set
import typing


from BaseClasses import Location


class KHBBSLocation(Location):
    game: str = "Kingdom Hearts Birth by Sleep"


class KHBBSLocationData(NamedTuple):
    category: str
    type: str
    code: Optional[int] = None
    offset: str = None
    forced_remote: bool = False


def get_locations_by_category(category: str) -> Dict[str, KHBBSLocationData]:
    location_dict: Dict[str, KHBBSLocationData] = {}
    for name, data in location_table.items():
        if data.category == category:
            location_dict.setdefault(name, data)

    return location_dict

location_table: Dict[str, KHBBSLocationData] = {
    # Terra Chests
    "(T) Land of Departure Mountain Path Pulsing Crystal Chest":               KHBBSLocationData("Land of Departure",  "Chest",   227_1200002, offset = "21E"),
    "(T) Land of Departure Mountain Path Hi-Potion Chest":                     KHBBSLocationData("Land of Departure",  "Chest",   227_1200003, offset = "226"),
    "(T) Land of Departure Mountain Path Stop Chest":                          KHBBSLocationData("Land of Departure",  "Chest",   227_1200004, offset = "22E"),
    "(T) Land of Departure Summit Soothing Crystal Chest":                     KHBBSLocationData("Land of Departure",  "Chest",   227_1200005, offset = "236"),
    "(T) Dwarf Woodlands Vault Balloon Letter Chest":                          KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200025, offset = "28E"),
    "(T) Dwarf Woodlands Vault Ether Chest":                                   KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200026, offset = "296"),
    "(T) Dwarf Woodlands Vault Potion Chest":                                  KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200027, offset = "29E"),
    "(T) Dwarf Woodlands Vault Flame Salvo Chest":                             KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200028, offset = "2A6"),
    "(T) Dwarf Woodlands Underground Waterway Potion Chest":                   KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200031, offset = "2AE"),
    "(T) Dwarf Woodlands Underground Waterway Block Recipe Chest":             KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200032, offset = "2B6"),
    "(T) Dwarf Woodlands Underground Waterway Poison Edge Chest":              KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200033, offset = "2BE"),
    "(T) Dwarf Woodlands Courtyard Fission Firaga Chest":                      KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200034, offset = "2C6"),
    "(T) Dwarf Woodlands Courtyard Potion Chest":                              KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200035, offset = "2CE"),
    "(T) Dwarf Woodlands Flower Glade Hungry Crystal Chest":                   KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200036, offset = "2D6"),
    "(T) Dwarf Woodlands Courtyard Map Chest":                                 KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200037, offset = "2DE", forced_remote = True),
    "(T) Dwarf Woodlands Underground Waterway Fire Chest":                     KHBBSLocationData("Dwarf Woodlands",    "Chest",   227_1200038, offset = "2E6"),
    "(T) Castle of Dreams Palace Courtyard Pulsing Crystal Chest":             KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200051, offset = "2F6"),
    "(T) Castle of Dreams Palace Courtyard Wellspring Crystal Chest":          KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200052, offset = "2FE"),
    "(T) Castle of Dreams Palace Courtyard Slow Chest":                        KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200053, offset = "306"),
    "(T) Castle of Dreams Ballroom Fleeting Crystal Chest":                    KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200054, offset = "30E"),
    "(T) Castle of Dreams Foyer Strike Raid Chest":                            KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200055, offset = "316"),
    "(T) Castle of Dreams Foyer Potion Chest":                                 KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200056, offset = "31E"),
    "(T) Castle of Dreams Foyer Hi-Potion Chest":                              KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200057, offset = "326"),
    "(T) Castle of Dreams Foyer Soothing Crystal Chest":                       KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200058, offset = "32E"),
    "(T) Castle of Dreams Antechamber Thunder Chest":                          KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200061, offset = "336"),
    "(T) Castle of Dreams Palace Courtyard Map Chest":                         KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200062, offset = "33E", forced_remote = True),
    "(T) Castle of Dreams Chateau Thunderstorm Chest":                         KHBBSLocationData("Castle of Dreams",   "Chest",   227_1200063, offset = "346"),
    "(T) Enchanted Dominion Waterside Potion Chest":                           KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200075, offset = "23E"),
    "(T) Enchanted Dominion Forest Clearing Blizzard Chest":                   KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200076, offset = "246"),
    "(T) Enchanted Dominion Audience Chamber Zero Gravity Chest":              KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200077, offset = "24E"),
    "(T) Enchanted Dominion Audience Chamber Ether Chest":                     KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200078, offset = "256"),
    "(T) Enchanted Dominion Audience Chamber Potion Chest":                    KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200081, offset = "25E"),
    "(T) Enchanted Dominion Hallway Ether Chest":                              KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200082, offset = "266"),
    "(T) Enchanted Dominion Aurora's Chamber Map Chest":                       KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200083, offset = "26E", forced_remote = True),
    "(T) Enchanted Dominion Tower Room Sleep Chest":                           KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200084, offset = "276"),
    "(T) Enchanted Dominion Waterside Pulsing Crystal Chest":                  KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200085, offset = "27E"),
    "(T) Enchanted Dominion Tower Room Attack Recipe Chest":                   KHBBSLocationData("Enchanted Dominion", "Chest",   227_1200086, offset = "286"),
    "(T) Mysterious Tower Mysterious Tower Pulsing Crystal Chest":             KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200101, offset = "34E"),
    "(T) Mysterious Tower Mysterious Tower Balloon Letter Chest":              KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200102, offset = "356"),
    "(T) Mysterious Tower Mysterious Tower Cure Chest":                        KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200103, offset = "35E"),
    "(T) Mysterious Tower Tower Entrance Magic Recipe Chest":                  KHBBSLocationData("Mysterious Tower",   "Chest",   227_1200104, offset = "366"),
    "(T) Radiant Garden Aqueduct Esuna Chest":                                 KHBBSLocationData("Radiant Garden",     "Chest",   227_1200125, offset = "36E"),
    "(T) Radiant Garden Aqueduct Blackout Chest":                              KHBBSLocationData("Radiant Garden",     "Chest",   227_1200126, offset = "376"),
    "(T) Radiant Garden Aqueduct Hi-Potion Chest":                             KHBBSLocationData("Radiant Garden",     "Chest",   227_1200127, offset = "37E"),
    "(T) Radiant Garden Outer Gardens Fira Chest":                             KHBBSLocationData("Radiant Garden",     "Chest",   227_1200128, offset = "386"),
    "(T) Radiant Garden Outer Gardens Pulsing Crystal Chest":                  KHBBSLocationData("Radiant Garden",     "Chest",   227_1200131, offset = "38E"),
    "(T) Radiant Garden Central Square Potion Chest":                          KHBBSLocationData("Radiant Garden",     "Chest",   227_1200132, offset = "396"),
    "(T) Radiant Garden Central Square Hi-Potion Chest":                       KHBBSLocationData("Radiant Garden",     "Chest",   227_1200133, offset = "39E"),
    "(T) Radiant Garden Purification Facility Mega-Potion Chest":              KHBBSLocationData("Radiant Garden",     "Chest",   227_1200134, offset = "3A6"),
    "(T) Radiant Garden Purification Facility Chaos Crystal Chest":            KHBBSLocationData("Radiant Garden",     "Chest",   227_1200135, offset = "3AE"),
    "(T) Radiant Garden Castle Town Map Chest":                                KHBBSLocationData("Radiant Garden",     "Chest",   227_1200136, offset = "3B6", forced_remote = True),
    "(T) Radiant Garden Fountain Court Thunder Surge Chest":                   KHBBSLocationData("Radiant Garden",     "Chest",   227_1200137, offset = "3BE"),
    "(T) Radiant Garden Fountain Court Fleeting Crystal Chest":                KHBBSLocationData("Radiant Garden",     "Chest",   227_1200138, offset = "3C6"),
    "(T) Radiant Garden Fountain Court Panacea Chest":                         KHBBSLocationData("Radiant Garden",     "Chest",   227_1200141, offset = "3CE"),
    "(T) Radiant Garden Merlin's House Shimmering Crystal Chest":              KHBBSLocationData("Radiant Garden",     "Chest",   227_1200142, offset = "3D6"),
    "(T) Olympus Coliseum Coliseum Gates Fire Strike Chest":                   KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200151, offset = "45E"),
    "(T) Olympus Coliseum Coliseum Gates Mega Attack Recipe Chest":            KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200152, offset = "466"),
    "(T) Olympus Coliseum Coliseum Gates Mega-Potion Chest":                   KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200153, offset = "46E"),
    "(T) Olympus Coliseum Vestibule Map Chest":                                KHBBSLocationData("Olympus Coliseum",   "Chest",   227_1200154, offset = "476", forced_remote = True),
    "(T) Deep Space Turo Prison Block High Jump Chest":                        KHBBSLocationData("Deep Space",         "Chest",   227_1200175, offset = "47E"),
    "(T) Deep Space Durgon Transporter Hi-Potion Chest":                       KHBBSLocationData("Deep Space",         "Chest",   227_1200176, offset = "486"),
    "(T) Deep Space Ship Corridor Ether Chest":                                KHBBSLocationData("Deep Space",         "Chest",   227_1200177, offset = "48E"),
    "(T) Deep Space Ship Corridor Hi-Potion Chest":                            KHBBSLocationData("Deep Space",         "Chest",   227_1200178, offset = "496"),
    "(T) Deep Space Ship Corridor Pulsing Crystal Chest":                      KHBBSLocationData("Deep Space",         "Chest",   227_1200181, offset = "49E"),
    "(T) Deep Space Ship Corridor Warp Chest":                                 KHBBSLocationData("Deep Space",         "Chest",   227_1200182, offset = "4A6"),
    "(T) Deep Space Control Room Hi-Potion Chest":                             KHBBSLocationData("Deep Space",         "Chest",   227_1200183, offset = "4AE"),
    "(T) Deep Space Turo Prison Block Brutal Blast Chest":                     KHBBSLocationData("Deep Space",         "Chest",   227_1200184, offset = "4B6"),
    "(T) Deep Space Turo Prison Block Pulsing Crystal Chest":                  KHBBSLocationData("Deep Space",         "Chest",   227_1200185, offset = "4BE"),
    "(T) Deep Space Turo Prison Block Mega-Ether Chest":                       KHBBSLocationData("Deep Space",         "Chest",   227_1200186, offset = "4C6"),
    "(T) Deep Space Ship Hub Hungry Crystal Chest":                            KHBBSLocationData("Deep Space",         "Chest",   227_1200187, offset = "4CE"),
    "(T) Deep Space Machinery Bay Access Mine Square Chest":                   KHBBSLocationData("Deep Space",         "Chest",   227_1200188, offset = "4D6"),
    "(T) Deep Space Turo Prison Block Mega-Potion Chest":                      KHBBSLocationData("Deep Space",         "Chest",   227_1200191, offset = "4DE"),
    "(T) Deep Space Launch Deck Thundara Chest":                               KHBBSLocationData("Deep Space",         "Chest",   227_1200192, offset = "4E6"),
    "(T) Deep Space Turo Transporter Map Chest":                               KHBBSLocationData("Deep Space",         "Chest",   227_1200193, offset = "4EE", forced_remote = True),
    "(T) Deep Space Launch Deck Abounding Crystal Chest":                      KHBBSLocationData("Deep Space",         "Chest",   227_1200195, offset = "4F6"),
    "(T) Deep Space Launch Deck Wellspring Crystal Chest":                     KHBBSLocationData("Deep Space",         "Chest",   227_1200196, offset = "4FE"),
    "(T) Deep Space Ship Hub Mega-Potion Chest":                               KHBBSLocationData("Deep Space",         "Chest",   227_1200197, offset = "506"),
    "(T) Deep Space Ship Hub Fleeting Crystal Chest":                          KHBBSLocationData("Deep Space",         "Chest",   227_1200198, offset = "50E"),
    "(T) Neverland Gully Map Chest":                                           KHBBSLocationData("Neverland",          "Chest",   227_1200201, offset = "516", forced_remote = True),
    "(T) Neverland Cove Hi-Potion Chest":                                      KHBBSLocationData("Neverland",          "Chest",   227_1200202, offset = "51E"),
    "(T) Neverland Cove Ether Chest":                                          KHBBSLocationData("Neverland",          "Chest",   227_1200203, offset = "526"),
    "(T) Neverland Cliff Path Hi-Potion Chest":                                KHBBSLocationData("Neverland",          "Chest",   227_1200204, offset = "52E"),
    "(T) Neverland Cliff Path Mega-Potion Chest":                              KHBBSLocationData("Neverland",          "Chest",   227_1200205, offset = "536"),
    "(T) Neverland Cliff Path Firaga Chest":                                   KHBBSLocationData("Neverland",          "Chest",   227_1200206, offset = "53E"),
    "(T) Neverland Mermaid Lagoon Dark Haze Chest":                            KHBBSLocationData("Neverland",          "Chest",   227_1200207, offset = "546"),
    "(T) Neverland Mermaid Lagoon Geo Impact Chest":                           KHBBSLocationData("Neverland",          "Chest",   227_1200208, offset = "54E"),
    "(T) Neverland Mermaid Lagoon Elixir Chest":                               KHBBSLocationData("Neverland",          "Chest",   227_1200211, offset = "556"),
    "(T) Neverland Peter's Hideout Shimmering Crystal Chest":                  KHBBSLocationData("Neverland",          "Chest",   227_1200212, offset = "55E"),
    "(T) Neverland Peter's Hideout Mega Magic Recipe Chest":                   KHBBSLocationData("Neverland",          "Chest",   227_1200213, offset = "566"),
    "(T) Neverland Jungle Clearing Hi-Potion Chest":                           KHBBSLocationData("Neverland",          "Chest",   227_1200214, offset = "56E"),
    "(T) Neverland Rainbow Falls: Crest Abounding Crystal Chest":              KHBBSLocationData("Neverland",          "Chest",   227_1200215, offset = "576"),
    "(T) Neverland Skull Rock: Entrance Panacea Chest":                        KHBBSLocationData("Neverland",          "Chest",   227_1200216, offset = "57E"),
    "(T) Neverland Skull Rock: Cavern Megalixir Chest":                        KHBBSLocationData("Neverland",          "Chest",   227_1200217, offset = "586"),
    "(T) Neverland Skull Rock: Cavern Ars Solum Chest":                        KHBBSLocationData("Neverland",          "Chest",   227_1200218, offset = "58E"),
    "(T) Neverland Skull Rock: Cavern Chaos Crystal Chest":                    KHBBSLocationData("Neverland",          "Chest",   227_1200221, offset = "596"),
    "(T) Neverland Rainbow Falls: Base Megalixir Chest":                       KHBBSLocationData("Neverland",          "Chest",   227_1200222, offset = "59E"),
    "(T) Neverland Rainbow Falls: Base Zero Graviga Chest":                    KHBBSLocationData("Neverland",          "Chest",   227_1200223, offset = "5A6"),
    "(T) Neverland Gully Hi-Potion Chest":                                     KHBBSLocationData("Neverland",          "Chest",   227_1200224, offset = "5AE"),
    "(T) Disney Town Main Plaza Map Chest":                                    KHBBSLocationData("Disney Town",        "Chest",   227_1200225, offset = "3DE", forced_remote = True),
    "(T) Disney Town Main Plaza Potion Chest":                                 KHBBSLocationData("Disney Town",        "Chest",   227_1200226, offset = "3E6"),
    "(T) Disney Town Raceway Abounding Crystal Chest":                         KHBBSLocationData("Disney Town",        "Chest",   227_1200227, offset = "3EE"),
    "(T) Disney Town Raceway Payback Fang Chest":                              KHBBSLocationData("Disney Town",        "Chest",   227_1200228, offset = "3F6"),
    "(T) Disney Town Raceway Slot Edge Chest":                                 KHBBSLocationData("Disney Town",        "Chest",   227_1200231, offset = "3FE"),
    "(T) Disney Town Gizmo Gallery Panacea Chest":                             KHBBSLocationData("Disney Town",        "Chest",   227_1200234, offset = "406"),
    "(T) Disney Town Gizmo Gallery Action Recipe Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200235, offset = "40E"),
    "(T) Disney Town Gizmo Gallery Chaos Crystal Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200236, offset = "416"),
    "(T) Disney Town Gizmo Gallery Thunder Chest 1":                           KHBBSLocationData("Disney Town",        "Chest",   227_1200237, offset = "41E"),
    "(T) Disney Town Gizmo Gallery Thunder Chest 2":                           KHBBSLocationData("Disney Town",        "Chest",   227_1200238, offset = "426"),
    "(T) Disney Town Pete's Rec Room Zero Gravira Chest":                      KHBBSLocationData("Disney Town",        "Chest",   227_1200241, offset = "42E"),
    "(T) Disney Town Pete's Rec Room Aerial Slam Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200242, offset = "436"),
    "(T) Disney Town Gizmo Gallery Absolute Zero Chest":                       KHBBSLocationData("Disney Town",        "Chest",   227_1200243, offset = "43E"),
    "(T) Disney Town Pete's Rec Room Break Time Chest":                        KHBBSLocationData("Disney Town",        "Chest",   227_1200244, offset = "446"),
    "(T) Disney Town Pete's Rec Room Chaos Crystal Chest":                     KHBBSLocationData("Disney Town",        "Chest",   227_1200245, offset = "44E"),
    "(T) Disney Town Gizmo Gallery Mega-Potion Chest":                         KHBBSLocationData("Disney Town",        "Chest",   227_1200246, offset = "456"),
    "(T) Keyblade Graveyard Twister Trench Windcutter Chest":                  KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200251, offset = "5B6"),
    "(T) Keyblade Graveyard Twister Trench Mega-Potion Chest":                 KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200252, offset = "5DE"),
    "(T) Keyblade Graveyard Twister Trench Mega-Ether Chest":                  KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200253, offset = "5C6"),
    "(T) Keyblade Graveyard Twister Trench Megalixir Chest":                   KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200254, offset = "5CE"),
    "(T) Keyblade Graveyard Seat of War Elixir Chest":                         KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200255, offset = "5D6"),
    "(T) Keyblade Graveyard Seat of War Mega-Potion Chest":                    KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200256, offset = "5DE"),
    "(T) Keyblade Graveyard Seat of War Map Chest":                            KHBBSLocationData("Keyblade Graveyard", "Chest",   227_1200257, offset = "5E6", forced_remote = True),

    # Terra Stickers
    "(T) Enchanted Dominion Forest Clearing Balloon Sticker":                  KHBBSLocationData("Enchanted Dominion", "Sticker", 227_1210002, offset = "1BE"),
    "(T) Enchanted Dominion Audience Chamber Huey Sticker":                    KHBBSLocationData("Enchanted Dominion", "Sticker", 227_1210003, offset = "166"),
    "(T) Enchanted Dominion Tower Room Flying Balloon Sticker":                KHBBSLocationData("Enchanted Dominion", "Sticker", 227_1210004, offset = "19E"),
    "(T) Castle of Dreams Chateau Traffic Cone Sticker":                       KHBBSLocationData("Castle of Dreams",   "Sticker", 227_1210005, offset = "1CE"),
    "(T) Castle of Dreams Passage Flying Balloon Sticker":                     KHBBSLocationData("Castle of Dreams",   "Sticker", 227_1210006, offset = "1A6"),
    "(T) Dwarf Woodlands Underground Waterway Louie Sticker":                  KHBBSLocationData("Dwarf Woodlands",    "Sticker", 227_1210007, offset = "176"),
    "(T) Dwarf Woodlands Flower Glade Balloon Sticker":                        KHBBSLocationData("Dwarf Woodlands",    "Sticker", 227_1210008, offset = "1C6"),
    "(T) Mysterious Tower Sorcerer's Chamber Balloon Sticker":                 KHBBSLocationData("Mysterious Tower",   "Sticker", 227_1210011, offset = "1E6"),
    "(T) Radiant Garden Outer Gardens Airplane Sticker":                       KHBBSLocationData("Radiant Garden",     "Sticker", 227_1210012, offset = "186"),
    "(T) Radiant Garden Central Square Flying Balloon Sticker":                KHBBSLocationData("Radiant Garden",     "Sticker", 227_1210013, offset = "1AE"),
    "(T) Radiant Fountain Court Dale Sticker":                                 KHBBSLocationData("Radiant Garden",     "Sticker", 227_1210014, offset = "196"),
    "(T) Olympus Coliseum Coliseum Gates Balloon Sticker":                     KHBBSLocationData("Olympus Coliseum",   "Sticker", 227_1210015, offset = "1EE"),
    "(T) Deep Space Turo Prison Block Flying Balloon Sticker":                 KHBBSLocationData("Deep Space",         "Sticker", 227_1210016, offset = "1B6"),
    "(T) Deep Space Ship Corridor UFO Sticker":                                KHBBSLocationData("Deep Space",         "Sticker", 227_1210017, offset = "1F6"),
    "(T) Neverland Peter's Hideout Dewey Sticker":                             KHBBSLocationData("Neverland",          "Sticker", 227_1210018, offset = "16E"),
    "(T) Neverland Rainbow Falls: Base Rainbow Sticker":                       KHBBSLocationData("Neverland",          "Sticker", 227_1210021, offset = "17E"),
    "(T) Neverland Skull Rock: Entrance Chip Sticker":                         KHBBSLocationData("Neverland",          "Sticker", 227_1210022, offset = "18E"),
    "(T) Disney Town Gizmo Gallery Pete Sticker":                              KHBBSLocationData("Disney Town",        "Sticker", 227_1210023, offset = "15E"),
    "(T) Disney Town Raceway Traffic Cone Sticker":                            KHBBSLocationData("Disney Town",        "Sticker", 227_1210024, offset = "1D6"),
    "(T) Keyblade Graveyard Twister Trench Traffic Cone Sticker":              KHBBSLocationData("Keyblade Graveyard", "Sticker", 227_1210025, offset = "1DE"),
    
    # Terra Story Rewards
    "(T) Land of Departure Orbs Defeated Max HP Increase":                     KHBBSLocationData("Land of Departure",  "Event",   227_1220000),
    "(T) Land of Departure Orbs Defeated Critical Impact":                     KHBBSLocationData("Land of Departure",  "Event",   227_1220001),
    "(T) Land of Departure Orbs Defeated Ventus D-Link":                       KHBBSLocationData("Land of Departure",  "Event",   227_1220002),
    "(T) Land of Departure Orbs Defeated Aqua D-Link":                         KHBBSLocationData("Land of Departure",  "Event",   227_1220003),
    "(T) Land of Departure Orbs Defeated Keyblade Board":                      KHBBSLocationData("Land of Departure",  "Event",   227_1220004),
    "(T) Land of Departure Eraqus Defeated Max HP Increase":                   KHBBSLocationData("Land of Departure",  "Event",   227_1220005),
    "(T) Land of Departure Eraqus Defeated Chaos Ripper":                      KHBBSLocationData("Land of Departure",  "Event",   227_1220006),
    "(T) Land of Departure Eraqus Defeated Xehanort's Report 8":               KHBBSLocationData("Land of Departure",  "Event",   227_1220007),
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