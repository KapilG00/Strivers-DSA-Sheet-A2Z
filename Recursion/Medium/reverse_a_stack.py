from typing import List


def insert_at_bottom(stack: List[int], temp: List[int]) -> None:
    if not stack:
        stack.append(temp)
        return

    val = stack.pop()

    insert_at_bottom(stack, temp)

    stack.append(val)    

# TC: O(n^2)
# SC: O(1); excluding auxiliary space, i.e. recursive call stack depth
def reverse_stack(stack: List[int]) -> List[int]:
    if not stack:
        return

    temp = stack.pop()

    reverse_stack(stack)

    insert_at_bottom(stack, temp)  



if __name__ == "__main__":
    stack = [4, 1, 3, 2]
    reverse_stack(stack)
    print(stack)