
# TC: O(2^n)
def fibonacci_number(num: int) -> int:
    # base case.
    if num <= 1:
        return num
    
    # multiple recursive call.
    last = fibonacci_number(num-1)
    second_last = fibonacci_number(num-2)
    
    return last + second_last

if __name__ == "__main__":
    print(fibonacci_number(4))
    print(fibonacci_number(10))