from typing import List


def mark_row(matrix: List[List[int]], row_number: int, matrix_columns: int):
    for column_number in range(matrix_columns):
        if matrix[row_number][column_number] != 0:
            matrix[row_number][column_number] = -1

def mark_column(matrix: List[List[int]], column_number: int, matrix_rows: int):
    for row_number in range(matrix_rows):
        if matrix[row_number][column_number] != 0:
            matrix[row_number][column_number] = -1

# Brute-force
# n => no. of matrix rows; m => no. of matrix columns
# TC: O(nm) * O(n+m) + O(nm) ~ O(n^3)
# SC: O(1)
def set_matrix_zeroes(matrix: List[List[int]]) -> List[List[int]]:
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])

    for row_number in range(matrix_rows):
        for column_number in range(matrix_columns):
            if matrix[row_number][column_number] == 0:
                mark_row(matrix, row_number, matrix_columns)
                mark_column(matrix, column_number, matrix_rows)

    for row_number in range(matrix_rows):
        for column_number in range(matrix_columns):
            if matrix[row_number][column_number] == -1:
                matrix[row_number][column_number] = 0

    return matrix                       

# Better
# n => no. of matrix rows; m => no. of matrix columns
# TC: O(nm) + O(nm) ~ O(n^2)
# SC: O(n) + O(m)
def set_matrix_zeroes(matrix: List[List[int]]) -> List[List[int]]:
    matrix_rows = len(matrix)
    matrix_columns = len(matrix[0])
    row_arr = [0] * matrix_rows # row_arr means vertical array
    column_arr = [0] * matrix_columns # column_arr means horizontal array

    for row_number in range(matrix_rows):
        for column_number in range(matrix_columns):
            if matrix[row_number][column_number] == 0:
                row_arr[row_number] = 1
                column_arr[column_number] = 1

    for row_number in range(matrix_rows):
        for column_number in range(matrix_columns):      
            if row_arr[row_number] == 1 or column_arr[column_number] == 1:
                matrix[row_number][column_number] = 0

    return matrix                  



if __name__ == "__main__":
    print(set_matrix_zeroes([[1,1,1], [1,0,1], [1,1,1]]))
    print(set_matrix_zeroes([[1, 2, 0, 4], [5, 6, 7, 8]]))