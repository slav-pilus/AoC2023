from unittest import TestCase

from day_1 import get_calibration_value_with_strings


class Test(TestCase):
    def test_main(self):
        # test get_calibration_value
        self.assertEqual(get_calibration_value_with_strings('abc123'), '13')
        self.assertEqual(get_calibration_value_with_strings('one2one'), '11')
        self.assertEqual(get_calibration_value_with_strings('two1nine'), '29')
        self.assertEqual(get_calibration_value_with_strings('eightwothree'), '83')
        self.assertEqual(get_calibration_value_with_strings('abcone2threexyz'), '13')
        self.assertEqual(get_calibration_value_with_strings('xtwone3four'), '24')
        self.assertEqual(get_calibration_value_with_strings('4nineeightseven2'), '42')
        self.assertEqual(get_calibration_value_with_strings('zoneight234'), '14')
        self.assertEqual(get_calibration_value_with_strings('7pqrstsixteen'), '76')
        self.assertEqual(get_calibration_value_with_strings('1abc2'), '12')
        self.assertEqual(get_calibration_value_with_strings('pqr3stu8vwx'), '38')
        self.assertEqual(get_calibration_value_with_strings('a1b2c3d4e5f'), '15')
        self.assertEqual(get_calibration_value_with_strings('treb7uchet'), '77')
        self.assertEqual(get_calibration_value_with_strings('eighthree'), '83')
        self.assertEqual(get_calibration_value_with_strings('sevenine'), '79')
        self.assertEqual(get_calibration_value_with_strings('oneight'), '11')