import unittest
from unittest.mock import patch, mock_open
from day_4 import get_winnings, main


class TestDay4(unittest.TestCase):

    def test_get_winnings(self):
        self.assertEqual(8, get_winnings("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"))

    @patch('day_4.read_file', return_value=[
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_read_file):
        main()

        # check if the read_file function was called with correct parameter
        mock_read_file.assert_called_once_with('./data/day4_input.txt')

        # check if print function was called with correct parameter
        mock_print.assert_called_once_with(13)


if __name__ == '__main__':
    unittest.main()
