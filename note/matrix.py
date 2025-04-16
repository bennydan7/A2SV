def diagonalSum(mat):
        n = len(mat)
        print(n)
        total = 0

        for i in range(n):
            total += mat[i][i]
            total += mat[i][n-1 - i]

        if n // 2 == 1:
              total -= mat[n//2][n//2]

        return total



print(diagonalSum(mat = [[5]]))