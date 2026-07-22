
# TC: O(logn)
# SC: O(n)
def find_square_root_of_number(num: int) -> int:
    arr = [i*i for i in range(1, num+1)]
    n = len(arr)

    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2

        if arr[mid] == num:
            return mid+1
        elif arr[mid] > num:
            high = mid-1
        else:
            low = mid+1

    return -1 

# TC: O(logn)
# SC: O(1)
def find_square_root_of_number(num: int) -> int:
    low = 1
    high = num
    square_root = 1

    while low <= high:
        mid = (low+high)//2
        current_square = mid*mid

        if current_square <= num:
            # Store mid as potential answer
            square_root = mid
            low = mid+1
        else:
            high = mid-1

    return square_root         



if __name__ == "__main__":
    print(find_square_root_of_number(36))
    print(find_square_root_of_number(144))
    print(find_square_root_of_number(81))