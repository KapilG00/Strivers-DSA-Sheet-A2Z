from typing import List


def insert_element(stack: List[int], temp: int) -> None:
    # Base case: Check if stack is empty or topmost element of stack is greater than "temp".
    if not stack or temp > stack[-1]:
        stack.append(temp)
        return

    # Pop topmost element from stack, since it is greater than the cureent "temp" value.
    val = stack.pop()

    # Insert "temp" at its correct position recursively.
    insert_element(stack, temp)

    # Append "val" into the stack.
    stack.append(val)

# TC: O(n^2)
# SC: O(1); excluding auxiliary space, i.e. recursive call stack depth
def sort_stack(stack: List[int]) -> None:
    # Check if stack is empty
    if not stack:
        return

    # Pop the topmost element
    temp = stack.pop()

    # Continue removing topmost element from stack until stack is empty
    sort_stack(stack)

    # Now, recursively insert elements at their correct positions.
    insert_element(stack, temp)
   



if __name__ == "__main__":
    stack = [4, 1, 3, 2]
    sort_stack(stack)
    print(stack)