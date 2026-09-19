# TC: O(2n)
# SC: O(n) + O(n)
def next_greater_ele(arr: list[int]) -> list[int]:
    n = len(arr)
    stack = []
    next_greater_ele_arr = [0] * n

    for i in range(n - 1, -1, -1):
        # Pop the elements from stack until stack is not empty
        # and stack top most element is less than or equal to current element
        # of an input array.
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()

        # Add the -1 in the output array if next greater element doesn't exists.
        if len(stack) == 0:
            next_greater_ele_arr[i] = -1
        # Add the top most element of stack into the output array.
        else:
            next_greater_ele_arr[i] = stack[-1]

        # Add the current value in the stack.
        stack.append(arr[i])

    return next_greater_ele_arr


if __name__ == "__main__":
    print(next_greater_ele([1, 3, 2, 4]))
