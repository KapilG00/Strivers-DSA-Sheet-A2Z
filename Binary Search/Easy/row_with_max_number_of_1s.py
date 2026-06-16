from typing import List


def lower_bound(arr: List[int], target: int) -> int:
    k = len(arr)
    low = 0
    high = k-1
    count_of_ls = k

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] >= target:
            count_of_ls = mid
            high = mid-1
        else:
            low = mid+1
    print("lower bound returned value is: ", count_of_ls)
    return count_of_ls        

# TC -> O(nlogm)
# SC -> O(1)
def find_row_with_max_1s(arr: List[int], rows: int, columns: int) -> int:
    max_1s = 0
    idx = -1

    for i in range(rows):
        count_1s = columns - lower_bound(arr[i], 1)
        print(f"current count of 1s in a current {i}th row is: ", count_1s)
        if count_1s > max_1s:
            max_1s = count_1s
            idx = i

    return idx        
    
        

if __name__ == "__main__":
    print(find_row_with_max_1s([[1,1,1], [0,0,1], [0,0,0]], 3, 3))
    print(find_row_with_max_1s([[0,0], [0,0]], 2, 2))