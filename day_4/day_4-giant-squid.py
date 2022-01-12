from typing import List, IO, Pattern
import re
from grid import Grid # importing custom class

file_path = "../files/day-4.txt"
empty_spaces = re.compile("\s+")


def extract_numbers(csv_numbers: str, *, delimiter: Pattern[str] = ",") -> List[int]:
    return [
        int(number) for number
        in re.split(delimiter, csv_numbers.strip())
    ]


def extract_all_grids(file_rows: IO[str]) -> List[List[List[int]]]:
    all_grids = []

    grid = []
    for row in file_rows:
        if row != "\n":
            numbers = extract_numbers(row, delimiter=empty_spaces)
            grid.append(numbers)

        if len(grid) == 5:
            grid = Grid(grid)
            all_grids.append(grid)

            # new grid for next 5x5 matrix
            grid = []

    return all_grids


def extract_numbers_and_grids(file_path: str) -> tuple:
    with open(file_path) as data:
        numbers_row = next(data)
        numbers_list = extract_numbers(numbers_row)
        grids = extract_all_grids(data)

    return numbers_list, grids


def play_bingo(numbers, grids):
    for number in numbers:
        for grid in grids:
            is_bingo = grid.mark_number(number)
            if is_bingo:
                return number * grid.sum_unmarked_numbers()


numbers_list, grids = extract_numbers_and_grids(file_path)
result = play_bingo(numbers_list, grids)
print(result)