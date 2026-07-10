from typing import List


def func(arr: List[int]) -> int:
    n = len(arr)
    leaders_array = []

    max_from_right = arr[n-1]
    leaders_array.append(max_from_right)

    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders_array.append(max_from_right)
    
    return leaders_array



if __name__ == "__main__":
    print(func([4,7,1,0]))
    print(func([10,22,12,3,0,6]))