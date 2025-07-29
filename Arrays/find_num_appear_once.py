from typing import List


# TC -> O(n^2)
# SC -> O(1)
def find_num_appears_once(arr: List[int]) -> int:
    n = len(arr)

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[j] == arr[i]:
                count += 1

        if count == 1:
            return arr[i]

    return -1

# TC -> O(nlogm) + O(m); where "m" is count of total unique elements in a given array.
# SC -> O(m)
def find_num_appears_once(arr: List[int]) -> int:
    n = len(arr)
    freq_count = {}

    for i in range(n): # O(nlogm)
        if arr[i] in freq_count:
            freq_count[arr[i]] += 1
        else:
            freq_count[arr[i]] = 1

    for k, v in freq_count.items(): # O(m)
        if v == 1:
            return k
    return -1                
                

if __name__ == "__main__":
    print(find_num_appears_once([2,2,1]))
    print(find_num_appears_once([4,1,2,1,2]))