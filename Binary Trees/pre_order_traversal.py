class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(n); where "n" is number of nodes in a BT.
# SC: O(n); if we have a binary tree as a skew tree in worst case.
def pre_order_traversal(node: Node):
    if node == None:
        return
    
    print(node.data)

    pre_order_traversal(node.left)

    pre_order_traversal(node.right)


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(2)
    root.right.right = Node(1)

    pre_order_traversal(root)

