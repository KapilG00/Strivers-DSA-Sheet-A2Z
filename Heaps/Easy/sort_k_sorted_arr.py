from typing import List
import heapq


# TC -> O(nlogn)
# SC -> O(k)
def sort_k_sorted_arr(arr: List[int], k: int) -> List[int]:
    sorted_arr = []
    heap = []
    n = len(arr)
    
    # Push k+1 elements to the heap.
    for i in range(min(k+1, n)):
        heapq.heappush(heap, arr[i])
    
    # Remove/Delete the top-most element.
    # Push the current element into the heap.
    for j in range(k+1, n):
        sorted_arr.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[j])
    
    # Pop remaining elements from heap
    while heap:
        sorted_arr.append(heapq.heappop(heap))    
        
    return sorted_arr
    


if __name__ == "__main__":
    print(sort_k_sorted_arr([6,5,3,2,8,10,9], 3))