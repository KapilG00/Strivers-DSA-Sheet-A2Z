from typing import List


# TC - O(n)
# SC - O(k)
def rotate_arr_by_k_places_right_left(arr: List[int], k: int, direction: str) -> List[int]:
    n = len(arr)

    if n == 0:
      return
    
    k = k % n
    temp_arr = [0] * k

    if direction == "left":
        for i in range(k):
            temp_arr[i] = arr[i]      # arr -> [1,2,3,4,5,6,7], temp_arr -> [1,2]
        for j in range(n-k):
            arr[j] = arr[j+k]         # arr -> [3,4,5,6,7,6,7], temp_arr -> [1,2]
        for l in range(n-k, n):
            arr[l] = temp_arr[l-n+k]  # arr -> [3,4,5,6,7,1,2], temp_arr -> [1,2]
    elif direction == "right":
        for i in range(k):
            temp_arr[i] = arr[n-k+i]  # arr -> [1,2,3,4,5,6,7], temp_arr -> [6,7]
        for j in range(n-k-1, -1, -1):
            arr[j+k] = arr[j]         # arr -> [1,2,1,2,3,4,5], temp_arr -> [6,7]
        for l in range(k):
            arr[l] = temp_arr[l]      # arr -> [6,7,1,2,3,4,5], temp_arr -> [6,7]        

    return arr


def reverse(arr: List[int], start: int, stop: int) -> None:
    while start < stop:
        temp = arr[start]
        arr[start] = arr[stop]
        arr[stop] = temp

        start += 1
        stop -= 1

# TC - O(n)
# SC - O(1)
def rotate_arr_by_k_places_right_left(arr: List[int], k: int, direction: str) -> List[int]:
    n = len(arr)

    if n == 0:
      return
    
    if direction == "left":
        reverse(arr, 0, k-1)   # reversing first k elements of an array.
        reverse(arr, k, n-1)   # reversing last n-k elements of an array.
        reverse(arr, 0, n-1)   # reversing the whole array.
    elif direction == "right":
        reverse(arr, n-k, n-1) # reversing last k elements of an array.
        reverse(arr, 0, n-k-1)   # reversing first n-k elements of an array.
        reverse(arr, 0, n-1)   # reversing the whole array.

    return arr




if __name__ == "__main__":
    print(rotate_arr_by_k_places_right_left([1,2,3,4,5,6,7], 2, "left"))
    print(rotate_arr_by_k_places_right_left([1,2,3,4,5,6,7], 2, "right"))    