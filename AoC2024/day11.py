import math
from functools import lru_cache

from dataloader import get_input_data


@lru_cache(maxsize=None)
def rule_2(stone: int) -> list[int]:
    stone_length = int(math.log10(stone)) + 1
    if stone_length % 2 == 0:
        div = 10 ** (stone_length // 2)
        return [stone // div, stone % div]
    return []


@lru_cache(maxsize=None)
def process_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif r2 := rule_2(stone):
        return r2
    else:
        return [stone * 2024]


@lru_cache(maxsize=None)
def blink_stone(stone: int, depth: int) -> int:
    if depth == 1:
        return len(process_stone(stone))
    return sum([blink_stone(x, depth - 1) for x in process_stone(stone)])


def main():
    stones = get_input_data(11, parser=lambda x: list(map(int, x.strip().split())))
    print(sum([blink_stone(x, 25) for x in stones]))  # 239714
    print(sum([blink_stone(x, 75) for x in stones]))  # 284973560658514


if __name__ == '__main__':
    main()
