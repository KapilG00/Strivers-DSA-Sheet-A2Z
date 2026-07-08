from typing import List

# TC -> O(n) + O(k); where k=n; 
# SC -> O(1)
# Brute-force
def sort_0s_1s_2s(arr: List[int]) -> List[int]:
    n = len(arr)
    counter_0s = 0
    counter_1s = 0 
    counter_2s = 0

    for i in range(n):
        if arr[i] == 0:
            counter_0s += 1
        elif arr[i] == 1:
            counter_1s += 1
        else:
            counter_2s += 1
    
    # Below code takes O(k)
    idx = 0
    while counter_0s:
        arr[idx] = 0
        idx += 1
        counter_0s -= 1

    while counter_1s:
        arr[idx] = 1
        idx += 1
        counter_1s -= 1

    while counter_2s:
        arr[idx] = 2
        idx += 1
        counter_2s -= 1

    return arr            
    
# TC -> O(n)
# SC -> O(1)
# Optimal (using dutch national flag algorithm)
def sort_0s_1s_2s(arr: List[int]) -> List[int]:
    n = len(arr)
    l, h, m = 0, n-1, 0

    while m < h:
        if arr[m] == 0:
            # swap
            arr[l], arr[m] = arr[m], arr[l]
            l += 1
            m += 1
        elif arr[m] == 2:
            # swap
            arr[h], arr[m] = arr[m], arr[h]
            h -= 1
        else:
            m += 1

    return arr                



if __name__ == "__main__":
    print(sort_0s_1s_2s([1,0,2,1,0]))
