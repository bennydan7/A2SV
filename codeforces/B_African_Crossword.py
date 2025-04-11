n,m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]

result = []


for i in range(n):
    for j in range(m):
        row = matrix[i]
        col = [matrix[x][j] for x in range(n)]
        if row.count(matrix[i][j]) == 1 and col.count(matrix[i][j]) == 1:
            result.append(matrix[i][j])
print("".join(map(str,result)))
