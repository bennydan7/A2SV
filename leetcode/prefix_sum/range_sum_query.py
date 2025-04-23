class NumMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.prefix_matrix = self._compute_prefix_sum_matrix()

    def _compute_prefix_sum_matrix(self):
        row = len(self.matrix)
        col = len(self.matrix[0])

        prefix_matrix = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                prefix_matrix[i][j] = (
                    self.matrix[i - 1][j - 1]
                    + prefix_matrix[i - 1][j]
                    + prefix_matrix[i][j - 1]
                    - prefix_matrix[i - 1][j - 1]
                )
        return prefix_matrix

    def sumRegion(self, row1, col1, row2, col2):
        return (
            self.prefix_matrix[row2 + 1][col2 + 1]
            - self.prefix_matrix[row2 + 1][col1]
            - self.prefix_matrix[row1][col2 + 1]
            + self.prefix_matrix[row1][col1]
        )


if __name__ == "__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    num_matrix = NumMatrix(matrix)
    print(num_matrix.sumRegion(1, 1, 2, 2))
    print(num_matrix.sumRegion(2, 1, 4, 3))
    print(num_matrix.sumRegion(1, 2, 2, 4))