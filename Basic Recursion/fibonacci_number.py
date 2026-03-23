def fibonacci_number(num: int) -> int:
    # base case.
    if num <= 1:
        return num
    
    # recursive call.
    return fibonacci_number(num-1) + fibonacci_number(num-2)


if __name__ == "__main__":
    print(fibonacci_number(4))
    print(fibonacci_number(50))