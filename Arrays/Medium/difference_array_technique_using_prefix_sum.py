from typing import List

# Brute-force
# TC: O(q*n); where 'n' is length of array and 'q' is no of queries.
# SC: O(1)
def differnce_array_technique(arr: List[int], queries: List[tuple]) -> List[int]:
    for query in queries:
        l, r, x = query

        for i in range(l, r+1):
            arr[i] += x

    return arr        

# TC: O(n) + O(q); where 'n' is length of array and 'q' is no of queries.
# SC: O(n)
def differnce_array_technique(arr: List[int], queries: List[tuple]) -> List[int]:
    n = len(arr)

    for query in queries:
        l, r, x = query
        
        arr[l] += x
        arr[r + 1] -= x
    
    prefix_sum_arr = [0] * n
    prefix_sum_arr[0] = arr[0]

    for i in range(1,n):
        prefix_sum_arr[i] = prefix_sum_arr[i-1] + arr[i]

    """Using below, we can reduce the SC from O(n) to O(1)"""
    # for i in range(1,n):
    #     arr[i] = arr[i-1] + arr[i]
     
    # return arr    
     
    return prefix_sum_arr
    
    

if __name__ == "__main__":
    print(differnce_array_technique([0,0,0,0,0,0,0], [(0,2,5), (1,3,6), (2,5,1)]))