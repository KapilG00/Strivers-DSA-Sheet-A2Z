# Using forward recursion.
def print_1_to_n(times: int, num: int) -> None:
    if num > times:
        return
    print(num, end=" ")
    print_1_to_n(times, num+1)

# Using backtracking.
def print_1_to_n(times: int, num: int) -> None:
    if num > times:
        return
    print_1_to_n(times, num+1)
    print(num, end=" ")


if __name__ == "__main__":
    print(print_1_to_n(4, 1))