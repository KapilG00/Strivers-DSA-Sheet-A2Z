# Nearest element in the array such that the element
# has an index smaller than current element.

# Need to check for smaller than current element
# on the left side of the current element.


def next_smaller_ele(arr: list[int]) -> list[int]:
    n = len(arr)
    stack = []
    next_smaller_ele_arr = [0] * n
    i = 0

    while i < n:
        while len(stack) > 0 and stack[-1] >= arr[i]:
            stack.pop()

        if len(stack) == 0:
            next_smaller_ele_arr[i] = -1
        else:
            next_smaller_ele_arr[i] = stack[-1]

        stack.append(arr[i])

        i += 1

    return next_smaller_ele_arr


if __name__ == "__main__":
    print(next_smaller_ele([4, 5, 2, 10, 8]))
    print(next_smaller_ele([3, 2, 1]))
