from BaseClasses import CollectionState, MultiWorld

WORLDS = [
    "Dwarf Woodlands",
    "Castle of Dreams",
    "Enchanted Dominion",
    "The Mysterious Tower",
    "Radiant Garden",
    "Mirage Arena",
    "Olympus Coliseum",
    "Deep Space",
    "Realm of Darkness",
    "Never Land",
    "Disney Town"]

def can_glide(state, player):
    return state.has("Glide", player) or state.has("Superglide", player) or state.has("Fire Glide", player)

def can_airslide(state, player):
    return state.has("Air Slide", player) or state.has("Ice Slide", player)

def has_x_worlds(state, player, num_of_worlds):
    return state.has_from_list_unique(WORLDS, player, num_of_worlds)

def set_rules(khbbsworld):
    multiworld = khbbsworld.multiworld
    player     = khbbsworld.player
    options    = khbbsworld.options
    # Location Rules
    if options.character == 2:
        multiworld.get_location("(T) The Land of Departure Defeat Eraqus Max HP Increase"        , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(T) The Land of Departure Defeat Eraqus Chaos Ripper"           , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(T) The Land of Departure Defeat Eraqus Xehanort's Report 8"    , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(T) Dwarf Woodlands Vault Flame Salvo Chest"                    , player).access_rule = lambda state: state.has("High Jump", player) or can_airslide(state, player)
        multiworld.get_location("(T) Castle of Dreams Passage Flying Balloon Sticker"            , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Radiant Garden Fountain Court Dale Sticker"                 , player).access_rule = lambda state: state.has("High Jump", player) and can_airslide(state, player)
        multiworld.get_location("(T) Radiant Garden Outer Gardens Airplane Sticker"              , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Olympus Coliseum Coliseum Gates Balloon Sticker"            , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Never Land Rainbow Falls: Base Rainbow Sticker"             , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Never Land Cliff Path Mega-Potion Chest"                    , player).access_rule = lambda state: can_airslide(state, player)
        multiworld.get_location("(T) Never Land Skull Rock: Cavern Megalixir Chest"              , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(T) Never Land Skull Rock: Entrance Chip Sticker"               , player).access_rule = lambda state: state.has("High Jump", player) and can_airslide(state, player)
        multiworld.get_location("(T) Never Land Skull Rock: Cavern Ars Solum Chest"              , player).access_rule = lambda state: state.has("High Jump", player) and can_airslide(state, player)
        multiworld.get_location("(T) Never Land Skull Rock: Cavern Chaos Crystal Chest"          , player).access_rule = lambda state: state.has("High Jump", player) and can_airslide(state, player)
        multiworld.get_location("(T) Disney Town Pete's Rec Room Aerial Slam Chest"              , player).access_rule = lambda state: can_airslide(state, player)
        multiworld.get_location("(T) Disney Town Pete's Rec Room Break Time Chest"               , player).access_rule = lambda state: can_airslide(state, player)
        multiworld.get_location("(T) Disney Town Raceway Traffic Cone Sticker"                   , player).access_rule = lambda state: state.has("High Jump", player) and can_airslide(state, player)
        multiworld.get_location("(T) The Keyblade Graveyard Twister Trench Traffic Cone Sticker" , player).access_rule = lambda state: state.has("High Jump", player)
        if options.mirage_arena:
            if options.command_board:
                multiworld.get_location("(T) Mirage Arena Win a Command Board game"              , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(T) Mirage Arena Win 3 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(T) Mirage Arena Win 5 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(T) Mirage Arena Win 7 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
            if options.super_bosses:
                multiworld.get_location("(T) Mirage Arena Villains' Vendetta Ultima Weapon"      , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(T) Mirage Arena Complete Villains' Vendetta"           , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(T) Mirage Arena Light's Lessons Max HP Increase"       , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(T) Mirage Arena Complete Light's Lessons"              , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(T) Mirage Arena Peering into Darkness Royal Radiance"  , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(T) Mirage Arena Complete Peering into Darkness"        , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
            multiworld.get_location("(T) Mirage Arena Complete Day of Reckoning"                 , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(T) Mirage Arena Complete Wheels of Misfortune"             , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(T) Mirage Arena Complete Risky Riches"                     , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(T) Mirage Arena Weaver Fever Max HP Increase"              , player).access_rule = lambda state: state.has_x_worlds(state, player, 4) and state.has("Enchanted Dominion", player)
            multiworld.get_location("(T) Mirage Arena Complete Weaver Fever"                     , player).access_rule = lambda state: state.has_x_worlds(state, player, 4) and state.has("Enchanted Dominion", player)
            multiworld.get_location("(T) Mirage Arena Sinister Sentinel Xehanort's Report 5"     , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(T) Mirage Arena Complete Sinister Sentinel"                , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(T) Mirage Arena Dead Ringer Darkgnaw"                      , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(T) Mirage Arena Complete Dead Ringer"                      , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(T) Mirage Arena Complete Combined Threat"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 6) and state.has("Radiant Garden", player)
            multiworld.get_location("(T) Mirage Arena Complete Treasure Tussle"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 6)
            multiworld.get_location("(T) Mirage Arena Complete Harsh Punishment"                 , player).access_rule = lambda state: state.has_x_worlds(state, player, 6)
            multiworld.get_location("(T) Mirage Arena Complete A Time to Chill"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Olympus Coliseum", player)
            multiworld.get_location("(T) Mirage Arena Copycat Crisis Max HP Increase"            , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(T) Mirage Arena Complete Copycat Crisis"                   , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(T) Mirage Arena Keepers of the Arena Ultima Cannon"        , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(T) Mirage Arena Complete Keepers of the Arena"             , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(T) Mirage Arena Monster of the Sea Mini"                   , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Disney Town", player)
            multiworld.get_location("(T) Mirage Arena Complete Monster of the Sea"               , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Disney Town", player)
            multiworld.get_location("(T) Mirage Arena Country Chase: Finish 5 laps in 2:30"          , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(T) Mirage Arena Disney Drive: Finish 5 laps in 5 minutes"      , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(T) Mirage Arena Grand Spree: Finish 5 laps in 5 minutes"       , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(T) Mirage Arena Castle Circuit: Finish 5 laps in 5:30"         , player).access_rule = lambda state: state.has("Disney Town", player)
        if options.super_bosses:
            multiworld.get_location("(T) The Land of Departure Defeat Unknown No Name"           , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
            multiworld.get_location("(T) The Keyblade Graveyard Defeat Vanitas Remnant Void Gear", player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
    if options.character == 1:
        multiworld.get_location("(A) The Land of Departure World Sealed Brightcrest"             , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(A) Dwarf Woodlands Vault Magnet Chest"                         , player).access_rule = lambda state: state.has("High Jump", player) or state.has("Doubleflight", player)
        multiworld.get_location("(A) Dwarf Woodlands Vault Bubble Sticker"                       , player).access_rule = lambda state: state.has("High Jump", player) and state.has("Doubleflight", player)
        multiworld.get_location("(A) Enchanted Dominion Dungeon Horace Sticker"                  , player).access_rule = lambda state: state.has("High Jump", player) or state.has("Doubleflight", player)
        multiworld.get_location("(A) Radiant Garden Front Doors Juice Sticker"                   , player).access_rule = lambda state: state.has("High Jump", player) or state.has("Doubleflight", player)
        multiworld.get_location("(A) Radiant Garden Aqueduct Donut Sticker"                      , player).access_rule = lambda state: state.has("High Jump", player) or state.has("Doubleflight", player)
        multiworld.get_location("(A) Radiant Garden Defeat Final Terra-Xehanort II"              , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
        multiworld.get_location("(A) Olympus Coliseum Coliseum Gates Fireworks Sticker"          , player).access_rule = lambda state: state.has("High Jump", player) or (can_airslide(state, player) or state.has("Doubleflight", player))
        multiworld.get_location("(A) Never Land Mermaid Lagoon Rainbow Sticker"                  , player).access_rule = lambda state: can_airslide(state, player)
        multiworld.get_location("(A) Never Land Jungle Clearing Fireworks Sticker"               , player).access_rule = lambda state: state.has("Doubleflight", player)
        multiworld.get_location("(A) Disney Town Raceway Daisy Sticker"                          , player).access_rule = lambda state: can_airslide(state, player)
        multiworld.get_location("(A) Disney Town Main Plaza Minnie Sticker"                      , player).access_rule = lambda state: state.has("High Jump", player) and state.has("Doubleflight", player)
        multiworld.get_location("(A) The Keyblade Graveyard Seat of War Flower Sticker"          , player).access_rule = lambda state: state.has("Doubleflight", player)
        multiworld.get_location("(A) The Keyblade Graveyard Fissure Bubble Sticker"              , player).access_rule = lambda state: state.has("High Jump", player) and state.has("Doubleflight", player)
        multiworld.get_location("(A) Mirage Arena Wheels of Misfortune Max HP Increase"          , player).access_rule = lambda state: state.has("Castle of Dreams", player)
        multiworld.get_location("(A) Mirage Arena Complete Wheels of Misfortune"                 , player).access_rule = lambda state: state.has("Castle of Dreams", player)
        multiworld.get_location("(A) Mirage Arena Combined Threat Sky Climber"                   , player).access_rule = lambda state: state.has("Radiant Garden", player)
        multiworld.get_location("(A) Mirage Arena Complete Combined Threat"                      , player).access_rule = lambda state: state.has("Radiant Garden", player)
        multiworld.get_location("(A) Mirage Arena A Time to Chill Max HP Increase"               , player).access_rule = lambda state: state.has("Olympus Coliseum", player)
        multiworld.get_location("(A) Mirage Arena Complete A Time to Chill"                      , player).access_rule = lambda state: state.has("Olympus Coliseum", player)
        multiworld.get_location("(A) Mirage Arena Country Chase: Finish 5 laps in 2:30"          , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(A) Mirage Arena Disney Drive: Finish 5 laps in 5 minutes"      , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(A) Mirage Arena Grand Spree: Finish 5 laps in 5 minutes"       , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(A) Mirage Arena Castle Circuit: Finish 5 laps in 5:30"         , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(A) Mirage Arena Monster of the Sea Mini"                       , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(A) Mirage Arena Complete Monster of the Sea"                   , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(A) Mirage Arena Villains' Vendetta Ultima Weapon"              , player).access_rule = lambda state: state.has("Disney Town", player) and state.has_group_unique("Command Board", player, 1) and state.has("Castle of Dreams", player) or state.has("Radiant Garden", player) or state.has("Olympus Coliseum")
        multiworld.get_location("(A) Mirage Arena Complete Villains' Vendetta"                   , player).access_rule = lambda state: state.has("Disney Town", player) and state.has_group_unique("Command Board", player, 1) and state.has("Castle of Dreams", player) or state.has("Radiant Garden", player) or state.has("Olympus Coliseum")
        multiworld.get_location("(A) Mirage Arena Light's Lessons Max HP Increase"               , player).access_rule = lambda state: state.has_all("Castle of Dreams", "Radiant Garden", "Olympus Coliseum", "Disney Town", player) and state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(A) Mirage Arena Complete Light's Lessons"                      , player).access_rule = lambda state: state.has_all("Castle of Dreams", "Radiant Garden", "Olympus Coliseum", "Disney Town", player) and state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(A) Mirage Arena Win a Command Board game"                      , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(A) Mirage Arena Win 3 Command Board games"                     , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(A) Mirage Arena Win 5 Command Board games"                     , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(A) Mirage Arena Win 7 Command Board games"                     , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(A) Mirage Arena Peering into Darkness Royal Radiance"          , player).access_rule = lambda state: state.has_all("Castle of Dreams", "Radiant Garden", "Olympus Coliseum", "Disney Town", player) and state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(A) Mirage Arena Complete Peering into Darkness"                , player).access_rule = lambda state: state.has_all("Castle of Dreams", "Radiant Garden", "Olympus Coliseum", "Disney Town", player) and state.has_group_unique("Command Board", player, 1)
        if options.mirage_arena:
            if options.command_board:
                multiworld.get_location("(A) Mirage Arena Win a Command Board game"              , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(A) Mirage Arena Win 3 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(A) Mirage Arena Win 5 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(A) Mirage Arena Win 7 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
            if options.super_bosses:
                multiworld.get_location("(A) Mirage Arena Villains' Vendetta Ultima Weapon"      , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(A) Mirage Arena Complete Villains' Vendetta"           , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(A) Mirage Arena Light's Lessons Max HP Increase"       , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(A) Mirage Arena Complete Light's Lessons"              , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(A) Mirage Arena Peering into Darkness Royal Radiance"  , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(A) Mirage Arena Complete Peering into Darkness"        , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
            multiworld.get_location("(A) Mirage Arena Complete Day of Reckoning"                 , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(A) Mirage Arena Complete Wheels of Misfortune"             , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(A) Mirage Arena Complete Risky Riches"                     , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(A) Mirage Arena Weaver Fever Max HP Increase"              , player).access_rule = lambda state: state.has_x_worlds(state, player, 4) and state.has("Enchanted Dominion", player)
            multiworld.get_location("(A) Mirage Arena Complete Weaver Fever"                     , player).access_rule = lambda state: state.has_x_worlds(state, player, 4) and state.has("Enchanted Dominion", player)
            multiworld.get_location("(A) Mirage Arena Sinister Sentinel Xehanort's Report 5"     , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(A) Mirage Arena Complete Sinister Sentinel"                , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(A) Mirage Arena Dead Ringer Darkgnaw"                      , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(A) Mirage Arena Complete Dead Ringer"                      , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(A) Mirage Arena Complete Combined Threat"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 6) and state.has("Radiant Garden", player)
            multiworld.get_location("(A) Mirage Arena Complete Treasure Tussle"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 6)
            multiworld.get_location("(A) Mirage Arena Complete Harsh Punishment"                 , player).access_rule = lambda state: state.has_x_worlds(state, player, 6)
            multiworld.get_location("(A) Mirage Arena Complete A Time to Chill"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Olympus Coliseum", player)
            multiworld.get_location("(A) Mirage Arena Copycat Crisis Max HP Increase"            , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(A) Mirage Arena Complete Copycat Crisis"                   , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(A) Mirage Arena Keepers of the Arena Ultima Cannon"        , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(A) Mirage Arena Complete Keepers of the Arena"             , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(A) Mirage Arena Monster of the Sea Mini"                   , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Disney Town", player)
            multiworld.get_location("(A) Mirage Arena Complete Monster of the Sea"               , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Disney Town", player)
            multiworld.get_location("(A) Mirage Arena Country Chase: Finish 5 laps in 2:30"          , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(A) Mirage Arena Disney Drive: Finish 5 laps in 5 minutes"      , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(A) Mirage Arena Grand Spree: Finish 5 laps in 5 minutes"       , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(A) Mirage Arena Castle Circuit: Finish 5 laps in 5:30"         , player).access_rule = lambda state: state.has("Disney Town", player)
        if options.super_bosses:
            multiworld.get_location("(A) The Land of Departure Defeat Unknown No Name"           , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
            multiworld.get_location("(A) The Keyblade Graveyard Defeat Vanitas Remnant Void Gear", player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
    if options.character == 0:
        multiworld.get_location("(V) Enchanted Dominion Audience Chamber Dewey Sticker"          , player).access_rule = lambda state: state.has("High Jump", player) and can_glide(state, player)
        multiworld.get_location("(V) Radiant Garden Front Doors Fireworks Sticker"               , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(V) Never Land Rainbow Falls: Base Rainbow Sticker"             , player).access_rule = lambda state: state.has("High Jump", player) and can_glide(state, player)
        multiworld.get_location("(V) Disney Town Raceway Superglide Chest"                       , player).access_rule = lambda state: can_glide(state, player)
        multiworld.get_location("(V) The Keyblade Graveyard Seat of War Ice Cream Sticker"       , player).access_rule = lambda state: state.has("High Jump", player)
        multiworld.get_location("(V) Mirage Arena Complete Combined Threat"                      , player).access_rule = lambda state: state.has("Radiant Garden", player)
        multiworld.get_location("(V) Mirage Arena Country Chase: Finish 5 laps in 2:30"          , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(V) Mirage Arena Disney Drive: Finish 5 laps in 5 minutes"      , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(V) Mirage Arena Grand Spree: Finish 5 laps in 5 minutes"       , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(V) Mirage Arena Castle Circuit: Finish 5 laps in 5:30"         , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(V) Mirage Arena Monster of the Sea Mini"                       , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(V) Mirage Arena Complete Monster of the Sea"                   , player).access_rule = lambda state: state.has("Disney Town", player)
        multiworld.get_location("(V) Mirage Arena Win a Command Board game"                      , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(V) Mirage Arena Win 3 Command Board games"                     , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(V) Mirage Arena Win 5 Command Board games"                     , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        multiworld.get_location("(V) Mirage Arena Win 7 Command Board games"                     , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
        if options.mirage_arena:
            if options.command_board:
                multiworld.get_location("(V) Mirage Arena Win a Command Board game"              , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(V) Mirage Arena Win 3 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(V) Mirage Arena Win 5 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
                multiworld.get_location("(V) Mirage Arena Win 7 Command Board games"             , player).access_rule = lambda state: state.has_group_unique("Command Board", player, 1)
            if options.super_bosses:
                multiworld.get_location("(V) Mirage Arena Villains' Vendetta Ultima Weapon"      , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(V) Mirage Arena Complete Villains' Vendetta"           , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(V) Mirage Arena Light's Lessons Max HP Increase"       , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(V) Mirage Arena Complete Light's Lessons"              , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(V) Mirage Arena Peering into Darkness Royal Radiance"  , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
                multiworld.get_location("(V) Mirage Arena Complete Peering into Darkness"        , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
            multiworld.get_location("(V) Mirage Arena Complete Day of Reckoning"                 , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(V) Mirage Arena Complete Wheels of Misfortune"             , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(V) Mirage Arena Complete Risky Riches"                     , player).access_rule = lambda state: state.has_x_worlds(state, player, 2)
            multiworld.get_location("(V) Mirage Arena Weaver Fever Max HP Increase"              , player).access_rule = lambda state: state.has_x_worlds(state, player, 4) and state.has("Enchanted Dominion", player)
            multiworld.get_location("(V) Mirage Arena Complete Weaver Fever"                     , player).access_rule = lambda state: state.has_x_worlds(state, player, 4) and state.has("Enchanted Dominion", player)
            multiworld.get_location("(V) Mirage Arena Sinister Sentinel Xehanort's Report 5"     , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(V) Mirage Arena Complete Sinister Sentinel"                , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(V) Mirage Arena Dead Ringer Darkgnaw"                      , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(V) Mirage Arena Complete Dead Ringer"                      , player).access_rule = lambda state: state.has_x_worlds(state, player, 4)
            multiworld.get_location("(V) Mirage Arena Complete Combined Threat"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 6) and state.has("Radiant Garden", player)
            multiworld.get_location("(V) Mirage Arena Complete Treasure Tussle"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 6)
            multiworld.get_location("(V) Mirage Arena Complete Harsh Punishment"                 , player).access_rule = lambda state: state.has_x_worlds(state, player, 6)
            multiworld.get_location("(V) Mirage Arena Complete A Time to Chill"                  , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Olympus Coliseum", player)
            multiworld.get_location("(V) Mirage Arena Copycat Crisis Max HP Increase"            , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(V) Mirage Arena Complete Copycat Crisis"                   , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(V) Mirage Arena Keepers of the Arena Ultima Cannon"        , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(V) Mirage Arena Complete Keepers of the Arena"             , player).access_rule = lambda state: state.has_x_worlds(state, player, 8)
            multiworld.get_location("(V) Mirage Arena Monster of the Sea Mini"                   , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Disney Town", player)
            multiworld.get_location("(V) Mirage Arena Complete Monster of the Sea"               , player).access_rule = lambda state: state.has_x_worlds(state, player, 8) and state.has("Disney Town", player)
            multiworld.get_location("(V) Mirage Arena Country Chase: Finish 5 laps in 2:30"          , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(V) Mirage Arena Disney Drive: Finish 5 laps in 5 minutes"      , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(V) Mirage Arena Grand Spree: Finish 5 laps in 5 minutes"       , player).access_rule = lambda state: state.has("Disney Town", player)
            multiworld.get_location("(V) Mirage Arena Castle Circuit: Finish 5 laps in 5:30"         , player).access_rule = lambda state: state.has("Disney Town", player)
        if options.super_bosses:
            multiworld.get_location("(V) The Land of Departure Defeat Unknown No Name"           , player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
            multiworld.get_location("(V) The Keyblade Graveyard Defeat Vanitas Remnant Void Gear", player).access_rule = lambda state: state.has_x_worlds(state, player, 10)
        
    
    # Region rules.
    multiworld.get_entrance("Dwarf Woodlands"                                                    , player).access_rule = lambda state: state.has("Dwarf Woodlands",      player)
    multiworld.get_entrance("Castle of Dreams"                                                   , player).access_rule = lambda state: state.has("Castle of Dreams",     player)
    multiworld.get_entrance("Enchanted Dominion"                                                 , player).access_rule = lambda state: state.has("Enchanted Dominion",   player)
    multiworld.get_entrance("The Mysterious Tower"                                               , player).access_rule = lambda state: state.has("The Mysterious Tower", player)
    multiworld.get_entrance("Radiant Garden"                                                     , player).access_rule = lambda state: state.has("Radiant Garden",       player)
    multiworld.get_entrance("Olympus Coliseum"                                                   , player).access_rule = lambda state: state.has("Olympus Coliseum",     player)
    multiworld.get_entrance("Deep Space"                                                         , player).access_rule = lambda state: state.has("Deep Space",           player)
   #multiworld.get_entrance("Destiny Islands"                                                    , player).access_rule = lambda state: state.has("Destiny Islands",      player)
    multiworld.get_entrance("Never Land"                                                         , player).access_rule = lambda state: state.has("Never Land",           player)
    multiworld.get_entrance("Disney Town"                                                        , player).access_rule = lambda state: state.has("Disney Town",          player)
    multiworld.get_entrance("Mirage Arena"                                                       , player).access_rule = lambda state: state.has("Mirage Arena",         player)
    multiworld.get_entrance("The Keyblade Graveyard"                                             , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra"}, player)
    multiworld.get_entrance("Realm of Darkness"                                                  , player).access_rule = lambda state: state.has_all({"Wayfinder Ventus", "Wayfinder Aqua", "Wayfinder Terra", "Realm of Darkness"}, player)

    # Win condition.
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
    