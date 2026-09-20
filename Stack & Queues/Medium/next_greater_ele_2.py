# Brute-force
# TC: O(n^2)
# SC: O(n)
def nge_2(arr: list[int]) -> list[int]:
    n = len(arr)
    nge_arr = [-1] * n

    for i in range(n):
        curr_ele = arr[i]
        for j in range(1, n):
            # This formula will help us to compare with
            # each index, other than itself and modulo
            # helps to have a circular nature of the array.
            idx = (i + j) % n

            if arr[idx] > curr_ele:
                nge_arr[i] = arr[idx]
                break

    return nge_arr


# Optimal (Using monotonically decreasing stack)
# TC: O(2n)
# SC: O(n) + O(n)
def nge_2(arr: list[int]) -> list[int]:
    n = len(arr)
    stack = []
    nge_arr = [0] * n

    for i in range(2 * n - 1, -1, -1):
        idx = i % n
        curr_ele = arr[idx]

        while len(stack) > 0 and stack[-1] <= curr_ele:
            stack.pop()

        if i < n:
            if len(stack) == 0:
                nge_arr[i] = -1
            else:
                nge_arr[i] = stack[-1]

        # Adding elements into stack.
        stack.append(curr_ele)

    return nge_arr


if __name__ == "__main__":
    print(nge_2([5, 7, 1, 7, 6, 0]))
