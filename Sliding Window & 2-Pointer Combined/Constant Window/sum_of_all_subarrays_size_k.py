from typing import List


# TC: O(k) + O(n-k)
# SC: O(1)
def print_sum_of_all_sub_arr_of_size_k(arr: List[int], k: int) -> None:
    n = len(arr)
    low = 0
    high = k-1
    window_sum = 0

    for i in range(low, high+1):
        window_sum += arr[i]

    print("current window_sum is:", window_sum)    

    while high < n-1:
        print(arr[low:high+1])
        
        window_sum -= arr[low]
        low += 1
        high += 1
        window_sum += arr[high]
        print("current window_sum is:", window_sum)   



if __name__ == "__main__":
    print(print_sum_of_all_sub_arr_of_size_k([1,2,3,4,5,6], 3))
    print(print_sum_of_all_sub_arr_of_size_k([1,-2,3,-4,5,6], 2))