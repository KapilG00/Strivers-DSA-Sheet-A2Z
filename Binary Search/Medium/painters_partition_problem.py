from typing import List


def painters_required(boards: List[int], current_time_to_paint: int) -> int:
    n = len(boards)
    painters = 1
    load_on_a_painter = 0

    # O(n)
    for board in boards: 
        if load_on_a_painter + board <= current_time_to_paint:
            load_on_a_painter += board
        else:
            painters += 1
            load_on_a_painter = board

    return painters            

# Brute-force
# TC: O(sum(arr)-max(arr)) * O(n)
# SC: O(1)
def painters_partition(boards: List[int], painters_available: int) -> int:
    min_time_required_to_paint_a_board = max(boards)
    max_time_required_to_paint_all_boards = sum(boards)

    # O(sum(arr)-max(arr))
    for i in range(min_time_required_to_paint_a_board, max_time_required_to_paint_all_boards+1):
        painters = painters_required(boards, i)

        if painters <= painters_available:
            return i
        
    return min_time_required_to_paint_a_board    

# Optimal
# TC: O(log(sum(arr)-max(arr))) * O(n)
# SC: O(1)
def painters_partition(boards: List[int], painters_available: int) -> int:
    low = max(boards)
    high = sum(boards)
    min_time_required_to_paint_all_boards = 0

    # O(sum(arr)-max(arr))
    while low <= high:
        mid = (low+high)//2

        if painters_required(boards, mid) <= painters_available:
            min_time_required_to_paint_all_boards = mid
            high = mid-1
        else:
            low = mid+1

    return min_time_required_to_paint_all_boards            

            


if __name__ == "__main__":
    print(painters_partition([5,5,5,5], 2))
    print(painters_partition([10,20,30,40], 2))
    print(painters_partition([1,2,3,4,5], 2))