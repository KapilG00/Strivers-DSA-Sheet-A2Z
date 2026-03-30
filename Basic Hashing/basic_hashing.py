from typing import List

# TC: O(n), SC: O(n)
def freq_of_numbers(arr: List[int]) -> dict[int, int]:
    freq_dict = {}
    n = len(arr)

    for i in range(n):
        if arr[i] not in freq_dict:
            freq_dict[arr[i]] = 1
        else:
            freq_dict[arr[i]] += 1

    return freq_dict            


if __name__ == "__main__":
    print(freq_of_numbers([10,5,10,15,10,5]))