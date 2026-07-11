from typing import List


def ls(arr: List[int], ele: int) -> bool:
    m = len(arr)

    for j in range(m):
        if arr[j] == ele:
            return True
    return False    


def func(arr: List[int]) -> int:
    n = len(arr)
    length_of_longest_cons_sequence = 1
    
    for i in range(n):
        current_length_of_longest_seq = 1
        ele = arr[i]

        while ls(arr, ele+1):
            ele += 1
            current_length_of_longest_seq += 1
        length_of_longest_cons_sequence = max(length_of_longest_cons_sequence, current_length_of_longest_seq)

    return length_of_longest_cons_sequence    

    
    



if __name__ == "__main__":
    print(func([100,4,200,1,3,2]))
    