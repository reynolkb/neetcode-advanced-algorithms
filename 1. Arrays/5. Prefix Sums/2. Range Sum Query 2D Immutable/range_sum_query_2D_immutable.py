from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i, line in enumerate(matrix):
            previous = 0
            for j, num in enumerate(line):
                previous += num
                above = self.sum_matrix[i][j + 1]
                self.sum_matrix[i + 1][j + 1] = previous + above

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_right = self.sum_matrix[r2][c2]
        above = self.sum_matrix[r1 - 1][c2]
        left = self.sum_matrix[r2][c1 - 1]
        top_left = self.sum_matrix[r1 - 1][c1 - 1]

        sum_col2 = bottom_right - above
        sum_col1 = left - top_left

        return sum_col2 - sum_col1


def main():
    commands = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
    values = [
        [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ],
        [2, 1, 4, 3],
        [1, 1, 2, 2],
        [1, 2, 2, 4]
    ]
    output = []
    obj = None
    for i, command in enumerate(commands):
        if command == "NumMatrix":
            obj = NumMatrix(values[i])
            output.append(None)
        elif command == "sumRegion":
            output.append(obj.sum_region(*values[i]))
    print(output)


if __name__ == "__main__":
    main()
