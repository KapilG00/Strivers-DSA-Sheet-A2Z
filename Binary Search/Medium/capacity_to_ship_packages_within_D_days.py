from typing import List


def calculate_days_required_to_ship(weights: List[int], current_possible_weight_capacity: int) -> int:
    n = len(weights)
    current_capacity = 0
    days_required_to_ship = 1

    for j in range(n):
        if current_capacity + weights[j] > current_possible_weight_capacity:
            days_required_to_ship += 1
            current_capacity = weights[j]
        else:
            current_capacity += weights[j]

    return days_required_to_ship        

# Brute-force
# TC: O(sum(arr)-max(arr)) * O(n)
# SC: O(1)
def capacity_to_ship_packages_within_D_days(weights: List[int], total_days: int) -> int:
    min_weight = max(weights)
    max_weight = sum(weights)

    for i in range(min_weight, max_weight+1):
        days_required = calculate_days_required_to_ship(weights, i)

        if days_required <= total_days:
            return i

# Optimal
# TC: O(log(sum(arr)-max(arr))) * O(n)
# SC: O(1)
def capacity_to_ship_packages_within_D_days(weights: List[int], total_days: int) -> int:
    low = max(weights)
    high = sum(weights)
    min_capacity = 0

    while low <= high:
        mid = (low+high)//2

        days_required = calculate_days_required_to_ship(weights, mid)

        if days_required <= total_days:
            min_capacity = mid
            high = mid-1
        else:
            low = mid+1

    return min_capacity            



if __name__ == "__main__":
    print(capacity_to_ship_packages_within_D_days([5,4,5,2,3,4,5,6], 5))
    print(capacity_to_ship_packages_within_D_days([1,2,3,4,5], 2))