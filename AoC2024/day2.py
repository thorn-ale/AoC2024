from dataloader import get_input_data
from itertools import pairwise


def safety_check(report: list[int]) -> bool:
    return (report == sorted(report) or report == sorted(report, reverse=True)) and all(
        [1 <= abs(a - b) <= 3 for a, b in pairwise(report)]
    )


def problem_dampener(report: list[int]) -> bool:
    return any([safety_check(report[:i] + report[i + 1 :]) for i in range(len(report))])


def main():
    data = get_input_data(
        2,
        parser=lambda p: [[int(x) for x in d.strip().split()] for d in p.splitlines()],
    )
    print(len([safe for d in data if (safe := safety_check(d))]))
    print(
        len([safe for d in data if (safe := safety_check(d) or problem_dampener(d))])
    )


if __name__ == '__main__':
    main()
