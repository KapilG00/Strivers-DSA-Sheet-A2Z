def postfix_to_infix(postfix_string: str) -> str:
    n = len(postfix_string)
    i = 0
    stack = []

    while i < n:
        # Add the operands into the stack.
        if postfix_string[i].isalnum():
            stack.append(postfix_string[i])

        # Add the operators into the stack in between last 2 elements of the stack.
        else:
            top_most_ele = stack.pop()
            second_top_most_ele = stack.pop()

            temp_ele = (
                "(" + second_top_most_ele + postfix_string[i] + top_most_ele + ")"
            )

            stack.append(temp_ele)
        print("stack:", stack)

        i += 1

    return stack[-1]


if __name__ == "__main__":
    print(postfix_to_infix("AB-DE+F*/"))
