# even_digits = [0, 2, 4, 6, 8]
# prime_digits = [2, 3, 5, 7]


MOD = 10**9 + 7

# TC: O(n)
# SC: O(1)
def count_good_numbers(n: int) -> int:
    count = 1

    for idx in range(n):
        if idx % 2 == 0:
            # Even index → 5 choices
            count *= 5
        else:
            # Odd index → 4 choices
            count *= 4

        count %= MOD

    return count

def power(x: int, n: int) -> int:
    result = 1

    while n > 0:
        # If n is odd, include current x
        if n % 2 == 1:
            result = (result * x) % MOD

        # Square x
        x = (x*x) % MOD

        # Divide exponent by 2
        n = n // 2

    return result

# TC: O(logn)
# SC: O(1)   
# Iterative approach using binary exponentiation.
def count_good_numbers(n: int) -> int:
    even = (n + 1) // 2
    odd = n // 2

    v1 = power(5, even)
    v2 = power(4, odd)

    return (v1 * v2) % MOD

def power(x: int, n: int) -> int:
    if n == 0:
        return 1

    if n == 1:
        return x

    if n%2 == 0:
        return power((x*x) % MOD, n//2)
    return (x * power(x, n-1)) % MOD

# TC: O(logn)
# SC: O(logn)   
# Recursive approach using binary exponentiation.
def count_good_numbers(n: int) -> int:
    even = (n+1)//2
    odd = n//2
    v1 = power(5, even)
    v2 = power(4, odd)

    return (v1*v2) % MOD

# # This is not efficient in terms of complexity.
# # This code was present on https://takeuforward.org/data-structure/count-good-numbers
# # TC: O(2^n)
# # SC: O(n); here "n" is recursive call stack depth
def count_good_numbers(n: int, idx: int) -> int:
    # Base case
    if idx == n:
        return 1

    count = 0
    
    # Even index: Use even digits
    if idx % 2 == 0:  
        for _ in range(5):
            count = (count + count_good_numbers(n, idx+1)) % MOD
    # Odd index: Use prime digits        
    else:
        for _ in range(4):
            count = (count + count_good_numbers(n, idx+1)) % MOD

    return count

        

if __name__ == "__main__":
    print(count_good_numbers(6))
    print(count_good_numbers(4))
    print(count_good_numbers(2))
    print(count_good_numbers(2, 0))
    print(count_good_numbers(4, 0))
    print(count_good_numbers(6, 0))