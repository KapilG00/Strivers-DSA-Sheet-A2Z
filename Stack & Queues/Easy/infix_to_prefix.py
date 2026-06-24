# TC: O(n) + O(n)
# SC: O(n) + O(n)
def infix_to_prefix(s: str) -> str:
    n = len(s)
    stack = []
    result = ""
    i = 0

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
        '(': 0,
        ')': 0
    }

    reversed_str = s[::-1]

    reversed_list = list(reversed_str)

    for j in range(len(reversed_list)):
        if reversed_list[j] == "(":
            reversed_list[j] = ")"
        elif reversed_list[j] == ")":
            reversed_list[j] = "("

    reversed_str = "".join(reversed_list)

    while i < n:
        # Add all the operands in the result.
        if reversed_str[i].isalnum():
            result += reversed_str[i]
        
        # Handle the '(' paranthesis.
        elif reversed_str[i] == '(':
            stack.append(reversed_str[i])

        # Handle the ')' paranthesis.
        elif reversed_str[i] == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
 
        # Add all the operators in the stack.
        else:
            if reversed_str[i] == '^':
                # Pop the operators from stack until current operator is less than or equal to stack's current operator.
                while len(stack) > 0 and precedence[reversed_str[i]] <= precedence[stack[-1]]:
                    result += stack.pop()
            else:
                # Pop the operators from stack until current operator is less than stack's current operator.
                while len(stack) > 0 and precedence[reversed_str[i]] < precedence[stack[-1]]:
                    result += stack.pop()

            stack.append(reversed_str[i])

        i += 1

    while len(stack) > 0:
        result += stack.pop()

    double_reversed_str = result[::-1]    
   
    return double_reversed_str



if __name__ == "__main__":
    print(infix_to_prefix("a+b*(c^d-e)"))
    print(infix_to_prefix("h^m^q^(7-4)"))
    print(infix_to_prefix("h+m+q+(7-4)"))