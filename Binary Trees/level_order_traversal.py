from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(n); where "n" is number of nodes in a BT.
# SC: O(n)
def level_order_traversal(node: Node):
    # Create a list to store levels
    list_of_levels = []
    if not root:
        # If the tree is empty, return an empty list
        return list_of_levels
    
    # Create a queue to store nodes for level-order traversal
    q = deque([root])
    
    while q:
        # Create a list to store nodes at the current level
        level = []
        for _ in range(len(q)):
            # Get the front node from the queue
            node = q.popleft()
            # Add the node value to the current level list
            level.append(node.data)
            
            # Enqueue the child nodes if they exist
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # Add the current level to the answer list
        list_of_levels.append(level)
    # Return the level-order traversal of the tree
    return list_of_levels
  
def printLevel(level):
    # Iterate through the list and print each element
    for num in level:
        print(num, end=' ')
    print()


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(2)
    root.right.right = Node(1)

    list_of_levels = level_order_traversal(root)
    for level in list_of_levels:
        printLevel(level)