from typing import List


def check_possiblity_to_make_required_bouquets(bloom_days: List[int], current_bloom_day: int, no_of_bouquets: int, required_no_of_roses_in_each_bouquet: int) -> bool:
    no_of_adjacent_bloomed_rose = 0
    no_of_bouquets_can_formed = 0
    n = len(bloom_days)

    for j in range(n):
        if bloom_days[j] <= current_bloom_day:
            no_of_adjacent_bloomed_rose += 1
        else:
            no_of_bouquets_can_formed += no_of_adjacent_bloomed_rose//required_no_of_roses_in_each_bouquet
            no_of_adjacent_bloomed_rose = 0

    no_of_bouquets_can_formed += no_of_adjacent_bloomed_rose//required_no_of_roses_in_each_bouquet

    if no_of_bouquets_can_formed >= no_of_bouquets:
        return True
    else:
        return False

# Brute-force
# TC: O(n) * O(max-min)
# SC: O(1)
def find_min_days_to_make_m_bouquets(bloom_days: List[int], no_of_bouquets: int, required_no_of_roses_in_each_bouquet: int) -> int:
    n = len(bloom_days)

    # Impossible case where we cannot make bouquets
    # as given total number of flowers are not enough
    # to make required number of bouquets. 
    if no_of_bouquets*required_no_of_roses_in_each_bouquet > n:
        return -1

    first_day_of_bloom = min(bloom_days)
    last_day_of_bloom = max(bloom_days)

    for i in range(first_day_of_bloom, last_day_of_bloom+1):
        possible = check_possiblity_to_make_required_bouquets(bloom_days, i, no_of_bouquets, required_no_of_roses_in_each_bouquet)
        if possible:
            return i

# Optimal  
# TC: O(n) * O(log(max-min))
# SC: O(1)    
def find_min_days_to_make_m_bouquets(bloom_days: List[int], no_of_bouquets: int, required_no_of_roses_in_each_bouquet: int) -> int:
    n = len(bloom_days)

    # Impossible case where we cannot make bouquets
    # as given total number of flowers are not enough
    # to make required number of bouquets. 
    if no_of_bouquets*required_no_of_roses_in_each_bouquet > n:
        return -1
    
    low = min(bloom_days)
    high = max(bloom_days)
    perfect_day = 0

    while low <= high:
        mid = (low+high)//2
        possible = check_possiblity_to_make_required_bouquets(bloom_days, mid, no_of_bouquets, required_no_of_roses_in_each_bouquet)

        if possible:
            perfect_day = mid
            high = mid-1
        else:
            low = mid+1

    return perfect_day            



if __name__ == "__main__":
    print(find_min_days_to_make_m_bouquets([7,7,7,7,13,11,12,7], 2, 3))
    print(find_min_days_to_make_m_bouquets([1,10,3,10,2], 3, 2))