from typing import List
from collections import deque


# TC: O(n)
# SC: O(k) 
def find_first_negative_in_every_window_of_size_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    low = 0
    high = 0
    first_negative_ele_arr = []
    dq = deque()
    
    while high < n:
        if arr[high] < 0:
            dq.append(high)

        if (high-low+1) == k:
            if dq:
                first_negative_ele_arr.append(arr[dq[0]])
            else:
                first_negative_ele_arr.append(0)

            if dq and dq[0] == low:
                dq.popleft()

            low += 1
        high += 1        

    return first_negative_ele_arr
        



if __name__ == "__main__":
    print(find_first_negative_in_every_window_of_size_k([-8,2,3,-6,1], 2))
    print(find_first_negative_in_every_window_of_size_k([4,1,1], 2))