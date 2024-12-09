from math import ceil
from multiprocessing import Pool, cpu_count
from dataloader import get_input_data
from vectors import Vec2i, NORTH, SOUTH, EAST, WEST


class CycleDetectedException(Exception): ...


def walk(map: dict[Vec2i, str], start_pos: Vec2i, start_dir: str, obstacle_pos: Vec2i|None = None) -> list[tuple[Vec2i, str]]:
    path: list[tuple[Vec2i, str]] = [(start_pos, start_dir)]
    cycle_check_set = set(path)
    while 1:
        pos, direction = path[-1]
        try:
            match direction:
                case '^' if map[pos + NORTH] == '#' or pos + NORTH == obstacle_pos:
                    path.append((pos, '>'))
                case '^':
                    path.append((pos + NORTH, direction))
                
                case 'v' if map[pos + SOUTH] == '#' or pos + SOUTH == obstacle_pos:
                    path.append((pos, '<'))
                case 'v' if map[pos + SOUTH]:
                    path.append((pos + SOUTH, direction))
                
                case '>' if map[pos + EAST] == '#' or pos + EAST == obstacle_pos:
                    path.append((pos, 'v'))
                case '>' if map[pos + EAST]:
                    path.append((pos + EAST, direction))
                
                case '<' if map[pos + WEST] == '#' or pos + WEST == obstacle_pos:
                    path.append((pos, '^'))
                case '<' if map[pos + WEST]:
                    path.append((pos + WEST, direction))
                
        except KeyError:
            break
        if path[-1] in cycle_check_set:
            raise CycleDetectedException()
        cycle_check_set.add(path[-1])
    return path

def count_cycle(args: tuple[list[Vec2i], dict[Vec2i, str], Vec2i, str]) -> int:
    path, map, start_pos, start_dir = args
    cycle_count = 0
    for pos in path:
        if pos == start_pos:
            continue
        if map[pos] == '.':
            try:
                walk(map|{pos:'#'}, start_pos, start_dir)
            except CycleDetectedException:
                cycle_count += 1
    return cycle_count

def main():
    data = get_input_data(6)
    map = {Vec2i(i, j): char for i, line in enumerate(data.splitlines()) for j, char in enumerate(line.strip())}
    guard = [pos for pos, char in map.items() if char in '^>v<'][0]
    direction = map[guard]
    map[guard] = '.'
    path = set([pos for pos, _ in walk(map, guard, direction)])
    print(len(path))
    pc = cpu_count()*2
    size = ceil(len(path)/pc)
    path = list(path)
    with Pool(pc) as p:
        print(sum(p.map(count_cycle, [(path[i*size:i*size+size], map, guard, direction) for i in range(pc)])))



if __name__ == '__main__':
    main()
