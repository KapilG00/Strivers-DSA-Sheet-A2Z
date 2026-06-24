# TC: O(n); n is length of input string.
# SC: O(N) N is length of stack.
def check_balanced_paranthesis(s: str) -> bool:
    stack = []

    if len(s) == 0:
        return True 

    for paranthesis in s:
        if paranthesis in ['[', '{', '(']:
            stack.append(paranthesis)
        else:
            if paranthesis == ']' and stack[-1] == '[':
                stack.pop()
            elif paranthesis == '}' and stack[-1] == '{':
                stack.pop()
            elif paranthesis == ')' and stack[-1] == '(':
                stack.pop()

    if len(stack) == 0:
        return True

    return False                    



if __name__ == "__main__":
    print(check_balanced_paranthesis("()[{}()]"))
    print(check_balanced_paranthesis("[()"))
    print(check_balanced_paranthesis(""))