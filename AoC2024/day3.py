from dataloader import get_input_data
import re


def main():
    data = get_input_data(3)
    print(
        sum([int(p1) * int(p2) for p1, p2 in re.findall(r'mul\((\d+),(\d+)\)', data)])
    )

    do = True
    acc = 0
    for expr, p1, p2 in re.findall(r'(don\'t\(\)|do\(\)|mul\((\d+),(\d+)\))', data):
        match expr, p1, p2:
            case 'do()', _, _:
                do = True
            case "don't()", _, _:
                do = False
            case _, p1, p2 if do:
                acc += int(p1) * int(p2)

    print(acc)


if __name__ == '__main__':
    main()
