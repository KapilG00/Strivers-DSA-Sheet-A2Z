import math

# TC: O(num), SC: O(1)
def check_prime_number_or_not(num: int) -> bool:
    is_prime = False
    count = 0

    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        is_prime = True
    return is_prime

# TC: O(sqrt(num)), SC: O(1)
def check_prime_number_or_not(num: int) -> bool:
    is_prime = False
    count = 0

    for i in range(1, int(math.isqrt(num))+1):
        if num%i == 0:
            count += 1
            if i != num//i:
                count += 1
    if count == 2:
        is_prime = True
    return is_prime


if __name__ == "__main__":
    print(check_prime_number_or_not(2))
    print(check_prime_number_or_not(10))