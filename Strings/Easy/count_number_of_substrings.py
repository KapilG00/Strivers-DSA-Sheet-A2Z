from typing import List


# Brute-force
# TC: O(n^2) + O(len(substrings_arr))
# SC: O(len(substrings_arr))
def count_substrings(s: str, k: int) -> List[str]:
    n = len(s)
    substrings_arr = []

    for i in range(n):
        for j in range(i, n):
            substrings_arr.append(s[i:j+1])

    substrings_count = 0

    for substring in substrings_arr:
        if len(set(substring)) == k:
            substrings_count += 1   
    return substrings_count   

def at_most_k_distinct(s: str, k: int) -> int:
    count_of_substrings = 0
    left = 0
    map = {}

    # Iterate with right pointer
    for right in range(len(s)):
        map[s[right]] = map.get(s[right], 0) + 1

        # Shrink window if distinct characters exceed k
        while len(map) > k:
            map[s[left]] -= 1
            if map[s[left]] == 0:
                del map[s[left]]
            left += 1    

        # Count substrings in current window
        count_of_substrings += (right - left + 1)       

    return count_of_substrings     

# Optimal
# Using sliding window
# Exactly k = Atmost k - Atmost k-1
# TC: O(n)
# SC: O(1)
def count_substrings(s: str, k: int) -> List[str]:
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k-1)



if __name__ == "__main__":
    print(count_substrings("pqpqs", 2))
    print(count_substrings("abcbaa", 3))