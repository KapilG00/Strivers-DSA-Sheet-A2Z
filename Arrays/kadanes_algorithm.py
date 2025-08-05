from typing import List


# TC -> O(n^3)
# SC -> O(1)
def max_sub_arr_sum(arr: List[int]) -> int:
    n = len(arr)
    max_sub_arr_sum = float('-inf')

    for i in range(n):
        for j in range(i, n):
            current_sum = 0
            for k in range(i, j+1):
                current_sum += arr[k]
            if current_sum > max_sub_arr_sum:
                max_sub_arr_sum = current_sum

    return max_sub_arr_sum               

# TC -> O(n^2)
# SC -> O(1)
def max_sub_arr_sum(arr: List[int]) -> int:
    n = len(arr)
    max_sub_arr_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]    
            if current_sum > max_sub_arr_sum:
                max_sub_arr_sum = current_sum

    return max_sub_arr_sum  

# TC -> O(n)
# SC -> O(1)
def max_sub_arr_sum(arr: List[int]) -> int:
    """Kadane's algorithm"""
    n = len(arr)
    max_sub_arr_sum = float('-inf')
    sum = 0

    for i in range(n):
        sum += arr[i]
        if sum > max_sub_arr_sum:
            max_sub_arr_sum = sum
        if sum < 0:
            sum = 0
    # Incase where we dont found the max_sub_arr_sum > 0.        
    if max_sub_arr_sum < 0:
        max_sub_arr_sum = 0
    
    return max_sub_arr_sum

# TC -> O(n)
# SC -> O(1)
# Printing the sub array with max sum.
def max_sub_arr_sum(arr: List[int]) -> int:
    """Kadane's algorithm"""
    n = len(arr)
    max_sub_arr_sum = float('-inf')
    sum = 0
    s = -1
    e = -1
    start = 0

    for i in range(n):
        # Starting index.
        if sum == 0:
            start = i
        sum += arr[i]
        if sum > max_sub_arr_sum:
            max_sub_arr_sum = sum
            s = start
            e = i
        if sum < 0:
            sum = 0

    print("The subarray is: [ ", end="")
    for i in range(s, e+1):
        print(arr[i], end=" ")
    print("]")

    # Incase where we dont found the max_sub_arr_sum > 0.        
    if max_sub_arr_sum < 0:
        max_sub_arr_sum = 0
    
    return max_sub_arr_sum



if __name__ == "__main__":
    print(max_sub_arr_sum([-2,1,-3,4,-1,2,1,-5,4]))
    print(max_sub_arr_sum([1]))
    print(max_sub_arr_sum([-4,-3,-2,-1]))