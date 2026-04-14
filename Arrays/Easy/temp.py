from typing import List

# Brute-force approach. (not in-place)
# def temp(arr: List[int]) -> int:
#     n = len(arr)
#     new_arr = [arr[0]]

#     for i in range(1, n):
#         if arr[i] > arr[i-1]:
#             new_arr.append(arr[i])

#     return len(new_arr) 

# Brute-force approach. (in-place)
# def temp(arr: List[int]) -> int:
#     index = 0
#     s = set()

#     for num in arr:
#         if num not in s:
#             s.add(num)
#             arr[index] = num
#             index += 1
#     return index

# Optimal approach. (in-place)
def temp(arr: List[int]) -> int:
    n = len(arr)
    i = 0

    for j in range(1, n):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i+1        



    


if __name__ == "__main__":
    print(temp([1,1,2,2,2,3,3]))