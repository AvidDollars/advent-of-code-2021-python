import re
from collections import namedtuple, Counter

data_file = "files/day-5.txt"
numbers_re = re.compile("(\d+),(\d+)\s->\s(\d+),(\d+)")


def extract_numbers(row: str) -> namedtuple:
    coords = namedtuple("coords", "x1 y1 x2 y2")
    numbers = numbers_re.match(row).groups()
    return coords(*(int(num) for num in numbers))


def update_counter(counter: Counter, *, x1: int, x2: int, y1: int, y2: int, straight_line: bool) -> None:
    if straight_line:
        if (x1 > x2):
            x1, x2 = x2, x1

        if (y1 > y2):
            y1, y2 = y2, y1

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                counter[(x, y)] += 1

    elif not straight_line:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        y_to_add = -1 if y1 > y2 else 1

        while x2 >= x1:
            counter[(x1, y1)] += 1
            x1 += 1
            y1 += y_to_add


def count_overlaps(*, only_straight_lines: bool = True) -> int:
    counter = Counter()

    with open(data_file) as data:
        for row in data:
            x1, y1, x2, y2 = extract_numbers(row)

            if x1 == x2 or y1 == y2:
                update_counter(counter, x1=x1, x2=x2, y1=y1, y2=y2, straight_line=True)

            elif only_straight_lines is False:
                update_counter(counter, x1=x1, x2=x2, y1=y1, y2=y2, straight_line=False)

    return sum(1 for counts in counter.values() if counts > 1)


# PART ONE
print(count_overlaps(only_straight_lines=True))

# PART TWO
print(count_overlaps(only_straight_lines=False))