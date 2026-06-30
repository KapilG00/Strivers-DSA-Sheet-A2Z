from typing import List


# TC -> O(n^2)
# SC -> O(n)
# Brute-force approach
def replace_with_rank(arr: List[int]) -> List[int]:
    rank_arr = []
    n = len(arr)

    for i in range(n):
        count_of_unique_smaller_eles = set()
        for j in range(n):
            if arr[j] < arr[i]:
                count_of_unique_smaller_eles.add(arr[j])
        rank_arr.append(len(count_of_unique_smaller_eles)+1)

    return rank_arr            

 # TC -> O(nlogn)
# SC -> O(n)
# Optimal approach
def replace_with_rank(arr: List[int]) -> List[int]:
    rank_arr = []
    sorted_arr = sorted(arr)
    rank_map = {}
    rank = 1

    for ele in sorted_arr:
        if ele not in rank_map:
            rank_map[ele] = rank
            rank += 1   
     
    print("rank map:", rank_map)

    for num in arr:
        rank_arr.append(rank_map[num])

    return rank_arr    
 
   

if __name__ == "__main__":
    print(replace_with_rank([20,15,26,2,98,6]))