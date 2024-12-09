from itertools import combinations, count
from typing import Generator

from dataloader import get_input_data
from vectors import Vec2i


def compute_antinodes(a1: Vec2i, a2: Vec2i) -> tuple[Vec2i, Vec2i]:
    delta = a2 - a1
    return a1 - delta, a2 + delta


def compute_harmonics(
    a1: Vec2i, a2: Vec2i
) -> Generator[list[tuple[Vec2i, Vec2i]], None, None]:
    delta = a2 - a1
    for i in count():
        di = delta * i
        yield (a1 - di, a2 + di)


def main():
    data = get_input_data(8).splitlines()
    map = {
        Vec2i(i, j): char
        for i, line in enumerate(data)
        for j, char in enumerate(line.strip())
    }
    positions = set(map.keys())

    frequencies = list(set(map.values()))
    antinodes: set[Vec2i] = set()

    for freq in frequencies:
        if freq == '.':
            continue
        antennas = [pos for pos, f in map.items() if f == freq]
        for a1, a2 in combinations(antennas, 2):
            antis = compute_antinodes(a1, a2)
            for anti in antis:
                if anti in positions:
                    antinodes.add(anti)
    print(len(antinodes))

    harmonics: set[Vec2i] = set()

    for freq in frequencies:
        if freq == '.':
            continue
        antennas = [pos for pos, f in map.items() if f == freq]
        for a1, a2 in combinations(antennas, 2):
            for h1, h2 in compute_harmonics(a1, a2):
                if h1 not in positions and h2 not in positions:
                    break
                if h1 in positions:
                    harmonics.add(h1)
                if h2 in positions:
                    harmonics.add(h2)
    print(len(harmonics))


if __name__ == '__main__':
    main()
