# TC: O(log10 N), SC: O(1)
def reverse_a_number(number: int) -> int:
    num = number
    reversed_number = 0

    while num != 0:
        last_digit = num % 10
        num = num // 10
        reversed_number = (reversed_number * 10) + last_digit
    return reversed_number


if __name__ == "__main__":
    print(reverse_a_number(12345))