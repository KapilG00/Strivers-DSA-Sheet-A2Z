from typing import List


# Brute-force
# TC: O(n^3)
# SC: O(2*number of triplets)
def three_sum(arr: List[int]) -> List[tuple[int, int, int]]:
    n = len(arr)
    st = set()

    for i in range(n): 
        for j in range(i+1, n):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplet = tuple(sorted([arr[i], arr[j], arr[k]]))
                    st.add(triplet) # O(log(number of unique triplets))
                
    return [triplet for triplet in st]

         
# Better
# TC: O(n^2)
# SC: O(2*number of triplets) + O(n)
def three_sum(arr: List[int]) -> List[tuple[int, int, int]]:
    n = len(arr)
    st = set()

    for i in range(n):
        hash_set = set()
        for j in range(i+1, n):
            third_element = -(arr[i]+arr[j])

            if third_element in hash_set:
                triplet = tuple(sorted([arr[i], arr[j], third_element]))
                st.add(triplet) # 

            hash_set.add(arr[j])  # O(n) for space complexity

    return [triplet for triplet in st]  
 
# Optimal
# TC: O(n^2) + O(nlogn)
# SC: O(len(triplets_arr))
def three_sum(arr: List[int]) -> List[tuple[int, int, int]]:
    n = len(arr)
    arr.sort() # O(nlogn) 
    triplets_arr = []

    for i in range(n): # O(n)
        j = i+1
        k = n-1

        if i > 0 and arr[i] == arr[i-1]:
            continue

        while j < k: # ~ O(n)
            current_sum = arr[i] + arr[j] + arr[k]
            if current_sum > 0:
                k -= 1
            elif current_sum < 0:
                j += 1
            else:
                triplets_arr.append((arr[i], arr[j], arr[k]))
                j += 1
                k -= 1

                # Skip duplicates for 'j'
                while j < k and arr[j] == arr[j-1]:
                    j += 1
                # Skip duplicates for 'k'
                while j < k and arr[k] == arr[k+1]:
                    k -= 1   
             
    return triplets_arr



    
if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4]))
    print(three_sum([-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]))