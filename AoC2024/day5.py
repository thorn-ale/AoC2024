from dataloader import get_input_data


def parse_rules(data: str) -> list[tuple[int, int]]:
    return [tuple(int(x) for x in line.split('|')) for line in data.splitlines()]


def parse_orders(data: str) -> list[list[int]]:
    return [[int(x) for x in line.split(',')] for line in data.splitlines()]


def parse_data(data: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules, orders = data.split('\n\n')
    return parse_rules(rules), parse_orders(orders)


def valid_pair(order: list[int], rule: tuple[int, int]) -> bool:
    try:
        return order.index(rule[0]) < order.index(rule[1])
    except ValueError:
        return True


def middle(order: list[int]) -> int:
    return order[len(order) // 2]


def swap(order: list[int], rule: tuple[int, int]) -> list[int]:
    x = order.index(rule[0])
    y = order.index(rule[1])
    temp = order[x]
    order[x] = order[y]
    order[y] = temp
    return order


def main():
    rules, orders = get_input_data(5, parser=parse_data)
    part1 = 0
    part2 = 0
    for order in orders:
        if all([valid_pair(order, r) for r in rules]):
            part1 += middle(order)
        else:
            while bad_rules := [r for r in rules if not valid_pair(order, r)]:
                rule = bad_rules.pop()
                order = swap(order, rule)
            part2 += middle(order)

    print(part1)  # 6034
    print(part2)  # 6305


if __name__ == '__main__':
    main()
