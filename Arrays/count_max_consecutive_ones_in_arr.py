from typing import List


# TC -> O(n^2)
# SC -> O(1)
def count_max_consecutives_ones_in_arr(arr: List[int]):
    n = len(arr)
    max_consec_ones_count = 0

    for i in range(n):
        current_max_consec_ones_count = 0
        for j in range(i, n):
            if arr[j] == 1:
                current_max_consec_ones_count += 1
            else:
                break    

        if current_max_consec_ones_count > max_consec_ones_count:
            max_consec_ones_count = current_max_consec_ones_count

    return max_consec_ones_count    

# TC -> O(n)
# SC -> O(1)
def count_max_consecutives_ones_in_arr(arr: List[int]):
    n = len(arr)
    max_consec_ones_count = 0
    current_max_consec_ones_count = 0

    for i in range(n):
        if arr[i] == 1:
            current_max_consec_ones_count += 1
        else:
            current_max_consec_ones_count = 0

        if current_max_consec_ones_count > max_consec_ones_count:
            max_consec_ones_count = current_max_consec_ones_count

    return max_consec_ones_count                



if __name__ == "__main__":
    print(count_max_consecutives_ones_in_arr([1,1,0,1,1,1]))
    print(count_max_consecutives_ones_in_arr([1,0,1,1,0,1]))