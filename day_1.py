import re

digits_as_string = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def read_file(file_path):
    with open(file_path) as f:
        list_of_lines = f.readlines()
    return list_of_lines


def get_calibration_value(line):
    digits = [c for i, c in enumerate(line) if c.isdigit()]
    first_digit = digits[0]
    last_digit = digits[len(digits) - 1]

    return first_digit + last_digit


def get_string_digit_location(line):
    locations = []
    for d in digits_as_string:
        if d in line:
            locations.append(line.index(d))

    if len(locations) == 0:
        return [-1, -1]

    locations.sort()

    return int(locations[0]), int(locations[len(locations) - 1])


def get_string_digits(line):
    values = []
    for d in digits_as_string:
        if d in line:
            values.append([m.start() for m in re.finditer(d, line)])

    return {line.index(d): i + 1 for i, d in enumerate(digits_as_string) if d in line}


def getFirstStringDigit(line):
    index = -1
    value = -1
    for d in digits_as_string:
        if d in line:
            if index == -1:
                index = line.index(d)
                value = digits_as_string.index(d) + 1

            if line.index(d) < index:
                index = line.index(d)
                value = digits_as_string.index(d) + 1

    return {index: value}


def get_last_string_digit(line):
    index = -1
    value = -1
    for d in digits_as_string:
        if d in line:
            current = [m.start() for m in re.finditer(d, line)]
            current.sort()
            if current[len(current) - 1] > index:
                index = current[len(current) - 1]
                value = digits_as_string.index(d) + 1

    return {index: value}


def get_calibration_value_with_strings(line):
    digits = [c for i, c in enumerate(line) if c.isdigit()]
    digits_locations = [i for i, c in enumerate(line) if c.isdigit()]

    first_string_digit = getFirstStringDigit(line)
    first_string_digit_location = list(first_string_digit.keys())[0]
    last_string_digit = get_last_string_digit(line)
    last_string_digit_location = list(last_string_digit.keys())[0]

    if len(digits) == 0:
        return str(list(first_string_digit.values())[0]) + str(list(last_string_digit.values())[0])

    first = int(digits[0])
    last = int(digits[len(digits) - 1])

    if int(list(first_string_digit.values())[0]) == -1:
        return str(digits[0]) + str(digits[len(digits) - 1])
    if digits_locations[0] > first_string_digit_location:
        first = int(list(first_string_digit.values())[0])
    if digits_locations[len(digits_locations) - 1] < last_string_digit_location:
        last = int(list(last_string_digit.values())[0])

    return str(first) + str(last)


def get_calibration_values(list_of_lines):
    sum_of_lines = 0
    for line in list_of_lines:
        sum_of_lines += int(get_calibration_value(line))

    return sum_of_lines


def get_calibration_values_with_strings(list_of_lines):
    sum_of_lines = 0
    for line in list_of_lines:
        sum_of_lines += int(get_calibration_value_with_strings(line))

    return sum_of_lines


def main():
    lines = read_file('./data/day1_input.txt')
    part_1 = get_calibration_values(lines)
    part_2 = get_calibration_values_with_strings(lines)
    #
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')



if __name__ == '__main__':
    main()
