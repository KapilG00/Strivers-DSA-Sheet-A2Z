# TC: O(num) 
# SC: O(1)
def fibonacci_using_dp_tabulation(num: int) -> int:
    prev_2 = 0 
    prev_1 = 1

    for _ in range(2, num+1):
        current = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 =  current

    return prev_1
    

if __name__ == "__main__":
    num = 5
    # If we dont optimise the space then we need to use this array.
    # dp_arr = [-1] * (num+1) 
    # print(fibonacci_using_dp_tabulation(num, dp_arr))

    # If we optimise the space then we need to get rid of the above array.
    print(fibonacci_using_dp_tabulation(num))