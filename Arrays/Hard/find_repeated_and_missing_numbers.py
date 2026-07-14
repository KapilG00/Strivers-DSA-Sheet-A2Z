from typing import List


# Brute-force
# TC: O(n^2)
# SC: O(1)
def find_repeated_number_A_and_missing_number_B(arr: List[int]) -> List[int]:
    n = len(arr)
    repeated_twice_number = -1
    missing_number = -1
    
    # O(n^2)
    for i in range(1, n+1):
        current_number_count = 0
        for j in range(n):
            if arr[j] == i:
                current_number_count += 1

        if current_number_count == 2:
            repeated_twice_number = i
        elif current_number_count == 0:
            missing_number = i

        # If both repeated_twice_number and missing_number are found, break out of loop.
        if repeated_twice_number != -1 and missing_number != -1:
            break        

    return [repeated_twice_number, missing_number]                

# Better
# TC: O(n) + O(n) = O(2n)
# SC: O(n)
def find_repeated_number_A_and_missing_number_B(arr: List[int]) -> List[int]:
    n = len(arr)
    repeated_twice_number = -1
    missing_number = -1
    hash_arr = [0] * (n+1)

    for i in range(n):
        hash_arr[arr[i]] += 1
        
    for j in range(1, len(hash_arr)):
        if hash_arr[j] == 2:
            repeated_twice_number = j
        if hash_arr[j] == 0:
            missing_number = j

        # If both repeated_twice_number and missing_number are found, break out of loop.
        if repeated_twice_number != -1 and missing_number != -1:
            break       

    return [repeated_twice_number, missing_number]

# Optimal
# TC: O(n)
# SC: O(1)
def find_repeated_number_A_and_missing_number_B(arr: List[int]) -> List[int]:
    n = len(arr)
    sn = n*(n+1)/2 # sum of 'n' natural numbers
    s2n = (n*(n+1)*(2*n+1))/6 # sum of squre of 'n' natural numbers
    s = 0
    s2 = 0

    for i in range(n):
        s += arr[i]
        s2 += arr[i]*arr[i]

    # s - sn
    val1 = s-sn   # x-y
    # s2 - s2n
    val2 = s2-s2n # x^2-y^2
    
    """
    val1 = x-y .... (i)
    val2 = x^2 - y^2
    
    val2 = (x-y)*(x+y)
    val2 = val1 * (x+y)
    let (x+y) = val3 .... (ii)
    val2 = val1 * val3
    val3 = val2/val1

    """
    val3 = val2/val1 # (x+y)/(x-y)

    """
    x-y = val1
    x+y = val3

    2x = val1+val3
    x = (val1+val3)/2
    
    from (i)
    [(val1+val3)/2]-y = val1
    val1+val3-2y = 2val1
    2y = val3-val1
    y = (val3-val1)/2
    """
    x = (val1+val3)/2
    y = x-val1

    return [x, y] # x => repeated_twice_number, y => missing_number



if __name__ == "__main__":
    print(find_repeated_number_A_and_missing_number_B([3,5,4,1,1]))
    print(find_repeated_number_A_and_missing_number_B([1,2,3,6,7,5,7]))