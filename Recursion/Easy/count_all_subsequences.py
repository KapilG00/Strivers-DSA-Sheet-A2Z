from typing import List


# TC: O(2^n)
# SC: O(n) + O(n) = O(2n) = O(n)
def count_all_subsequences(arr: List[int], idx: int, subsequences_arr: List[int], count: int) -> int:
    n = len(arr)
    
    # base case
    if idx == n:
        if subsequences_arr:
            count += 1
        return count

    # take
    subsequences_arr.append(arr[idx])
    take = count_all_subsequences(arr, idx+1, subsequences_arr, count)

    # pop/remove
    subsequences_arr.pop()

    # not take
    not_take = count_all_subsequences(arr, idx+1, subsequences_arr, count)

    return take+not_take

# Without the need of "subsequences_arr" and "count" (RECOMMENDED)
# TC: O(2^n)
# SC: O(n)
def count_all_subsequences(arr: List[int], idx: int) -> int:
    n = len(arr)
    
    # base case
    if idx == n:
        return 1

    # take
    take = count_all_subsequences(arr, idx+1)

    # not take
    not_take = count_all_subsequences(arr, idx+1)

    return take+not_take



if __name__ == "__main__":
    print(count_all_subsequences([3,1,2], 0, [], 0))
    print(count_all_subsequences([3,1,2], 0) - 1)