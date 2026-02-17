import math

# Using type casting.
# TC: O(N), SC: O(N)
def count_all_digits_of_a_number(number: int) -> int:
    count = 0
    for _ in str(number):
        count += 1
    return count

# Using division by 10 method.
# TC: O((log10 N) + 1), SC: O(1)
def count_all_digits_of_a_number(number: int) -> int:
    count = 0
    num = number
    while num != 0:
        num = num // 10
        count += 1
    return count    

# Using (log10 N) + 1 formula.
# TC: O(1), SC: O(1)
def count_all_digits_of_a_number(number: int) -> int:
    count = int(math.log10(number)+1)
    return count


if __name__ == "__main__":
    print(count_all_digits_of_a_number(12345))