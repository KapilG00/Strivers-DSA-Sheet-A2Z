from typing import List


# TC -> O(n^3)
# SC -> O(1)
def max_product_subarr_in_arr(arr: List[int]) -> int:
    n = len(arr)
    max_product = float('-inf')

    for i in range(n):
        for j in range(i+1, n):
            current_product = 1
            for k in range(i, j+1):
                current_product *= arr[k]
            max_product = max(current_product, max_product)
    return max_product

# TC -> O(n^2)
# SC -> O(1)
def max_product_subarr_in_arr(arr: List[int]) -> int:
    n = len(arr)
    max_product = float('-inf')

    for i in range(n):
        current_product = arr[i]
        for j in range(i+1, n):
            current_product *= arr[j]
            max_product = max(current_product, max_product)
    return max_product

# TC -> O(n)
# SC -> O(1)
def max_product_subarr_in_arr(arr: List[int]) -> int:
    n = len(arr)
    max_product = float('-inf')
    prefix_product, suffix_product = 1, 1

    for i in range(n):
        if prefix_product == 0:
            prefix_product = 1
        if suffix_product == 0:
            suffix_product = 1
        prefix_product *= arr[i]           # from front
        suffix_product *= arr[n-i-1]       # from back
        max_product = max(max_product, prefix_product, suffix_product)
    return max_product


if __name__ == "__main__":
    print(max_product_subarr_in_arr([1,2,3,4,5,0]))
    print(max_product_subarr_in_arr([1,2,-3,0,-4,-5]))
    print(max_product_subarr_in_arr([-2,3,4,-1,0,-2,3,1,4,0,4,6,-1,4]))