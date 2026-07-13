from typing import List


# Brute-force
# TC: O(n^3)
# SC: O(2*number of unique quadruplets)
def four_sum(arr: List[int], target: int) -> List[tuple[int, int, int]]:
    n = len(arr)
    st = set()

    for i in range(n): 
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == target:
                        quadruplet = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                        st.add(quadruplet) # O(log(number of unique quadruplets))
                
    return [quadruplet for quadruplet in st]

         
# Better
# TC: O(n^3)
# SC: O(2*number of unique quadruplets) + O(n)
def four_sum(arr: List[int], target: int) -> List[tuple[int, int, int]]:
    n = len(arr)
    st = set() # O(n) for space

    for i in range(n):
        for j in range(i+1, n):
            hash_set = set() # O(n) for space
            for k in range(j+1, n):
                fourth_element = target-(arr[i]+arr[j]+arr[k])

                if fourth_element in hash_set:
                    quadruplet = tuple(sorted([arr[i], arr[j], arr[k], fourth_element]))
                    st.add(quadruplet) # 

                hash_set.add(arr[k])

    return [quadruplet for quadruplet in st]  # O(number of unique quadruplets) for space
 
# # Optimal
# # TC: O(n^3) + O(log(number of unique triplets)) + O(nlogn)
# # SC: O(len(quadruplets_arr))
def four_sum(arr: List[int], target: int) -> List[tuple[int, int, int]]:
    n = len(arr)
    arr.sort() # O(nlogn) 
    quadruplets_arr = []

    for i in range(n): # O(n)
        if i > 0 and arr[i] == arr[i-1]: # Skipping duplicates
            continue
        for j in range(i+1, n):
            k = j+1
            l = n-1

            if j != i+1 and arr[j] == arr[j-1]: # Skipping duplicates
                continue

            while k < l: # ~ O(n)
                current_sum = arr[i] + arr[j] + arr[k] + arr[l]
                if current_sum > target:
                    l -= 1
                elif current_sum < target:
                    k += 1
                else:
                    quadruplets_arr.append((arr[i], arr[j], arr[k], arr[l]))
                    k += 1
                    l -= 1

                    # Skip duplicates for 'k'
                    while k < l and arr[k] == arr[k-1]:
                        k += 1
                    # Skip duplicates for 'l'
                    while k < l and arr[l] == arr[l+1]:
                        l -= 1   
             
    return quadruplets_arr



    
if __name__ == "__main__":
    print(four_sum([1,0,-1,0,-2,2], 0))