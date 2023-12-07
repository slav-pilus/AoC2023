def read_file(file_path):
    with open(file_path) as f:
        list_of_lines = f.readlines()
    return list_of_lines


def get_calibration_value(line):
    digits = [c for i, c in enumerate(line) if c.isdigit()]
    first_digit = digits[0]
    last_digit = digits[len(digits) - 1]

    return first_digit + last_digit


def get_calibration_values(list_of_lines):
    sum_of_lines = 0
    for line in list_of_lines:
        sum_of_lines += int(get_calibration_value(line))

    return sum_of_lines


def main():
    lines = read_file('./data/day1_input.txt')
    part_1 = get_calibration_values(lines)

    print(f'Part 1: {part_1}')


if __name__ == '__main__':
    main()
