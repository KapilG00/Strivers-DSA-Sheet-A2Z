# Using forward recursion.
def print_n_to_1(times: int) -> None:
    if times < 1:
        return
    print(times, end=" ")
    print_n_to_1(times-1)

# Using backtracking.
def print_n_to_1(times: int) -> None:
    if times < 1:
        return
    print_n_to_1(times-1)
    print(times, end=" ")


if __name__ == "__main__":
    print(print_n_to_1(4))