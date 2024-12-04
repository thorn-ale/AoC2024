from dataloader import get_input_data


def count_func(data: list[str], target: str) -> int:
    return sum([line.count(target) + line[::-1].count(target) for line in data])


def cols(data: list[str]) -> list[str]:
    w = len(data)
    return [''.join([data[j][i] for j in range(w)]) for i in range(w)]


def diags1(data: list[str]) -> list[str]:
    w = len(data)
    return [
        ''.join([data[r][c] for r, c in zip(range(k + 1), reversed(range(k + 1)))])
        for k in range(w)
    ] + [
        ''.join([data[r][c] for r, c in zip(range(k, w), reversed(range(w)))])
        for k in range(1, w)
    ]


def diags2(data: list[str]) -> list[str]:
    w = len(data)
    return [
        ''.join([data[r][c] for r, c in zip(range(abs(k - w)), range(k, w))])
        for k in reversed(range(w))
    ] + [
        ''.join([data[r][c] for r, c in zip(range(k, w), range(abs(k - w)))])
        for k in range(1, w)
    ]


def count_patterns(data: list[str]) -> int:
    # patterns

    # M.S   S.S   M.M   S.M   M.S
    # .A.   .A.   .A.   .A.   .A.
    # M.S   M.M   S.S   S.M   S.M

    # (-1, -1) (-1,  0) (-1,  1)
    # ( 0, -1) ( 0,  0) ( 0,  1)
    # ( 1, -1) ( 1,  0) ( 1,  1)

    patterns = [
        # 1
        {(-1, -1): 'M', (-1, 1): 'S', (1, -1): 'M', (1, 1): 'S'},
        # 2
        {(-1, -1): 'S', (-1, 1): 'S', (1, -1): 'M', (1, 1): 'M'},
        # 3
        {(-1, -1): 'M', (-1, 1): 'M', (1, -1): 'S', (1, 1): 'S'},
        # 4
        {(-1, -1): 'S', (-1, 1): 'M', (1, -1): 'S', (1, 1): 'M'},
    ]
    return sum(
        [
            int(
                data[i][j] == 'A'
                and any(
                    [
                        all([data[i + c[0]][j + c[1]] == val for c, val in p.items()])
                        for p in patterns
                    ]
                )
            )
            for i in range(1, len(data) - 1)
            for j in range(1, len(data[i]) - 1)
        ]
    )


def main():
    data = get_input_data(4).splitlines()
    t = 'XMAS'
    print(
        count_func(data, t)
        + sum([count_func(orient(data), t) for orient in [cols, diags1, diags2]])
    )
    print(count_patterns(data))


if __name__ == '__main__':
    main()
