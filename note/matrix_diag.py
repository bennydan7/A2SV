def diagonalSum(mat):
    n = len(mat)
    total = 0
    
    for i in range(n):
        total += mat[i][i]
        total += mat[i][n - 1 - i]  # Secondary diagonal
    
    if n % 2 == 1:
        total -= mat[n//2][n//2]
    
    return total

# Example Test Cases
mat1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

mat2 = [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]

print(diagonalSum(mat1))  # Output: 25 (1+5+9 + 3+7)
print(diagonalSum(mat2))  # Output: 8 (1+1+1+1 + 1+1+1+1)
