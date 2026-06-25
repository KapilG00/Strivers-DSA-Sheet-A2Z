# TC: O(n)
# SC: O(N)
def number_of_greater_elements_to_right(arr: List[int]) -> List[int]:
    n = len(arr)
    greater_ele_arr = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            poped_idx = stack.pop()
            greater_ele_arr[poped_idx] = arr[i]
        stack.append(i)

    return greater_ele_arr



if __name__ == "__main__":
    print(infix_to_postfix("a+b*(c^d-e)"))
    print(infix_to_postfix("h^m^q^(7-4)"))
    print(infix_to_postfix("h+m+q+(7-4)"))