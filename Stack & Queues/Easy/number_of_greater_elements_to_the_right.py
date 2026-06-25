from typing import List

# TC: O(n^2)
# SC: O(n)
def number_of_greater_elements_to_right(arr: List[int]) -> List[int]:
    n = len(arr)
    greater_ele_arr = [-1] * n

    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                greater_ele_arr[i] = arr[j]
                break       

    return greater_ele_arr        

# TC: O(n)
# SC: O(n)
# Monotonically decreasing stack.
def number_of_greater_elements_to_right(arr: List[int]) -> List[int]:
    n = len(arr)
    greater_ele_arr = [-1] * n
    stack = []

    for i in range(n-1,-1,-1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
            
        if stack:
            greater_ele_arr[i] = stack[-1]

        stack.append(arr[i])

    return greater_ele_arr




if __name__ == "__main__":
    print(number_of_greater_elements_to_right([1,3,2,4]))
    print(number_of_greater_elements_to_right([6,8,0,1,3]))