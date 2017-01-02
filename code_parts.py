
code_parts = [
    "pirate, treasure, script = get_board_status(game)\n"
    "locations = assign_targets(game, pirate, treasure, script)\n"
    "if try_bermuda(game, pirate):\n"
    "    return\n"
    "game.set_sail(pirate, locations[0])\n",

    "pirate, treasure, script = get_board_status(game)\n"
    "locations = assign_targets(game, pirate, treasure, script)\n"
    "if try_defend(game, pirate):\n"
    "    return\n"
    "game.set_sail(pirate, locations[0])\n",

    "pirate, treasure, script = get_board_status(game)\n"
    "locations = assign_targets(game, pirate, treasure, script)\n"
    "if try_attack(game, pirate):\n"
    "    return\n"
    "game.set_sail(pirate, locations[0])\n"]


def get_board_status(game):
    pirate = game.my_pirates()[0]
    game.debug("pirate: " + str(pirate.id))
    treasure = game.treasures()[-1]
    game.debug("treasure: " + str(treasure.id))
    script = get_available_script(game)
    return pirate, treasure, script


def assign_targets(game, pirate, treasure, script):
    moves = game.get_actions_per_turn()
    if script is not None:
        destination = script.location
    elif not pirate.has_treasure:
        destination = treasure.location
    else:
        moves = 1
        destination = pirate.initial_loc
    locations = game.get_sail_options(pirate, destination, moves)
    locations = get_safe_locations(game, locations)
    return locations


def take_action(game, pirate, locations):
    if try_bermuda(game, pirate):
        return
    if try_defend(game, pirate):
        return
    if try_attack(game, pirate):
        return
    game.set_sail(pirate, locations[0])


def try_defend(game, pirate):
    for enemy in game.enemy_pirates():
        if game.in_range(pirate, enemy):
            game.defend(pirate)
            return True
    return False


def try_attack(game, pirate):
    for enemy in game.enemy_pirates():
        if game.in_range(pirate, enemy):
            game.attack(pirate, enemy)
            return True
    return False


def try_bermuda(game, pirate):
    if game.get_my_bermuda_zone() is None and game.get_my_scripts_num() >= game.get_required_scripts_num():
        game.summon_bermuda_zone(pirate)
        return True
    return False


def get_safe_locations(game, locations):
    return [loc for loc in locations if not game.in_enemy_bermuda_zone(loc)]


def get_available_script(game):
    if len(game.scripts()) > 0:
        return game.scripts()[0]
    return None