from typing import List


def print_ele_of_pascals_triangle(row: int, column: int):
    """
    Returns the element at (row, column) in Pascal's Triangle.
    Rows and columns are 1-based.
    """
    n = row - 1
    r = column - 1
    result = 1

    # Compute nCr
    for i in range(r):
        result = result * (n - i)
        result = result // (i + 1)

    return result

# TC: ~O(rows^3)
# SC: O(rows^2)
# Brute-force
def print_pascals_triangle(rows: int):
    pascals_triangle = []

    for row in range(1, rows+1):
        temp_arr = []

        for column in range(1, row+1):
            temp_arr.append(print_ele_of_pascals_triangle(row, column))

        pascals_triangle.append(temp_arr)

    return pascals_triangle

def generate_row(row: int):
    result = 1
    triangle_row = []
    triangle_row.append(1)

    for column in range(1, row):
        result = result * (row-column)
        result = result // column
        triangle_row.append(result)

    return triangle_row    

# TC: O(n^2)
# SC: O(n^2)
def print_pascals_triangle(rows: int):
    pascals_triangle = []

    for row in range(1, rows+1):
        triangle_row = generate_row(row)
        pascals_triangle.append(triangle_row)

    return pascals_triangle     



if __name__ == "__main__":
    print(print_pascals_triangle(6))