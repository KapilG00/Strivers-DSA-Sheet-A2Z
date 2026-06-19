# TC: O(logn)
# SC: O(logn)
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