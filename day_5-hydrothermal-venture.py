import re
from collections import namedtuple, Counter

data_file = "files/day-5.txt"
numbers_re = re.compile("(\d+),(\d+)\s->\s(\d+),(\d+)")
counter = Counter()


def extract_numbers(row: str) -> namedtuple:
    coords = namedtuple("coords", "x1 y1 x2 y2")
    numbers = numbers_re.match(row).groups()
    return coords(*(int(num) for num in numbers))


def update_counter(counter: Counter, *, x1: int, x2: int, y1: int, y2: int) -> None:
    if (x1 > x2):
        x1, x2 = x2, x1

    if (y1 > y2):
        y1, y2 = y2, y1

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            counter[(x, y)] += 1


def count_overlaps(counter: Counter) -> int:
    overlaps = 0
    for coords, counts in counter.items():
        if counts > 1:
            overlaps += 1
    return overlaps


with open(data_file) as data:
    for row in data:
        x1, y1, x2, y2 = extract_numbers(row)

        if x1 == x2 or y1 == y2:
            update_counter(counter, x1=x1, x2=x2, y1=y1, y2=y2)

print(count_overlaps(counter))