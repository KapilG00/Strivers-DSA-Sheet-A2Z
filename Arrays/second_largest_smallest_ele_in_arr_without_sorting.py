from typing import List

# Brute-force approach (Using sorting approach)
# Time Complexity: O(NlogN) for sorting the array
# Space Complexity: O(1)
# Note: This approach only works if there are no duplicates in array.
def second_largest_smallest_ele(arr: List[int]) -> tuple[int, int]:
    n = len(arr)

    if n == 0 or n == 1:
        return (-1, -1)
    
    arr.sort()
    return arr[1], arr[n-2]

# Better approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def second_largest_smallest_ele(arr: List[int]) -> tuple[int, int]:
    n = len(arr)

    if n == 0 or n == 1:
        return (-1, -1)
    
    smallest_ele, largest_ele = float('inf'), float('-inf')
    second_smallest_ele, second_largest_ele = float('inf'), float('-inf')
     
    # Finding the smallest and largest ele.
    for i in range(n):
        smallest_ele = min(smallest_ele, arr[i])
        largest_ele = max(largest_ele, arr[i])

    for j in range(n):
        # Finding second smallest ele.    
        if arr[j] < second_smallest_ele and arr[j] != smallest_ele:
            second_smallest_ele = arr[j]
        # Finding second largest ele.
        elif arr[j] > second_largest_ele and arr[j] != largest_ele:
            second_largest_ele = arr[j]
        
    return second_smallest_ele, second_largest_ele          

# Optimal approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def second_smallest_ele(arr: List[int], n: int) -> int:
    smallest_ele = float('inf')
    second_smallest_ele = float('inf')

    for i in range(n):
        if arr[i] < smallest_ele:
            second_smallest_ele = smallest_ele
            smallest_ele = arr[i]
        elif arr[i] < second_smallest_ele and arr[i] != smallest_ele:
            second_smallest_ele = arr[i]

    return second_smallest_ele        

def second_largest_ele(arr: List[int], n: int) -> int:
    largest_ele = float('-inf')
    second_largest_ele = float('-inf')

    for i in range(n):
        if arr[i] > largest_ele:
            second_largest_ele = largest_ele
            largest_ele = arr[i]
        elif arr[i] > second_largest_ele and arr[i] != largest_ele:
            second_largest_ele = arr[i]

    return second_largest_ele        

def second_largest_smallest_ele(arr: List[int]) -> tuple[int, int]:
    n = len(arr)

    if n == 0 or n == 1:
        return (-1, -1)
    
    second_smallest_element = second_smallest_ele(arr, n)
    second_largest_element = second_largest_ele(arr, n)

    return second_smallest_element, second_largest_element



if __name__ == "__main__":
    print(second_largest_smallest_ele([1, 2, 4, 3, 7, 5])) # To test brute-force only.
    print(second_largest_smallest_ele([1, 2, 4, 7, 7, 5]))
    print(second_largest_smallest_ele([1]))