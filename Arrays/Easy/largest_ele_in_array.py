from typing import List

# TC -> O(nlogn)
# SC -> O(1)
def find_largest_ele_in_arr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]

# TC -> O(n)
# SC -> O(1)
def find_largest_ele_in_arr(arr: List[int]) -> int:
    largest = arr[0]
    n = len(arr)

    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]

    return largest        


if __name__ == "__main__":
    print(find_largest_ele_in_arr([2,5,1,3,0]))