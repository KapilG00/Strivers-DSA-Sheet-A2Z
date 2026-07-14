from typing import List


# TC -> O(n) + O(n) + O(nlogn) = O(2n) + O(nlogn)
# SC -> O(n)
# Brute-force
def merge_overlapping_subintervals(arr: List[int]) -> List[List[int]]:
    n = len(arr)
    arr.sort() # O(nlogn)
    non_overlapping_intervals = []

    for i in range(n): # O(n)
        current_interval_start = arr[i][0]
        current_interval_end = arr[i][1]

        if non_overlapping_intervals and current_interval_end <= non_overlapping_intervals[-1][1]:
            continue

        for j in range(i+1, n): # O(n)
            if arr[j][0] <= current_interval_end:
                current_interval_end = max(current_interval_end, arr[j][1])
            else:
                break

        non_overlapping_intervals.append((current_interval_start, current_interval_end))        

    return non_overlapping_intervals 
    
# TC -> O(n) + O(nlogn)
# SC -> O(n)
# Optimal
def merge_overlapping_subintervals(arr: List[int]) -> int:
    n = len(arr)
    arr.sort() # O(nlogn)
    non_overlapping_intervals = []

    for i in range(n): # O(n)
        if not non_overlapping_intervals or arr[i][0] > non_overlapping_intervals[-1][1]:
            non_overlapping_intervals.append((arr[i]))
        else:
            non_overlapping_intervals[-1][1] = max(non_overlapping_intervals[-1][1], arr[i][1])      

    return non_overlapping_intervals 
    



if __name__ == "__main__":
    print(merge_overlapping_subintervals([[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]))
    print(merge_overlapping_subintervals([[1,3],[2,6],[8,10],[15,18]]))
    print(merge_overlapping_subintervals([[1,4],[4,5]]))