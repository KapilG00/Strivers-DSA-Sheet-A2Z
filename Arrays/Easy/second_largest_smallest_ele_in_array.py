from typing import List


# TC -> O(nlogn) + O(n) + O(n) = O(n log n)
# SC -> O(1)
# Brute-force approach.
def find_second_largest_smallest_ele_in_arr(arr: List[int]) -> tuple[int, int]:
    n = len(arr)
    arr.sort()
    largest_ele = arr[-1]
    smallest_ele = arr[0]
    second_largest = 0
    second_smallest = 0

    for i in range(n-1,0,-1):
        if arr[i] < largest_ele:
            second_largest = arr[i]
            break

    for i in range(n):
        if arr[i] > smallest_ele:
            second_smallest = arr[i]
            break    

    return (second_largest, second_smallest)    

# TC -> O(n) + O(n) = O(n)
# SC -> O(1)
# Better approach.
def find_second_largest_smallest_ele_in_arr(arr: List[int]) -> tuple[int, int]:
    n = len(arr)
    smallest = float('inf')
    second_smallest = float('inf')
    largest = float('-inf')
    second_largest = float('-inf')

    for i in range(n):
        smallest = min(smallest, arr[i])
        largest = max(largest, arr[i])

    for i in range(n):
        if arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]
        if arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return (second_largest, second_smallest)

# TC -> O(n) + O(n) = O(n)
# SC -> O(1)
# Optimal approach.
def find_second_largest(arr: List[int], n: int) -> int:
    largest = float('-inf')
    second_largest = float('-inf')

    for i in range(n):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest        

def find_second_smallest(arr: List[int], n: int) -> int:
    smallest = float('inf')
    second_smallest = float('inf') 

    for i in range(n):
        if arr[i] < smallest:
            second_smallest = smallest
            smallest = arr[i]
        elif arr[i] < second_smallest and arr[i] != smallest:
            second_smallest = arr[i]

    return second_smallest            

def find_second_largest_smallest_ele_in_arr(arr: List[int]) -> tuple[int, int]:
    n = len(arr)
    second_largest = find_second_largest(arr, n)
    second_smallest = find_second_smallest(arr, n)
    
    return (second_largest, second_smallest)


if __name__ == "__main__":
    print(find_second_largest_smallest_ele_in_arr([1,2,4,7,7,5]))