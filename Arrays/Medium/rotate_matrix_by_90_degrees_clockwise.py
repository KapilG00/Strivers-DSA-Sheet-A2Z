from typing import List


# Brute-force
# n => no. of matrix rows; m => no. of matrix columns
# TC: O(n^2)
# SC: O(n^2)
# def rotate_matrix_by_90_degrees(matrix: List[List[int]]) -> List[List[int]]:
#     n = len(matrix)
#     rotated_matrix = [[0]* n for _ in range(n)]

#     for row in range(n):
#         for column in range(n):
#             rotated_matrix[column][n-1-row] = matrix[row][column]

#     return rotated_matrix

# Optimal
# n => no. of matrix rows; m => no. of matrix columns
# TC: [O(n/2) * O(n/2)] + O(n*(n/2))
# SC: O(1)
def rotate_matrix_by_90_degrees(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
     
    # O(n/2) * O(n/2)
    # Take transpose of the matrix.
    for row in range(n-1): # O(n/2)
        for column in range(row+1, n): # O(n/2)
            if row != column:
                print(row, column)
                matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]   
    # O(n*(n/2))
    # Reverse every row.
    for row in range(n): # O(n)
        matrix[row].reverse() # O(n/2)

    return matrix


if __name__ == "__main__":
    print(rotate_matrix_by_90_degrees([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))