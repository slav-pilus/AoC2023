from utils import read_file


def get_winning_numbers(line):
    temp = line.split("|")
    temp = temp[0].split(":")
    temp = temp[1].split(" ")
    winnings = {int(el): 0 for el in temp if len(el) > 0}

    # print(winnings)
    return winnings


def check_winnings(winnings, line):
    temp = line.split("|")
    temp = temp[1].split(" ")
    for number in temp:
        if len(number.strip()) > 0:
            my_num = int(number.strip())
            if my_num in winnings:
                winnings[my_num] += 1

    return winnings


def get_winnings(line):
    winnings = get_winning_numbers(line)
    check_winnings(winnings, line)

    no_of_matched = len([v for v in winnings.values() if v > 0])

    points = 0
    for i in range(1, no_of_matched + 1):
        if i == 1:
            points = 1
        else:
            points *= 2

    return points


def main():
    lines = read_file('./data/day4_input.txt')

    answer = 0
    for line in lines:
        answer += get_winnings(line)

    print(answer)


if __name__ == '__main__':
    main()
