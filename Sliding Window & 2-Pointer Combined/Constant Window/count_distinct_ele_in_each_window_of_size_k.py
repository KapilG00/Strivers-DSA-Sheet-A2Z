from typing import List


# TC: O(k) + O(n-k)
# SC: O(k) + O(n-k+1)
def count_of_distinct_eles_in_window_of_size_k(arr: List[int], k: int) -> List[int]:
    n = len(arr)
    low = 0
    high = k-1
    distinct_ele_count_arr = []
    hash_map = {}
    
    # First window
    for i in range(low, high+1):
        if arr[i] not in hash_map:
            hash_map[arr[i]] = 1
        else:
            hash_map[arr[i]] += 1

    distinct_ele_count_arr.append(len(hash_map))             

    while high < n-1:
        high += 1
        
        # Adding new element
        if arr[high] not in hash_map:
            hash_map[arr[high]] = 1
        else:
            hash_map[arr[high]] += 1
        
        # Remove outgoing element
        if arr[low] in hash_map:
            if hash_map[arr[low]] > 1:
                hash_map[arr[low]] -= 1
            else:
                hash_map.pop(arr[low])

        low += 1
        distinct_ele_count_arr.append(len(hash_map))         

    return distinct_ele_count_arr  



if __name__ == "__main__":
    print(count_of_distinct_eles_in_window_of_size_k([1,2,1,3,4,2,3], 4))
    print(count_of_distinct_eles_in_window_of_size_k([4,1,1], 2))