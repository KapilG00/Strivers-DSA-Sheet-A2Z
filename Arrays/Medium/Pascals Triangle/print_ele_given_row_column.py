from typing import List


# TC: O(r)
# SC: O(1)
def print_ele_of_pascals_triangle(row: int, column: int):
    """
    nCr = n!/r!(n-r)!
    e.g. n is 4 and r is 2

    4C2 = 4!/2!(2!) = 4*3*2!/2!*2! = 4*3/2*1 = 6
    """
    n = row-1
    r = column-1
    result = 1

    # nCr formula
    for i in range(r):
        result = result * (n - i)
        result = result // (i + 1)

    return result    


if __name__ == "__main__":
    print(print_ele_of_pascals_triangle(5, 3))