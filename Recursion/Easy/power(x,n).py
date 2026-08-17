# This is linearly increasing time complexity solution,
# hence, it will not work for large values of "n".
# TC: O(n)
# SC: O(1)
# Iterative approach
def func(x: int, n: int) -> int:
    temp = n

    if n < 0:
        x = 1/x
        temp = -1 * n

    value = 1
    for _ in range(temp):
        value *= x

    return value




# TC: O(logn)
# SC: O(logn)
# Recursive approach
def helper(x: int, n: int) -> float:
    # base condition.
    if n == 0:
        return 1.0
    
    # base condition.
    if n == 1:
        return x
    
    if n%2 == 0:
        return helper(x*x, n/2)
    return x * helper(x, n-1)

def calculate_power_of_x_over_n(x: int, n: int) -> float:
    if n < 0:
        return 1 / helper(x, -n)
    return helper(x, n)

if __name__ == "__main__":
    print(calculate_power_of_x_over_n(2, 10))
    print(calculate_power_of_x_over_n(2, -2))