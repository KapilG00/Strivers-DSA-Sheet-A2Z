from typing import List


# Brute-force
# TC: O(n)
# SC: O(1)
def kth_missing_positive_number(arr: List[int], k: int) -> int:
    n = len(arr)

    for i in range(n):
        if arr[i] <= k:
            k += 1
        else: 
            break   

    return k     


# Optimal
# TC: O(n)
# SC: O(1)
def kth_missing_positive_number(arr: List[int], k: int) -> int:
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        no_of_missing_numbers = arr[mid]-(mid+1)

        if no_of_missing_numbers < k:
            low = mid+1
        else:
            high = mid-1    

    return high+1+k # For derivation, check notes.



if __name__ == "__main__":
    print(kth_missing_positive_number([4,7,9,10], 1))
    print(kth_missing_positive_number([4,7,9,10], 4))