def infix_to_prefix(infix_string: str) -> str:
    n = len(infix_string)
    prefix_string = ""
    stack = []
    i = 0

    precedence = {"^": 3, "/": 2, "*": 2, "+": 1, "-": 1, "(": 0, ")": 0}

    # Reverse the infix string
    reversed_infix_string = infix_string[::-1]

    reverse_infix_list = list(reversed_infix_string)

    for j in range(len(reverse_infix_list)):
        if reverse_infix_list[j] == "(":
            reverse_infix_list[j] = ")"
        elif reverse_infix_list[j] == ")":
            reverse_infix_list[j] = "("

    reversed_infix_string = "".join(reverse_infix_list)

    while i < n:
        # Add the operands in the prefix string.
        if reversed_infix_string[i].isalnum():
            prefix_string += reversed_infix_string[i]

        # Handle the "("
        elif reversed_infix_string[i] == "(":
            stack.append(reversed_infix_string[i])

        # Handle the ")"
        elif reversed_infix_string[i] == ")":
            while len(stack) > 0 and stack[-1] != "(":
                prefix_string += stack.pop()
            stack.pop()

        # Add the operators in the stack.
        else:
            if reversed_infix_string[i] == "^":
                while (
                    len(stack) > 0
                    and precedence[reversed_infix_string[i]] == precedence[stack[-1]]
                ):
                    prefix_string += stack.pop()
            else:
                while (
                    len(stack) > 0
                    and precedence[reversed_infix_string[i]] < precedence[stack[-1]]
                ):
                    prefix_string += stack.pop()

            stack.append(reversed_infix_string[i])

        i += 1

    # Add all the operators from stack into prefix string.
    while len(stack) > 0:
        prefix_string += stack.pop()

    # Reverse the prefix string.
    prefix_string = prefix_string[::-1]

    return prefix_string


if __name__ == "__main__":
    print(infix_to_prefix("x+y*z/w+u"))
    print(infix_to_prefix("a-b-c"))
    print(infix_to_prefix("a+b*c-d/e^f"))
    print(infix_to_prefix("a^b^c-d/e+f"))
    print(infix_to_prefix("a+b*(c^d-e)"))
