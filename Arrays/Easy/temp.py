from typing import List

# brute-force (O(n)+O(n-k), O(n))
def temp(arr: List[int]) -> int:
    n = len(arr)
    temp_arr = []

    for i in range(n):
        if arr[i] != 0:
            temp_arr.append(arr[i])
    
    k = len(temp_arr)
    for _ in range(n-k):
        temp_arr.append(0)

    return temp_arr    

# optimal
def temp(arr: List[int]) -> int:
    n = len(arr)
    j = -1

    # Find the first zero
    for k in range(len(arr)):
        if arr[k] == 0:
            j = k
            break

    # If no zero found, return
    if j == -1:
        return

    for i in range(j+1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return arr        

    


if __name__ == "__main__":
    print(temp([1,0,2,3,0,4,0,1]))