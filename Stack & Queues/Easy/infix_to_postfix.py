# TC: O(n)
# SC: O(N)
def infix_to_postfix(s: str) -> str:
    n = len(s)
    stack = []
    result = ""
    i = 0

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    while i < n:
        # Add all the operands in the result.
        if s[i].isalnum():
            result += s[i]
        
        # Handle the '(' paranthesis.
        elif s[i] == '(':
            stack.append(s[i])

        # Handle the ')' paranthesis.
        elif s[i] == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        # Add all the operators in the stack.
        else:
            # Pop all the operators from stack until current operator is greater than stack's current operator.
            while len(stack) > 0 and \
                  stack[-1] != '(' and \
                  (
                    precedence[stack[-1]] > precedence[s[i]] or 
                    # Below condition is for the cases where stack's top most element's precedence
                    # and current character precedence of an input string are equal AND current character
                    # is not equal to "^" (because "^" is right associative). 
                    (
                        precedence[stack[-1]] == precedence[s[i]] and
                        s[i] != '^'
                    )
                  ):
                result += stack.pop()
            stack.append(s[i])    

        i += 1

    while len(stack) > 0:
        result += stack.pop()
   
    return result



if __name__ == "__main__":
    print(infix_to_postfix("a+b*(c^d-e)"))
    print(infix_to_postfix("h^m^q^(7-4)"))
    print(infix_to_postfix("h+m+q+(7-4)"))