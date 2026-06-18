
# TC ->  O(n^2)
# SC -> O(n)
# Brute-force approach.
def check_string_is_rotated(s: str, goal: str) -> bool:
    n, m = len(s), len(goal)

    if n != m:
        return False

    for i in range(len(s)):
        current_rotated_version =  s[i:] + s[:i]

        if current_rotated_version == goal:
            return True
    return False


# TC ->  O(n)
# SC -> O(n)
# Optimal approach
def check_string_is_rotated(s: str, goal: str) -> bool:
    n, m = len(s), len(goal)

    if n != m:
        return False
    
    double_s = s + s

    if goal in double_s:
        return True
    return False

    

if __name__ == "__main__":
    print(check_string_is_rotated("rotation", "tionrota"))
    print(check_string_is_rotated("hello", "lohelx"))