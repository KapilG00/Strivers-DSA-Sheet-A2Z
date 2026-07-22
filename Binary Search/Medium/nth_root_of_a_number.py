

# TC: O(logm)
# SC: O(1)
def find_nth_root_of_number(n: int, m: int) -> int:
    low = 1
    high = m

    while low <= high:
        mid = (low+high)//2
        nth_root = mid**n

        if nth_root == m:
            return mid
        elif nth_root < m:
            low = mid+1
        else:
            high = mid-1

    return -1        
       

def func(mid: int, n: int, m: int):
    current_val = 1

    for _ in range(1, n+1):
        current_val = current_val*mid
        if current_val > m:
            return 2
    if current_val == m:
        return 1
    else:
        return 0    

# TC: O(logm)
# SC: O(1)
def find_nth_root_of_number(n: int, m: int) -> int:
    low = 1
    high = m

    while low <= high:
        mid = (low+high)//2
        nth_root = func(mid, n, m)

        # if func returned 1
        if nth_root == 1:
            return mid
        # if func returned 0
        elif nth_root == 0:
            low = mid+1
        # if func returned 2    
        else:
            high = mid-1

    return -1  


if __name__ == "__main__":
    print(find_nth_root_of_number(3, 27))
    print(find_nth_root_of_number(4, 69))
    print(find_nth_root_of_number(3, 512))