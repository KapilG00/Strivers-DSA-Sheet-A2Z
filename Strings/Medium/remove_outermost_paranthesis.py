# TC: O(n)
# SC: O(1)
def remove_outermost_parantheses(s: str) -> str:
    output_valid_string = ""
    level = 0

    for i in range(len(s)):
        if s[i] == "(":
            if level > 0:
                output_valid_string += s[i]
            level += 1
        elif s[i]  == ")":
            level -= 1
            if level > 0:
                output_valid_string += s[i]

    return output_valid_string            
    



if __name__ == "__main__":
    print(remove_outermost_parantheses("((()))"))
    print(remove_outermost_parantheses("()(()())(())"))