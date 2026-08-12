# TC: O(n)
# SC: O(1)
def max_nesting_depth_parantheses(s: str) -> int:
    max_depth = 0
    depth = 0

    for char in s:
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1

        max_depth = max(max_depth, depth)

    return max_depth            



if __name__ == "__main__":
    print(max_nesting_depth_parantheses("(1+(2*3)+((8)/4))+1"))
    print(max_nesting_depth_parantheses("(1)+((2))+(((3)))"))