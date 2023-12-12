# test_day_3.py

import unittest

import day_3


class TestDay3(unittest.TestCase):

    def test_find_all_parts_two_lines_with_special_character6(self):
        lines = ['467..114..',
                 '...*......',
                 '..35..633.',
                 '......#...',
                 '617*......',
                 '.....+.58.',
                 '..592.....',
                 '......755.',
                 '...$.*....',
                 '.664.598..']
        expected_result = 4361

        actual_result = day_3.find_all_parts(lines)
        sum = 0;
        for i in actual_result:
            sum += int(i)

        self.assertEqual(expected_result, sum)

    def test_find_all_parts_two_lines_with_special_character5(self):
        lines = ['467..114..',
                 '...*......']
        expected_result = 467

        actual_result = day_3.find_all_parts(lines)
        sum = 0;
        for i in actual_result:
            sum += int(i)

        self.assertEqual(expected_result, sum)

    def test_find_all_parts_two_lines_with_special_characters_reverse_4(self):
        lines = [".1234.",
                 ".....$"]

        expected_result = ['1234']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_two_lines_with_special_characters4(self):
        lines = [".....$",
                 ".1234"]
        expected_result = ['1234']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_two_lines_with_special_characters3(self):
        lines = ["$....-",
                 ".3...9"]
        expected_result = ['3', '9']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_two_lines_with_special_characters2(self):
        lines = ["$.",
                 ".3"]
        expected_result = ['3']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_two_lines_with_special_characters(self):
        lines = [".$",
                 "2."]
        expected_result = ['2']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_two_lines_with_one_special_characters(self):
        lines = ["$",
                 "1"]
        expected_result = ['1']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_single_line_with_all_special_characters(self):
        lines = ["1#.2%.*3."]
        expected_result = ['1', '2', '3']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_single_line_with_multiple_parts(self):
        lines = [".12+..467+..+114.."]
        expected_result = ['12', '467', '114']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_single_line_with_single_part(self):
        lines = ["467+..114.."]
        expected_result = ['467']

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(expected_result, actual_result)

    def test_find_all_parts_single_line_with_no_parts(self):
        lines = ["467..114.."]
        expected_result = []

        actual_result = day_3.find_all_parts(lines)

        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
