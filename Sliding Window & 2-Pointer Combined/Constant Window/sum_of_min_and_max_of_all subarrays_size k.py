from typing import List
from collections import deque


# TC: O(n)
# SC: O(k)
def sum_of_min_max_all_sub_arrs_of_size_k(arr: List[int], k: int) -> int:
    n = len(arr)
    low = 0
    high = 0
    min_dq = deque()  # increasing order indices
    max_dq = deque()  # decreasing order indices
    total_sum = 0

    while high < n:
        # Maintain min deque
        while min_dq and arr[min_dq[-1]] >= arr[high]:
            min_dq.pop()

        # Maintain max deque
        while max_dq and arr[max_dq[-1]] <= arr[high]:
            max_dq.pop()

        min_dq.append(high)
        max_dq.append(high)

        # Window of size k formed
        if (high-low+1) == k:

            window_min = arr[min_dq[0]]
            window_max = arr[max_dq[0]]

            window_sum = window_min + window_max
            total_sum += window_sum

            # Remove outgoing element
            if min_dq and min_dq[0] == low:
                min_dq.popleft()

            if max_dq and max_dq[0] == low:
                max_dq.popleft()

            low += 1

        high += 1

    return total_sum  



if __name__ == "__main__":
    print(sum_of_min_max_all_sub_arrs_of_size_k([2,5,-1,7,-3,-1,-2], 4))
    print(sum_of_min_max_all_sub_arrs_of_size_k([1,-2,3,-4,5,6], 2))