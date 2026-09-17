def prefix_to_infix(prefix_string: str) -> str:
    n = len(prefix_string)
    i = n - 1
    stack = []

    while i >= 0:
        # Add the operands in the stack.
        if prefix_string[i].isalnum():
            stack.append(prefix_string[i])

        # Add the operators in the stack.
        else:
            top_most_ele = stack.pop()
            second_top_most_ele = stack.pop()

            temp_str = "(" + top_most_ele + prefix_string[i] + second_top_most_ele + ")"
            stack.append(temp_str)

        i -= 1

    return stack[-1]


if __name__ == "__main__":
    print(prefix_to_infix("*+PQ-MN"))
