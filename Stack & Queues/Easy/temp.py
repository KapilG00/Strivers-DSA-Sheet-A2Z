# TC: O(n)
# SC: O(N)
def infix_to_postfix(infix_string: str) -> str:
    n = len(infix_string)
    stack = []
    res = ""
    i = 0

    operators_priorities_mapping = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3,
        "(": 0,
        ")": 0,
    }

    while i < n:
        # Adding the operands to the result.
        if infix_string[i].isalnum():
            res += infix_string[i]

        # Handling the "(" and ")" conditions.
        elif infix_string[i] == "(":
            stack.append(infix_string[i])

        elif infix_string[i] == ")":
            while len(stack) > 0 and stack[-1] != "(":
                res += stack.pop()
            # This pop is to remove the "(" from the stack.
            stack.pop()

        # Adding the operators to the stack.
        else:
            while (
                len(stack) > 0
                and stack[-1] != "("
                and (
                    operators_priorities_mapping[infix_string[i]]
                    < operators_priorities_mapping[stack[-1]]
                    or (
                        operators_priorities_mapping[infix_string[i]]
                        == operators_priorities_mapping[stack[-1]]
                        and infix_string[i] != "^"
                    )
                )
            ):
                res += stack.pop()

            stack.append(infix_string[i])

        i += 1

    # Adding remaining elements from stack into postfix string.
    while len(stack) > 0:
        res += stack.pop()

    return res


if __name__ == "__main__":
    print(infix_to_postfix("a+b*(c^d-e)"))
    print(infix_to_postfix("h^m^q^(7-4)"))
    print(infix_to_postfix("h+m+q+(7-4)"))
