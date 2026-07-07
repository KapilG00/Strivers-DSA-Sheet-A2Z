from typing import List


# TC: O(num) 
# SC: O(num) + O(num); one is for recursion stack space and the other is for our dp array.
def fibonacci_using_dp_memoization(num: int, dp_arr: List[int]) -> int:
    if num <= 1:
        return num
    
    if dp_arr[num] != -1:
        return dp_arr[num]
    
    dp_arr[num] = fibonacci_using_dp_memoization(num-1, dp_arr) + fibonacci_using_dp_memoization(num-2, dp_arr)
    
    return dp_arr[num]



if __name__ == "__main__":
    num = 5
    dp_arr = [-1] * (num+1)
    print(fibonacci_using_dp_memoization(num, dp_arr))