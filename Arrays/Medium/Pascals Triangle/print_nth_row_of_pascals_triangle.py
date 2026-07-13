from typing import List


# TC: O(n)
# SC: O(1)
def print_nth_row_pascals_triangle(n: int):
    result = 1
    print(result)

    for i in range(1, n):
        result = result * (n - i)
        result = result // i
        print(result)

    return    


if __name__ == "__main__":
    print(print_nth_row_pascals_triangle(6))