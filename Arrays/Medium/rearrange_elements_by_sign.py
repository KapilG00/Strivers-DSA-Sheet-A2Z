from typing import List


# TC: O(n) + O(n/2)
# SC: O(n/2) + O(n/2)
# Brute-force
def rearrange_alternately_by_sign(arr: List[int]) -> List[int]:
    pos_ele_arr = []
    neg_ele_arr = []
    n = len(arr)

    for i in range(n):
        if arr[i] < 0:
            neg_ele_arr.append(arr[i])
        else:
            pos_ele_arr.append(arr[i])

    for j in range(len(pos_ele_arr)):
        arr[2*j] = pos_ele_arr[j]
        arr[2*j+1] = neg_ele_arr[j]

    return arr

# TC: O(n)
# SC: O(n)
# Optimal
def rearrange_alternately_by_sign(arr: List[int]) -> List[int]:
    "We know that the resultant array must start from a positive element."
    n = len(arr)
    pos_idx = 0
    neg_idx = 1
    result_arr = [0] * n

    for i in range(n):
        if arr[i] > 0:
            result_arr[pos_idx] = arr[i]
            pos_idx += 2
        else:
            result_arr[neg_idx] = arr[i]
            neg_idx += 2

    return result_arr            



if __name__ == "__main__":
    print(rearrange_alternately_by_sign([1,2,-4,-5]))
    print(rearrange_alternately_by_sign([1,2,-3,-1,-2,3]))