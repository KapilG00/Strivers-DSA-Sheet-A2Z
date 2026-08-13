INT_MIN = -2**31
INT_MAX = 2**31 - 1

def helper(s: str, i: int, num: int, sign: int) -> int:
    # Base case
    if i >= len(s) or not s[i].isdigit():
        return sign*num

    # Update num
    num = num * 10 + int(s[i])

    # Clamp if overflow
    if sign*num <= INT_MIN:
        return INT_MIN
    if sign*num >= INT_MAX:
        return INT_MAX

    return helper(s, i+1, num, sign)

# TC: O(n)
# SC: O(n)    
def recursive_implementation_of_atoi(s: str) -> int:
    i = 0

    # Skipping white spaces.
    while i < len(s) and s[i] == " ":
        i += 1

    # Handle sign.
    sign = 1
    if i < len(s) and (s[i] == "+" or s[i]  == "-"):
        sign = -1 if s[i] == "-" else 1
        i += 1

    return helper(s, i, 0, sign)        



if __name__ == "__main__":
    print(recursive_implementation_of_atoi(" -12345"))
    print(recursive_implementation_of_atoi("4193 with words"))