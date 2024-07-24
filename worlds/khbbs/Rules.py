from BaseClasses import CollectionState, MultiWorld

def set_rules(khbbsworld):
    multiworld = khbbsworld.multiworld
    player     = khbbsworld.player
    options    = khbbsworld.options
    # Location Rules
    if options.character == 2:
        multiworld.get_location("(T) The Land of Departure Defeat Eraqus Max HP Increase"       , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(T) The Land of Departure Defeat Eraqus Chaos Ripper"          , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(T) The Land of Departure Defeat Eraqus Xehanort's Report 8"   , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(T) Dwarf Woodlands Vault Flame Salvo Chest"                   , player).access_rule = lambda state: state.has("Sliding Dash", player) and (state.has("High Jump", player) or state.has("Air Slide", player))
        multiworld.get_location("(T) Dwarf Woodlands Underground Waterway Louie Sticker"        , player).access_rule = lambda state: state.has("Sliding Dash", player)
        multiworld.get_location("(T) Dwarf Woodlands Courtyard Fission Firaga Chest"            , player).access_rule = lambda state: state.has("Sliding Dash", player) or state.has("High Jump", player)
        multiworld.get_location("(T) Enchanted Dominion Audience Chamber Huey Sticker"          , player).access_rule = lambda state: state.has("Sliding Dash", player) or (state.has("High Jump", player) and state.has("Air Slide", player))
        multiworld.get_location("(T) Castle of Dreams Passage Flying Balloon Sticker"           , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Radiant Garden Fountain Court Dale Sticker"                , player).access_rule = lambda state: state.has("High Jump", player) and state.has("Sliding Dash", player)
        multiworld.get_location("(T) Radiant Garden Outer Gardens Airplane Sticker"             , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Olympus Coliseum Coliseum Gates Balloon Sticker"           , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Deep Space Turo Prison Block Brutal Blast Chest"           , player).access_rule = lambda state: state.has("High Jump", player) or state.has("Air Slide", player) or state.has("Sliding Dash", player)
        multiworld.get_location("(T) Deep Space Turo Prison Block Flying Balloon Sticker"       , player).access_rule = lambda state: state.has("High Jump", player) or state.has("Air Slide", player) or state.has("Sliding Dash", player)
        multiworld.get_location("(T) Deep Space Turo Prison Block Mega-Potion Chest"            , player).access_rule = lambda state: state.has("High Jump", player) or state.has("Air Slide", player) or state.has("Sliding Dash", player)
        multiworld.get_location("(T) Deep Space Machinery Bay Access Mine Square Chest"         , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Never Land Rainbow Falls: Base Rainbow Sticker"            , player).access_rule = lambda state: state.has("High Jump", player) and state.has("Sliding Dash", player)
        multiworld.get_location("(T) Never Land Cliff Path Mega-Potion Chest"                   , player).access_rule = lambda state: state.has("Air Slide", player) and state.has("Sliding Dash", player)
        multiworld.get_location("(T) Never Land Skull Rock: Cavern Megalixir Chest"             , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Never Land Skull Rock: Entrance Chip Sticker"              , player).access_rule = lambda state: state.has("High Jump", player) and (state.has("Sliding Dash", player) or state.has("Air Slide", player))
        multiworld.get_location("(T) Never Land Skull Rock: Cavern Ars Solum Chest"             , player).access_rule = lambda state: state.has("High Jump", player) and (state.has("Sliding Dash", player) or state.has("Air Slide", player))
        multiworld.get_location("(T) Never Land Skull Rock: Cavern Chaos Crystal Chest"         , player).access_rule = lambda state: state.has("High Jump", player) and (state.has("Sliding Dash", player) or state.has("Air Slide", player))
        multiworld.get_location("(T) Disney Town Gizmo Gallery Absolute Zero Chest"             , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Gizmo Gallery Mega-Potion Chest"               , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Gizmo Gallery Chaos Crystal Chest"             , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Gizmo Gallery Action Recipe Chest"             , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Gizmo Gallery Panacea Chest"                   , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Gizmo Gallery Pete Sticker"                    , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Pete's Rec Room Zero Gravira Chest"            , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Pete's Rec Room Chaos Crystal Chest"           , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Pete's Rec Room Aerial Slam Chest"             , player).access_rule = lambda state: (state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)) and state.has("Air Slide", player)
        multiworld.get_location("(T) Disney Town Pete's Rec Room Break Time Chest"              , player).access_rule = lambda state: (state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)) and state.has("Air Slide", player)
        multiworld.get_location("(T) Disney Town Raceway Slot Edge Chest"                       , player).access_rule = lambda state: state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)
        multiworld.get_location("(T) Disney Town Raceway Traffic Cone Sticker"                  , player).access_rule = lambda state: (state.has("Thunder", player) or state.has("Thundara", player) or state.has("Thundaga", player)) and state.has("High Jump", player) and state.has("Air Slide", player) and state.has("Sliding Dash", player)
        multiworld.get_location("(T) The Keyblade Graveyard Twister Trench Traffic Cone Sticker", player).access_rule = lambda state: state.has("High Jump", player)
    
    # Region rules.
    multiworld.get_entrance("Dwarf Woodlands"                                                   , player).access_rule = lambda state: state.has("Dwarf Woodlands",      player)
    multiworld.get_entrance("Castle of Dreams"                                                  , player).access_rule = lambda state: state.has("Castle of Dreams",     player)
    multiworld.get_entrance("Enchanted Dominion"                                                , player).access_rule = lambda state: state.has("Enchanted Dominion",   player)
    multiworld.get_entrance("The Mysterious Tower"                                              , player).access_rule = lambda state: state.has("The Mysterious Tower", player)
    multiworld.get_entrance("Radiant Garden"                                                    , player).access_rule = lambda state: state.has("Radiant Garden",       player)
    multiworld.get_entrance("Olympus Coliseum"                                                  , player).access_rule = lambda state: state.has("Olympus Coliseum",     player)
    multiworld.get_entrance("Deep Space"                                                        , player).access_rule = lambda state: state.has("Deep Space",           player)
   #multiworld.get_entrance("Destiny Islands"                                                   , player).access_rule = lambda state: state.has("Destiny Islands",      player)
    multiworld.get_entrance("Never Land"                                                        , player).access_rule = lambda state: state.has("Never Land",           player)
    multiworld.get_entrance("Disney Town"                                                       , player).access_rule = lambda state: state.has("Disney Town",          player)
    multiworld.get_entrance("The Keyblade Graveyard"                                            , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
    multiworld.get_entrance("Realm of Darkness"                                                 , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player) and state.has("Realm of Darkness", player)

    # Win condition.
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
    