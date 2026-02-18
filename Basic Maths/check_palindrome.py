# TC: O((log10 N) + 1), SC: O(1)
def check_palindrome(number: int) -> bool:
    reversed_number = 0
    num = number
    while num != 0:
        last_digit = num % 10
        reversed_number = (reversed_number * 10) + last_digit
        num = num // 10

    if number == reversed_number:
        return True
    return False    


if __name__ == "__main__":
    print(check_palindrome(4554))
    print(check_palindrome(7789))