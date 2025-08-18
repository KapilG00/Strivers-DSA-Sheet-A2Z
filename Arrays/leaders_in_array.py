from typing import List


# TC -> O(n^2)
# SC -> O(1)
def leaders_in_arr(arr: List[int]) -> None:
    n = len(arr)

    for i in range(n):
        is_leader = True
        for j in range(i+1, n):
            if arr[i] <= arr[j]:
                is_leader = False
                break
        if is_leader:
            print(f"{arr[i]} is a leader.")        
    
    return 0

# TC -> O(n)
# SC -> O(1)
def leaders_in_arr(arr: List[int]) -> None:
    n = len(arr)

    max_from_right = arr[n-1]
    print(f"{max_from_right} is a leader")

    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            print(f"{arr[i]} is a leader.")
    
    return 0         



if __name__ == "__main__":
    print(leaders_in_arr([4,7,1,0]))
    print(leaders_in_arr([10,22,12,3,0,6]))