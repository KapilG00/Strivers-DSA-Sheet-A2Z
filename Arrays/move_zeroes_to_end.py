from typing import List

# Brute-force approach
# TC -> O(n)
# SC -> O(n)
def move_zeroes_to_end(arr: List[int]) -> List[int]:
    n = len(arr)
    new_arr = []

    for i in range(n):
        if arr[i] != 0:
            new_arr.append(arr[i])
    m = len(new_arr)

    for _ in range(n-m):
        new_arr.append(0)

    return new_arr    

# Optimal approach
# TC -> O(n)
# SC -> O(1)
def move_zeroes_to_end(arr: List[int]) -> List[int]:
    n = len(arr)
    j = -1
    
    for k in range(n):
        if arr[k] == 0:
            j = k
            break

    if j == -1:
        return arr    
     
    i = j+1

    while i < n:
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1

    return arr    


if __name__ == "__main__":
    print(move_zeroes_to_end([1,0,2,3,0,4,0,1]))
    print(move_zeroes_to_end([1,2,0,1,0,4,0]))