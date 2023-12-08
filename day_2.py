from utils import read_file

limits = {
    'green': 13,
    'blue': 14,
    'red': 12
}


def build_colors(color_groups):
    result = []
    for item in color_groups:
        key_value = item.strip().split(" ")
        key_value = [elem.strip(',') for elem in key_value]
        result.append({key_value[i + 1]: int(key_value[i]) for i in range(0, len(key_value), 2)})
    return result


def get_game_id(game_id):
    return int(game_id.split()[-1])


def build_game(game):
    game_id_tmp, color_data = game.split(":")
    game_id = get_game_id(game_id_tmp)

    color_groups = color_data.split(";")
    color_groups = build_colors(color_groups)

    game_object = {game_id: color_groups}
    return game_object


def is_game_possible(game):
    for k, v in game.items():
        for dictionary in v:
            for color, num in dictionary.items():
                if num > limits[color]:
                    return False
    return True


def get_possible_games(games):
    possible_games = []
    for game in games:
        g = build_game(game)
        if is_game_possible(g):
            possible_games.append(g.keys())

    return sum_game_ids(possible_games)


def sum_game_ids(possible_games):
    total = 0
    for dictionary in possible_games:
        for key in dictionary:
            total += key

    return total


def main():
    games = read_file('./data/day2_input.txt')

    possible = get_possible_games(games)
    print(possible)


if __name__ == '__main__':
    main()
