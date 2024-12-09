from collections.abc import Callable
from functools import reduce

from dataloader import get_input_data


def lr_eval(
    result: int, parts: list[int], operators: list[Callable[[int, int], int]]
) -> int:
    return result if result in reduce(lambda acc, n: [op(a, n) for a in acc for op in operators], parts[1:], [parts[0]]) else 0


def main():
    equations = get_input_data(
        7,
        parser=lambda data: [
            (
                int(line.split(':')[0]),
                [int(i) for i in line.split(':')[1].strip().split()],
            )
            for line in data.splitlines()
        ],
    )
    operators = [int.__add__, int.__mul__, lambda x, y: int(str(x)+str(y))]
    r1 = sum([lr_eval(*equation, operators[:2]) for equation in equations])
    print(r1)  
    assert r1 == 2654749936343

    r2 = sum([lr_eval(*equation, operators) for equation in equations])
    print(r2)  
    assert r2 == 124060392153684


if __name__ == '__main__':
    main()
