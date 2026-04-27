from typing import List

# brute-force
# def temp(arr1: List[int], arr2: List[int]) -> int:
#     n1, n2 = len(arr1), len(arr2)
#     arr = []

#     for i in range(n1):
#         if arr1[i] not in arr:
#             arr.append(arr1[i])
    
#     for j in range(n2):
#         if arr2[j] not in arr:
#             arr.append(arr2[j])

#     return arr        
 
# brute-force
# def temp(arr1: List[int], arr2: List[int]) -> int:
#     n1, n2 = len(arr1), len(arr2)
#     hash_map = {}
#     arr = []

#     for i in range(n1):
#         if arr1[i] not in hash_map:
#             hash_map[arr1[i]] = 1
#         else:
#             hash_map[arr1[i]] += 1    

#     for j in range(n2):
#         if arr2[j] not in hash_map:
#             hash_map[arr2[j]] = 1
#         else:
#             hash_map[arr2[j]] += 1

#     for key in hash_map.keys():
#         arr.append(key)

#     return arr    


# optimal
def temp(arr1: List[int], arr2: List[int]) -> int:
    n1, n2 = len(arr1), len(arr2)
    i, j = 0, 0
    arr = []

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if len(arr) == 0 or arr[-1] != arr1[i]:
                arr.append(arr1[i]) 
            i += 1
        elif arr2[j] < arr1[i]:
            if len(arr) == 0 or arr[-1] != arr2[j]:    
                arr.append(arr2[j]) 
            j += 1
        else:
            if arr[-1] != arr1[i]:
                arr.append(arr1[i])
            i += 1

    while i < n1:
        if arr[-1] != arr1[i]:
            arr.append(arr1[i])
        i += 1

    while j < n2:
        if arr[-1] != arr2[j]:
            arr.append(arr2[j])    
        j += 1


    return arr               





    


if __name__ == "__main__":
    print(temp([1,2,3,4,5,6,7,8,9,10], [2,3,4,4,5,11,12]))