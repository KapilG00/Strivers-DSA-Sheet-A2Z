from typing import List


def highest_lowest_freq_elements(arr: List[int]) -> tuple[int, int]:
    freq_dict = {}
    n = len(arr)

    for i in range(n):
        if arr[i] not in freq_dict:
            freq_dict[arr[i]] = 1
        else:
            freq_dict[arr[i]] += 1
    
    highest_ele = 0
    lowest_ele = 0
    highest_freq = 0
    lowest_freq = n
    
    for k, v in freq_dict.items():
        if v > highest_freq:
            highest_freq = v
            highest_ele = k
        elif v < lowest_freq:
            lowest_freq = v
            lowest_ele = k

    return (highest_ele, lowest_ele)        



if __name__ == "__main__":
    print(highest_lowest_freq_elements([10,5,10,15,10,5]))