from typing import List


# TC: O(n+m) + O(n+m)    
# SC: O(n+m)
# Brute-force
def merge_two_sorted_arrays_without_extra_space(arr1: List[int], arr2: List[int]) -> List[int]:
    n = len(arr1)
    m = len(arr2)
    arr = []
    i, j = 0, 0

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            arr.append(arr2[j])
            j += 1

    # for remaining elements of arr1
    while i < n:
        arr.append(arr1[i])
        i += 1

    # for remaining elements of arr2        
    while j < m:
        arr.append(arr2[j])
        j += 1

    # Put back the elements from arr to arr1 and arr2 in ascending order.
    p = len(arr)
    q = 0

    while q < p:
        if q < n:
            arr1[q] = arr[q]
        else:
            arr2[q-n] = arr[q]
        q += 1         

    return (arr1, arr2)  

# TC: O(n+m) + O(n+m)    
# SC: O(n+m)
# Brute-force
def merge_two_sorted_arrays_without_extra_space(arr1: List[int], arr2: List[int]) -> List[int]:
    n = len(arr1)
    m = len(arr2)
    arr = [0] * (n+m)
    i, j = 0, 0
    idx = 0

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            arr[idx] = arr1[i]
            i += 1
            idx += 1
        else:
            arr[idx] = arr2[j]
            j += 1
            idx += 1

    # for remaining elements of arr1
    while i < n:
        arr[idx] = arr1[i]
        idx += 1
        i += 1

    # for remaining elements of arr2        
    while j < m:
        arr[idx] = arr2[j]
        idx += 1
        j += 1

    # Put back the elements from arr to arr1 and arr2 in ascending order.
    p = len(arr)
    q = 0

    while q < p:
        if q < n:
            arr1[q] = arr[q]
        else:
            arr2[q-n] = arr[q]
        q += 1         

    return (arr1, arr2)  

# TC: O(min(n,m)) + O(nlogn) + O(mlogm)    
# SC: O(1)
# Optimal
def merge_two_sorted_arrays_without_extra_space(arr1: List[int], arr2: List[int]) -> tuple[List[int], List[int]]:
    n = len(arr1)
    m = len(arr2)
    i = n-1
    j = 0

    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        else:
            break

    arr1.sort()
    arr2.sort()    

    return (arr1, arr2)  


if __name__ == "__main__":
    print(merge_two_sorted_arrays_without_extra_space([-5,-2,4,5], [-3,1,8]))
    