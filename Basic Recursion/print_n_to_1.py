# Using forward recursion.
def print_n_to_1(times: int) -> None:
    if times < 1:
        return
    print(times, end=" ")
    print_n_to_1(times-1)

# Using backtracking.
def print_n_to_1(times: int, num: int) -> None:
    if num > times:
        return
    print_n_to_1(times, num+1)
    print(num, end=" ")



if __name__ == "__main__":
    print(print_n_to_1(4))
    print(print_n_to_1(4, 1)) # For back-tracking