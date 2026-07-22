from typing import List
import math


def hours_took_to_eat_all_bananas(arr: List[int], current_eating_speed: int) -> int:
    total_hours = 0
    n = len(arr)

    for i in range(n):
        total_hours += math.ceil(arr[i]/current_eating_speed)

    return total_hours

# TC: O(n*log(max(arr)))
# SC: O(1)
def koko_eating_bananas(arr: List[int], h: int) -> int:
    low = 1
    high = max(arr)
    min_eating_speed = float('inf')

    while low <= high:
        mid = (low+high)//2
        current_eating_time = hours_took_to_eat_all_bananas(arr, mid)

        if current_eating_time <= h:
            min_eating_speed = min(min_eating_speed, mid)
            high = mid-1
        else:
            low = mid+1

    return min_eating_speed        
        


if __name__ == "__main__":
    print(koko_eating_bananas([7,15,6,3], 8))
    print(koko_eating_bananas([25,12,8,14,19], 5))