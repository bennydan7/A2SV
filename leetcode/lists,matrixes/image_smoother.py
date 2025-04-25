def imageSmoother(img):
    m,n = len(img), len(img[0])
    res = [[0]* n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            total,count = 0,0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if i < 0 or i == m or j < 0 or j == n:
                        continue
                    total += img[i][j]
                    count += 1
            res[r][c] = total // count
    return res


    