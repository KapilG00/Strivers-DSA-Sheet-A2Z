# TC: O(num), SC: O(num)
def sum_of_first_n_natural_numbers(num: int) -> int:
    if num == 1:
        return 1
    sum = num + sum_of_first_n_natural_numbers(num-1)
    return sum


if __name__ == "__main__":
    print(sum_of_first_n_natural_numbers(4))