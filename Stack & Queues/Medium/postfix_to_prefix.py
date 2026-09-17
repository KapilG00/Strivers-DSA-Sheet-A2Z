def postfix_to_prefix(postfix_string: str) -> str:
    n = len(postfix_string)
    i = 0
    stack = []

    while i < n:
        # Add the operands into the stack.
        if postfix_string[i].isalnum():
            stack.append(postfix_string[i])

        # Add the operators into the stack.
        else:
            top_most_ele = stack.pop()
            second_top_most_ele = stack.pop()

            temp_str = postfix_string[i] + second_top_most_ele + top_most_ele
            stack.append(temp_str)

        i += 1

    return stack[-1]


if __name__ == "__main__":
    print(postfix_to_prefix("AB-DE+F*/"))
