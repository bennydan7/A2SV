def spiral_matrix(matrix):
    row = len(matrix)
    col = len(matrix[0])

    top,bottom = 0,col - 1
    left,right = 0, row - 1

    results = []

    while top <= bottom and left <= right:

        for i in range(left,right+1):
            results.append(matrix[top][i])
        top +=1

        for i in range(top,bottom + 1):
            results.append(matrix[i][right])
        right -=1
        
        for i in range(right,left - 1,-1):
            results.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom,top - 1,-1):
            results.append(matrix[i][left])
        left += 1


    return results


print(spiral_matrix(matrix = [[1,2,3],[4,5,6],[7,8,9]]))