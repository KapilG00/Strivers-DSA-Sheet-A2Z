class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(n); where "n" is number of nodes in a BT.
# SC: O(n)
def iterative_in_order_traversal(node: Node):
    stack = []
    in_order_traversal_list = []

    while True:
        # If the current node is not None
        if node is not None:
            # Push the current node to the stack
            stack.append(node)
            # Move to the left child of the current node
            node = node.left
        else:
            # If the stack is empty, break the loop
            if not stack:
                break  
            # Retrieve a node from the stack
            node = stack.pop()
            # Add the node's value to the in-order traversal list
            in_order_traversal_list.append(node.data)
            # Move to the right child of the current node
            node = node.right

    return in_order_traversal_list             



if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(2)
    root.right.right = Node(1)

    print(iterative_in_order_traversal(root))
