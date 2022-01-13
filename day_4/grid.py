from typing import List
from collections import namedtuple


class Grid:
    def __init__(self, matrix: List[List[int]]):
        self._matrix = matrix
        self._index = {}
        self._index_matrix()
        self.solved = False

    def mark_number(self, number: int) -> bool:
        """
        if number exists in a grid, it will be marked
        if one of the rows or columns is after that completed, True will be returned, False otherwise
        """
        if number in self._index:
            row, column = self._index[number]
            self._matrix[row][column] = True

        is_bingo = self._check_if_bingo()
        return is_bingo

    def sum_unmarked_numbers(self):
        return sum(
            sum([num for num in row if num is not True])
            for row in self._matrix
        )

    def _index_matrix(self) -> None:
        """
        to be used as a fast check whether number exists in a grid
        """
        position = namedtuple("position", "x y")

        for row_idx, row in enumerate(self._matrix):
            for col_idx, number in enumerate(row):
                self._index[number] = position(row_idx, col_idx)

    def _check_if_bingo(self) -> bool:
        if self.solved:
            return True

        # checking rows
        for row in self._matrix:
            if self.all_positions_are_checked(row):
                self.solved = True
                return True

        # 90 degrees rotation → for checking columns
        for row in list(list(x)[::-1] for x in zip(*self._matrix)):
            if self.all_positions_are_checked(row):
                self.solved = True
                return True

        # not a Bingo :(
        return False

    @staticmethod
    def all_positions_are_checked(row: list) -> bool:
        return all(map(lambda position: position is True, row))