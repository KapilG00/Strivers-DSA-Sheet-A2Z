# TC: O(num) 
# SC: O(1)
def climbing_stairs(num: int) -> int:
    # base case 1
    if num == 0:
        return 1
    
    # base case 2 (where if we are standing at step 1 then we can only step down by 1 way)
    if num == 1:
        return 1

    left_recursion = climbing_stairs(num-1) # heading down from 5th step by 1 step each time.
    right_recursion = climbing_stairs(num-2) # heading down from 5th step by 2 steps each time.

    return left_recursion + right_recursion
    

if __name__ == "__main__":
    num = 5
    print(climbing_stairs(num))