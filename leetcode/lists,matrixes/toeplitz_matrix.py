# def is_toeplitz_matrix(matrix):
#     rows = len(matrix)
#     cols = len(matrix[0])
#     diagonal = []
#     #  from the top row
#     for col in range(cols):
#         i,j = 0,col
#         while i < rows and j < cols:
#             diagonal.append(matrix[i][j])
#             i += 1
#             j += 1
        
#     # from the first column 
#     for row in range(rows):
#         i,j = row,0
#         while i < rows and j < cols:
#             diagonal.append(matrix[i][j])
#             i += 1
#             j += 1

#     print(dia)


def is_toeplitz_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows - 1):
        for j in range (cols -1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True


    
print(is_toeplitz_matrix(matrix = [[1,2],[2,2]]))