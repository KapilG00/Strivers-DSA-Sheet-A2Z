from typing import List
import math

# TC: O(num), SC: O(num)
def print_all_divisors_of_a_number(num: int) -> List[int]:
    divisors_list = []

    for i in range(1, num+1):
        if num%i == 0:
            divisors_list.append(i)
    return divisors_list        

# TC: O(sqrt(num)), SC: O(2*sqrt(num))
def print_all_divisors_of_a_number(num: int) -> List[int]:
    divisors_list = []

    for i in range(1, int(math.isqrt(num))+1):
        if num%i == 0:
            divisors_list.append(i)
            if i != num // i:
                divisors_list.append(num // i)
    return divisors_list 

if __name__ == "__main__":
    print(print_all_divisors_of_a_number(36))
    print(print_all_divisors_of_a_number(12))