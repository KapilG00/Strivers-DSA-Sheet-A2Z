
# TC -> O(n)
# SC -> O(1)
def remove_outermost_paranthesis(string: str) -> str:
    n = len(string)
    res = ""
    counter = 0

    for i in range(n):
        if string[i] == "(":
            if counter > 0:
                res += string[i]
            counter += 1    
        elif string[i] == ")":
            counter -= 1    
            if counter > 0:
                res += string[i]  
    return res               


if __name__ == "__main__":
    print(remove_outermost_paranthesis("((()))"))
    print(remove_outermost_paranthesis("()(()())(())"))