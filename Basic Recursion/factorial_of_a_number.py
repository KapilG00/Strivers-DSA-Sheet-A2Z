# TC: O(num), SC: O(num)
def factorial_of_a_number(num: int) -> int:
    if num == 1:
        return 1

    return num * factorial_of_a_number(num-1)


if __name__ == "__main__":
    print(factorial_of_a_number(4))