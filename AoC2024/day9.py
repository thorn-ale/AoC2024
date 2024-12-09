from dataloader import get_input_data


def next_free_pos(disk_repr: list[int]) -> int:
    for i, item in enumerate(disk_repr):
        if item == -1:
            return i


def next_memory_pos(disk_repr: list[int]) -> int:
    for i, item in enumerate(disk_repr[::-1]):
        if item != -1:
            return len(disk_repr) - i - 1


def part1(disk_repr: list[int]) -> int:
    while 1:
        free, file = next_free_pos(disk_repr), next_memory_pos(disk_repr)
        disk_repr[free] = disk_repr[file]
        disk_repr[file] = -1
        if free == file - 1:
            break
    return sum([i * x for i, x in enumerate(disk_repr) if x != -1])


def free_memory_map(disk_repr: list[int]) -> list[tuple[int, int]]:
    res = []
    i = 0
    memory_size = len(disk_repr)
    while i < memory_size:
        value = disk_repr[i]
        if value == -1:
            j = i
            while j < memory_size and disk_repr[j] == -1:
                j += 1
            res.append((i, j - i))
            i += j - i
        else:
            i += 1
    return res


def reverse_file_map(disk_repr: list[int]) -> list[tuple[int, int, int]]:
    res = []
    i = 0
    memory_size = len(disk_repr)
    while i < memory_size:
        value = disk_repr[i]
        if value != -1:
            j = i
            while j < memory_size and disk_repr[j] == value:
                j += 1
            res.append((i, j - i, value))
            i += j - i
        else:
            i += 1
    return res[::-1]


def part2(disk_repr: list[int]) -> int:
    for file_start_pos, file_size, file_idx in reverse_file_map(disk_repr):
        for block_start_pos, block_size in free_memory_map(disk_repr):
            if file_size <= block_size and block_start_pos < file_start_pos:
                for i in range(file_size):
                    disk_repr[block_start_pos + i] = file_idx
                    disk_repr[file_start_pos + i] = -1
                break
    return sum([i * x for i, x in enumerate(disk_repr) if x != -1])


def main():
    data = get_input_data(9).strip()
    # data = '2333133121414131402'
    disk_repr = []
    file_block = True
    file_idx = 0
    for value in data:
        if file_block:
            disk_repr += [file_idx] * int(value)
            file_idx += 1
        else:
            disk_repr += [-1] * int(value)
        file_block = not file_block
    p1_hash = part1(disk_repr.copy())
    print(p1_hash)  # 6225730762521

    p2_hash = part2(disk_repr.copy())
    print(p2_hash)  # 6250605700557

    assert p1_hash == 6225730762521
    assert p2_hash == 6250605700557


if __name__ == '__main__':
    main()
