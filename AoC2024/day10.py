from collections import deque

from dataloader import get_input_data
from vectors import Vec2i, NORTH, SOUTH, EAST, WEST

DIRS = [NORTH, SOUTH, EAST, WEST]


def valid_neighbours(trailmap: dict[Vec2i, int], pos: Vec2i) -> list[Vec2i]:
    res = []
    for d in DIRS:
        n_pos = pos + d
        if n_pos in trailmap and trailmap[n_pos] == trailmap[pos] + 1 and n_pos:
            res.append(n_pos)
    return res


def check_trail(trailmap: dict[Vec2i, int], start_pos: Vec2i) -> int:
    score = 0
    path = deque([start_pos])
    visited = set()
    while path:
        current = path.popleft()
        if current in visited:
            continue
        visited.add(current)
        if trailmap[current] == 9:
            score += 1
        else:
            path += valid_neighbours(trailmap, current)
    return score


def rank_trail(trailmap: dict[Vec2i, int], start_pos: Vec2i) -> int:
    rank = 0
    path = deque([start_pos])
    while path:
        current = path.popleft()
        if trailmap[current] == 9:
            rank += 1
        else:
            path.extend(valid_neighbours(trailmap, current))
    return rank


def main():
    data = get_input_data(10).splitlines()
    trailmap = {
        Vec2i(i, j): int(height)
        for i, line in enumerate(data)
        for j, height in enumerate(line.strip())
    }
    trail_count, trail_rank = 0, 0
    for pos, height in trailmap.items():
        if height == 0:
            trail_count += check_trail(trailmap, pos)
            trail_rank += rank_trail(trailmap, pos)
    print(trail_count)
    print(trail_rank)


if __name__ == '__main__':
    main()
