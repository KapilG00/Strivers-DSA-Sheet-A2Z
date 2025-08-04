from typing import List

# TC -> O(n^2)
# SC -> O(1)
def majority_occurs_more_than_half_of_arr_size(arr: List[int]) -> int:
    n = len(arr)
    N = n // 2

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1
        if count > N:
            return arr[i]
    return -1

# TC -> O(nlogn)
# SC -> O(m); where "m" is the size of an hashmap.
def majority_occurs_more_than_half_of_arr_size(arr: List[int]) -> int:
    n = len(arr)
    N = n // 2
    ele_freq_map = {}

    for i in range(n):
        if arr[i] in ele_freq_map:
            ele_freq_map[arr[i]] += 1
        else:
            ele_freq_map[arr[i]] = 1
    for k, v in ele_freq_map.items():
        if v > N:
            return k
    return -1                
            
# TC -> O(n)
# SC -> O(1)
# Moore's Voting Algorithm
def majority_occurs_more_than_half_of_arr_size(arr: List[int]) -> int:
    n = len(arr)
    N = n / 2
    count = 0
    ele = 0

    for i in range(n):
        if count == 0:
            ele = arr[i]
            count = 1
        elif ele == arr[i]:
            count += 1
        else:
            count -= 1

    counter = 0
    for j in range(n):
        if arr[j] == ele:
            counter += 1
    if counter > (n/2):
        return ele     

    return -1       


if __name__ == "__main__":
    print(majority_occurs_more_than_half_of_arr_size([3,2,3]))
    print(majority_occurs_more_than_half_of_arr_size([2,2,1,1,1,2,2]))
    print(majority_occurs_more_than_half_of_arr_size([4,4,2,4,3,4,4,3,2,4]))