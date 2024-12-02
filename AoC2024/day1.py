from dataloader import get_input_data


def parser(data: str) -> tuple[list[int], list[int]]:
    col1, col2 = [], []
    for line in data.splitlines():
        x, y = line.strip().split()
        col1.append(int(x))
        col2.append(int(y))
    return col1, col2


def main():
    col1, col2 = get_input_data(1, parser=parser)
    col1 = sorted(col1)
    col2 = sorted(col2)
    print(sum([abs(x - y) for x, y in zip(col1, col2)]))
    s1 = set()
    for i in range(len(col1)):
        s1.add((col1[i], col2.count(col1[i])))
    print(sum(x * y for x, y in s1))


if __name__ == '__main__':
    main()
