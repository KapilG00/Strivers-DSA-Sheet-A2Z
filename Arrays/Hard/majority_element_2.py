from typing import List


# Brute-force
# TC: O(n^2)
# SC: O(len(majority_element_arr))
def majority_element_2(arr: List[int]) -> int:
    n = len(arr)
    majority_element_arr = []

    for i in range(n):
        # If a previously included element is found during traversal, 
        # skip it to avoid counting duplicates.
        if len(majority_element_arr) == 0 or majority_element_arr[0] != arr[i]:
            current_ele_freq = 0
            for j in range(n):
                if arr[j] == arr[i]:
                    current_ele_freq += 1

            if current_ele_freq > n//3:
                majority_element_arr.append(arr[i])

        # If the result array already contains 2 elements, break out of the loop, 
        # as there can’t be more than two majority elements.
        if len(majority_element_arr) == 2:
            break        

    return majority_element_arr                

# Better
# TC: O(n)
# SC: O(len(majority_element_arr)) + O(len(map))
def majority_element_2(arr: List[int]) -> int:
    n = len(arr)
    map = {}
    majority_elements_arr = []
    # Least occurrence of the majority element
    min_freq_of_majority_ele_possible = n // 3 + 1

    for i in range(n):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            map[arr[i]] += 1
        
        if map[arr[i]] == min_freq_of_majority_ele_possible:
            majority_elements_arr.append(arr[i])

        if len(majority_elements_arr) == 2:
            break

    return majority_elements_arr        

# Optimal
# TC: O(n) + O(n) = O(2n)
# SC: O(len(majority_element_arr)) ~ O(1)
def majority_element_2(arr: List[int]) -> tuple[int,int]:
    n = len(arr)
    majority_1 = float('-inf')
    majority_2 = float('-inf')
    votes_1 = 0
    votes_2 = 0

    for i in range(n): # O(n)
        if majority_1 == arr[i]:
            votes_1 += 1
        elif majority_2 == arr[i]:
            votes_2 += 1
        elif votes_1 == 0 and majority_2 != arr[i]:
            majority_1 = arr[i]
            votes_1 = 1
        elif votes_2 == 0 and majority_1 != arr[i]:
            majority_2 = arr[i]
            votes_2 = 1
        else:
            votes_1 -= 1
            votes_2 -= 1   

    majority_elements_arr = []
    votes_1 = 0
    votes_2 = 0

    for j in range(n): # O(n)
        if majority_1 == arr[j]:
            votes_1 += 1
        if majority_2 == arr[j]:
            votes_2 += 1

    min_freq_of_majority_ele_possible = n // 3 + 1        

    if votes_1 >= min_freq_of_majority_ele_possible:
        majority_elements_arr.append(majority_1)
    if votes_2 >= min_freq_of_majority_ele_possible:
        majority_elements_arr.append(majority_2)

    return majority_elements_arr         



if __name__ == "__main__":
    print(majority_element_2([1,2,1,1,3,2]))
    print(majority_element_2([1,2,1,1,3,2,2]))