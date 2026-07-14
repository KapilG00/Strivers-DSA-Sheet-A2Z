from typing import List


# TC -> O(n^3)
# SC -> O(1)
# Brute-force
def count_sub_arrays_with_xor_k(arr: List[int], k: int) -> int:
    n = len(arr)
    sub_arrays_count = 0

    for i in range(n):
        for j in range(i, n):
            xor = 0
            for l in range(i, j+1):
                xor = xor ^ arr[l]

            if xor == k:
                sub_arrays_count += 1

    return sub_arrays_count            

# TC -> O(n^2)
# SC -> O(1)
# Better
def count_sub_arrays_with_xor_k(arr: List[int], k: int) -> int:
    n = len(arr)
    sub_arrays_count = 0

    for i in range(n):
        xor = 0
        for j in range(i, n):
            xor = xor ^ arr[j]

            if xor == k:
                sub_arrays_count += 1

    return sub_arrays_count  

# TC -> O(n)
# SC -> O(n)
# Optimal
def count_sub_arrays_with_xor_k(arr: List[int], k: int) -> int:
    n = len(arr)
    sub_arrays_count = 0
    xor_map = {0:1}
    prefix_xor = 0

    for i in range(n):
        prefix_xor ^= arr[i]

        rem = prefix_xor ^ k

        if rem in xor_map:
            sub_arrays_count += xor_map[rem]    

        if prefix_xor in xor_map:
            xor_map[prefix_xor] += 1
        else:
            xor_map[prefix_xor] = 1            
    
    return sub_arrays_count


if __name__ == "__main__":
    print(count_sub_arrays_with_xor_k([4,2,2,6,4], 6))
    print(count_sub_arrays_with_xor_k([5,6,7,8,9], 5))