# TC: O(num), SC: O(num)
def sum_of_first_n_natural_numbers(num: int) -> int:
    if num == 1:
        return 1
    sum = num + sum_of_first_n_natural_numbers(num-1)
    return sum

# Parameterised recursion
def sum_of_first_n_natural_numbers(num: int, sum: int) -> int:
    if num == 0:
        print(sum)
        return 
    sum_of_first_n_natural_numbers(num-1, sum+num)

    


if __name__ == "__main__":
    # print(sum_of_first_n_natural_numbers(4))
    print(sum_of_first_n_natural_numbers(4, 0))