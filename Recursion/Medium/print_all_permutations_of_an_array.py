from typing import List


# TC: O(n!) * O(n)
# SC: O(n!) * [O(n) + O(n)] = O(n!) * O(n)
def print_all_permutations(arr: List[int], permutations_arr: List[int], permute_arr: List[int], bool_arr: List[bool]) -> List[int]:
    n = len(arr)
    
    # base case
    if len(permute_arr) == n:
        permutations_arr.append(permute_arr.copy())
        # print(permute_arr)
        return
    
    for i in range(n):
        if not bool_arr[i]:
            bool_arr[i] = True
            permute_arr.append(arr[i])
            print_all_permutations(arr, permutations_arr, permute_arr, bool_arr)
            permute_arr.pop()
            bool_arr[i] = False

def start_permute(arr: List[int]):
    n = len(arr)
    permutations_arr = []
    permute_arr = []
    bool_arr = [False] * n
    print_all_permutations(arr, permutations_arr, permute_arr, bool_arr)
    return permutations_arr

# TC: O(n!) * O(n)
# SC: O(n!) * O(n)
def print_all_permutations(arr: List[int], permutations_arr: List[int], idx: int) -> List[int]:
    n = len(arr)
    
    # base case
    if idx == n:
        permutations_arr.append(arr.copy())
        return
    
    for i in range(idx, n):
        arr[idx], arr[i] = arr[i], arr[idx] # Choose
        print_all_permutations(arr, permutations_arr, idx+1)
        arr[idx], arr[i] = arr[i], arr[idx] # Undo (backtrack)

def start_permute(arr: List[int]):
    permutations_arr = []
    print_all_permutations(arr, permutations_arr, 0)
    return permutations_arr



if __name__ == "__main__":
    print(start_permute([1,3,2]))
    print(start_permute([4,5,3,1,2]))
    print(start_permute([1,0,-3,2]))