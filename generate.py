from pathlib import Path
from datetime import timedelta
from functools import cache

out_file = Path("./docs/index.md")

LAST_LEVEL = 500


@cache
def calculate_score(level: int) -> int:
    if level <= 1:
        return 10
    return level * 10 + calculate_score(level - 1)


@cache
def get_level_time(level: int) -> timedelta:
    times = {
        1: timedelta(seconds=38),
        2: timedelta(seconds=31),
        3: timedelta(seconds=26),
        4: timedelta(seconds=22),
    }

    if level <= 1:
        return times[level]

    if level in times:
        return times[level] + get_level_time(level - 1)

    return timedelta(seconds=20) + get_level_time(level - 1)


def main():
    markdown = "\n".join(
        [
            "|level|score|time|",
            "|:-:|:-:|:-:|",
            *[
                f"|{level}|{calculate_score(level)}|{get_level_time(level)}|"
                for level in range(1, LAST_LEVEL + 1)
            ],
        ]
    )

    out_file.write_text(markdown)


if __name__ == "__main__":
    main()
