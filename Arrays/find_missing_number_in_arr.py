from typing import List

# TC -> O(n^2)
# SC -> O(1)
def find_missing_number_in_arr(arr: List[int], N: int) -> int:
    for i in range(1, N+1):
        if i not in arr:
            return i

    return -1

# TC -> O(n^2)
# SC -> O(1)
def find_missing_number_in_arr(arr: List[int], N: int) -> int:
    for i in range(1, N+1):
        missing_number_found = False

        for j in range(len(arr)):
            if arr[j] == i:
                missing_number_found = True
                break

        if not missing_number_found:
            return i    

    return -1

# Using hash array.
# TC -> O(n) + O(n) ~ O(2n)
# SC -> O(n)
def find_missing_number_in_arr(arr: List[int], N: int) -> int:
    hash_arr = [0] * (N+1)
    
    for i in range(len(arr)):
        hash_arr[arr[i]] += 1  

    for j in range(1, len(hash_arr)):
        if hash_arr[j] == 0:
            return j

    return -1        

# Using sum of natural numbers formula.
# TC -> O(n)
# SC -> O(1)
def find_missing_number_in_arr(arr: List[int], N: int) -> int:
    arr_sum = 0
    for i in range(len(arr)):
        arr_sum += arr[i]

    natural_sum = N*(N+1) // 2
    missing_number = natural_sum - arr_sum

    if missing_number == 0:
        return -1

    return missing_number    



if __name__ == "__main__":
    print(find_missing_number_in_arr([1,2,4,5], 5))
    print(find_missing_number_in_arr([1,3], 3))
    print(find_missing_number_in_arr([1,2], 2))