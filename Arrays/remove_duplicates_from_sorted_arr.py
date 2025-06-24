from typing import List


# Time complexity: O(n^2)
# Space Complexity: O(n)
def remove_duplicates_from_sorted_arr(arr: List[int]) -> List[int]:
    n = len(arr)
    non_duplicate_arr = []

    for i in range(n):
        if arr[i] not in non_duplicate_arr:
            non_duplicate_arr.append(arr[i])
    
    m = len(non_duplicate_arr)

    for _ in range(n-m):
        non_duplicate_arr.append("_")

    return non_duplicate_arr

# Time complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates_from_sorted_arr(arr: List[int]) -> List[int]:
    n = len(arr)
    non_duplicate_arr = [arr[0]]

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            non_duplicate_arr.append(arr[i])
    
    m = len(non_duplicate_arr)

    for _ in range(n-m):
        non_duplicate_arr.append("_")        

    return non_duplicate_arr
     

if __name__ == "__main__":
    print(remove_duplicates_from_sorted_arr([1,1,2,2,2,3,3]))