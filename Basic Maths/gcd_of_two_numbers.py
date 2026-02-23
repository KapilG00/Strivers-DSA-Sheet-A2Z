# TC: O(min(num1, num2), SC: O(1)
def gcd_of_two_numbers(num1: int, num2: int) -> int:
    min_of_two_numbers = min(num1, num2)
    gcd = 1
    
    for i in range(1, min_of_two_numbers+1):
        if num1%i == 0 and num2%i == 0:
            gcd = i
    return gcd        

# # TC: O(min(num1, num2), SC: O(1)
def gcd_of_two_numbers(num1: int, num2: int) -> int:
    min_of_two_numbers = min(num1, num2)
    gcd = 1
    
    for i in range(min_of_two_numbers, 0, -1):
        if num1%i == 0 and num2%i == 0:
            return i

# Using euclidean algorithm.
# TC: O(min(num1, num2), SC: O(1)
def gcd_of_two_numbers(num1: int, num2: int) -> int:
    while num1>0 and num2>0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    if num1 == 0:
        return num2
    return num1


if __name__ == "__main__":
    print(gcd_of_two_numbers(9, 12))