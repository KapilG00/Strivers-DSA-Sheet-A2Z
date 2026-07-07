from typing import List


def func(arr: List[int], sum: int) -> List[int]:
    n = len(arr)
    max_length = 0
    l, r = 0, 0
    prefix_sum = arr[0]

    while r < n:
        # If the sum exceeds K, shrink the window
        while l <= r and prefix_sum > sum:
            prefix_sum -= arr[l]
            l += 1

        if prefix_sum == sum:
            max_length = max(max_length, r-l+1)

        r += 1
        if r < n:
            prefix_sum += arr[r] 

    return max_length        



if __name__ == "__main__":
    print(func([10,5,2,7,1,9], 10))
    print(func([-3,2,1], 6))