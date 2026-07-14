from typing import List


def func(arr1: List[int], arr2: List[int]) -> int:
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

    print(arr1)
    print(arr2)
    
    



if __name__ == "__main__":
    print(func([-5,-2,4,5], [-3,1,8]))
    