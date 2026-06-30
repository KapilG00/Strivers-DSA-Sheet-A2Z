from typing import List


# TC -> O(n)
# SC -> O(1)
def jump_game_1(jumps: List[int]) -> bool:
    max_idx_reached = 0

    for i in range(len(jumps)):
        if i > max_idx_reached:
            return False

        max_idx_reached = max(max_idx_reached, i+jumps[i]) 

    return True
        

    
if __name__ == "__main__":
    print(jump_game_1([2,3,1,0,4]))
    print(jump_game_1([3,2,1,0,4]))