from typing import List

# TC -> O(n^3) 
# SC -> O(1)
# Brute-force
def max_sub_arr_sum(arr: List[int]) -> int:
    n = len(arr)
    max_subarr_sum = float('-inf')
    
    for i in range(n):
        for j in range(i, n):
            current_sub_arr_sum = 0
            for k in range(i, j+1):
                current_sub_arr_sum += arr[k]

            if current_sub_arr_sum > max_subarr_sum:
                max_subarr_sum = current_sub_arr_sum

    return max_subarr_sum                

# TC -> O(n^2) 
# SC -> O(1)
# Better
def max_sub_arr_sum(arr: List[int]) -> int:
    n = len(arr)
    max_subarr_sum = float('-inf')
    
    for i in range(n):
        current_sub_arr_sum = 0
        for j in range(i, n):
            current_sub_arr_sum += arr[j]

            if current_sub_arr_sum > max_subarr_sum:
                max_subarr_sum = current_sub_arr_sum

    return max_subarr_sum

# TC -> O(n)
# SC -> O(1)
# Optimal (using kadane's algorithm)
def max_sub_arr_sum(arr: List[int]) -> int:
    n = len(arr)
    sum = 0
    max_subarr_sum = float('-inf')

    for i in range(n):
        sum += arr[i]
        
        if sum > max_subarr_sum:
            max_subarr_sum = sum

        # There is no need to add negative number to our sum because it will make
        # our max sub array sum more small.
        if sum < 0:
            sum = 0

    return max_subarr_sum        

# TC -> O(n)
# SC -> O(1)
# Optimal (using kadane's algorithm)
# Follow-up: if question asks to return for sub array with max sum.
def max_sub_arr_sum(arr: List[int]) -> tuple[int, int]:
    n = len(arr)
    sum = 0
    start = 0
    max_subarr_sum = float('-inf')
    max_sum_subarr_start_idx = -1
    max_sum_subarr_end_idx = -1

    for i in range(n):
        if sum == 0:
            start = i

        sum += arr[i]
        
        if sum > max_subarr_sum:
            max_subarr_sum = sum
            max_sum_subarr_start_idx = start
            max_sum_subarr_end_idx = i
            
        # There is no need to add negative number to our sum because it will make
        # our max sub array sum more small.
        if sum < 0:
            sum = 0

    return (max_sum_subarr_start_idx, max_sum_subarr_end_idx)



if __name__ == "__main__":
    print(max_sub_arr_sum([2,3,5,-2,7,-4]))
    print(max_sub_arr_sum([-2,-3,-7,-2,-10,-4]))
