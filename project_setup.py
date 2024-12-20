from pathlib import Path


def main():
    project_dir = Path(__file__).parent
    input_dir = project_dir.joinpath('input')
    src_dir = project_dir.joinpath('AoC2024')
    input_dir.mkdir(exist_ok=True)
    src_dir.mkdir(exist_ok=True)
    for i in range(1, 26):
        daily_src = src_dir.joinpath(f'day{i}.py')
        if not daily_src.exists():
            open(
                daily_src, 'w', encoding='utf-8'
            ).write(f"""from dataloader import get_input_data


def main():
    _data = get_input_data({i})


if __name__ == '__main__':
    main()

""")


if __name__ == '__main__':
    main()
