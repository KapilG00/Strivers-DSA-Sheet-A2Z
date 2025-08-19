from typing import List


def linear_search(arrr: List[int], x: int) -> int:
    m = len(arrr)

    for j in range(m):
        if arrr[j] == x:
            return True
    return False

# Brute-force approach
# TC -> O(n^2)
# SC -> O(1)
def longest_consecutive_sequence_in_array(arr: List[int]) -> int:
    n = len(arr)
    longest_cons_seq_length = 1

    for i in range(n):
        current_longest_cons_seq_length = 1
        current_ele = arr[i]

        while linear_search(arr, current_ele+1):
            current_ele += 1
            current_longest_cons_seq_length += 1
        longest_cons_seq_length = max(longest_cons_seq_length, current_longest_cons_seq_length)
               
    return longest_cons_seq_length

# Better approach
# TC ->  O(nlogn) + O(n)
# SC -> O(1)
def longest_consecutive_sequence_in_array(arr: List[int]) -> int:
    n = len(arr)
    
    if n == 0:
        return 0
    
    arr.sort() # O(nlogn)
    longest_cons_seq_length = 1
    last_smaller = float('-inf')
    current_longest_cons_seq_length = 0
    
    for i in range(n):
        if arr[i]-1 == last_smaller:
            current_longest_cons_seq_length += 1
            last_smaller = arr[i]
        # reset sequence    
        elif arr[i] != last_smaller:
            last_smaller = arr[i]
            current_longest_cons_seq_length = 1 
        longest_cons_seq_length = max(longest_cons_seq_length, current_longest_cons_seq_length)

    return longest_cons_seq_length

# Optimal approach
# TC ->  O(n)+O(2*n) ~ O(3*n) (n is a size of a set)
# SC -> O(n)
def longest_consecutive_sequence_in_array(arr: List[int]) -> int:
    n = len(arr)
    
    if n == 0:
        return 0
    
    longest_cons_seq_length = 1
    st = set()

    for i in range(n):
        st.add(arr[i])

    for ele in st:
        if (ele-1) not in st:
            current_longest_cons_seq_length = 1
            num = ele
            while (num+1) in st:
                num += 1
                current_longest_cons_seq_length += 1
            longest_cons_seq_length = max(longest_cons_seq_length, current_longest_cons_seq_length)

    return longest_cons_seq_length            


if __name__ == "__main__":
    print(longest_consecutive_sequence_in_array([100,200,1,3,2,4]))
    print(longest_consecutive_sequence_in_array([3,8,5,7,6]))
    print(longest_consecutive_sequence_in_array([100,200,101,102,2,4]))