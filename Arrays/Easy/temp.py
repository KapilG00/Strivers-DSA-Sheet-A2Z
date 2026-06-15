from typing import List

# Brute-force
def func(arr: List[int]) -> int:
    n = len(arr)
    max_count_of_cons_1s = 0

    for i in range(n):
        current_count_of_1s = 0
        for j in range(i, n):
            if arr[j] == 1:
                current_count_of_1s += 1
            else:
                break
        if current_count_of_1s > max_count_of_cons_1s:
            max_count_of_cons_1s = current_count_of_1s

    return max_count_of_cons_1s                
        

# Better
# def func(arr: List[int]) -> tuple[int, int]:


# Optimal
def func(arr: List[int]) -> int:
    n = len(arr)
    i = 0
    count = 0
    max_count = 0

    for i in range(n):
        if arr[i] == 1:
            count += 1
        else:
            count = 0        
        max_count = max(count, max_count)
    return max_count


    

if __name__ == "__main__":
    print(func([1,1,0,1,1,1]))
    print(func([1,0,1,1,0,1]))