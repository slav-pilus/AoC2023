from utils import read_file
import re

special_chars = r'[&$=%#@/+*-]'
numbers_pattern = r'\d+'


def check_lines(line, another_line):
    out = []
    result = re.finditer(numbers_pattern, line)
    for items_list in result:
        if re.search(special_chars, another_line[items_list.start() - 1:  items_list.end() + 1]):
            out.append(items_list.group())
        elif re.search(special_chars, another_line[items_list.start():  items_list.end() + 1]):
            out.append(items_list.group())
        elif re.search(special_chars, another_line[items_list.start() - 1:  items_list.end()]):
            out.append(items_list.group())

    return out


def find_parts(line, prev_line, next_line):
    parts = []

    parts.extend(check_lines(line, line))

    if len(prev_line) > 0:
        parts.extend(check_lines(line, prev_line))

    if len(next_line) > 0:
        parts.extend(check_lines(line, next_line))

    return parts


def remove_dots(lines):
    lines_no_dots = []
    for line in lines:
        lines_no_dots.append(line.replace('.', ' '))

    return lines_no_dots


def find_all_parts(lines):
    lines = remove_dots(lines)
    parts = []
    for i in range(len(lines)):
        prev_line = ''
        line = lines[i]
        next_line = ''

        if i > 0:  # not the first item
            prev_line = lines[i - 1]
        if i < len(lines) - 1:  # not the last item
            next_line = lines[i + 1]

        part_for_section = find_parts(line, prev_line, next_line)
        if part_for_section:
            parts.extend(part_for_section)

    return parts


def find_unique_chars(s):
    return set(s)


def main():
    lines = read_file('./data/day3_input.txt')
    unique_chars = set()
    for line in lines:
        unique_chars.update(find_unique_chars(line))

    for char in unique_chars:
        if not str(char).isdigit() or char.isalpha():
            print(char)

    parts = find_all_parts(lines)
    print(parts)

    answer = 0

    for part in parts:
        answer += int(part)

    print(answer)


if __name__ == '__main__':
    main()
