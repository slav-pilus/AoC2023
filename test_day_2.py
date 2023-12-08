import unittest

from day_2 import get_possible_games

GAME_1 = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
GAME_2 = "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"
GAME_3 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
GAME_4 = "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
GAME_5 = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"


class TestPossibleGame(unittest.TestCase):

    def test_get_possible_games_possible_game(self):
        games = [GAME_2]
        expected_result = 2

        actual_result = get_possible_games(games)

        self.assertEqual(actual_result, expected_result)

    def test_get_possible_games_impossible_game(self):
        games = [GAME_4]
        expected_result = 0

        actual_result = get_possible_games(games)

        self.assertEqual(actual_result, expected_result)

    def test_get_possible_games(self):
        games = [GAME_1, GAME_2, GAME_3, GAME_4, GAME_5]
        expected_result = 8

        actual_result = get_possible_games(games)

        self.assertEqual(actual_result, expected_result)

    def test_get_possible_games_empty_input(self):
        games = []
        expected_result = 0

        actual_result = get_possible_games(games)

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
