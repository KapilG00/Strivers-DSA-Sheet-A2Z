# TC: O(log(N) + 1), SC: O(1)
def check_armstrong_number(num: int) -> bool:
    is_armstrong = False
    value = num
    sum = 0
    k = len(str(num))
    
    while value > 0:
        last_digit = value % 10
        sum = sum + (last_digit**k)
        value = value // 10
    if sum == num:
        is_armstrong = True
    return is_armstrong        


if __name__ == "__main__":
    print(check_armstrong_number(153))
    print(check_armstrong_number(3712))