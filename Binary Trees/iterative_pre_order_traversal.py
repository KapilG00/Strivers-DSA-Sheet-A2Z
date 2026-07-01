class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(n); where "n" is number of nodes in a BT.
# SC: O(n)
def iterative_pre_order_traversal(node: Node):
    stack = [node]
    pre_order_traversal_list = []
    if node is None:
        return pre_order_traversal_list
    
    while stack:
        top_most_node = stack.pop()
        pre_order_traversal_list.append(top_most_node.data)

        if top_most_node.right:
            stack.append(top_most_node.right)
        if top_most_node.left:
            stack.append(top_most_node.left)

    return pre_order_traversal_list             



if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(2)
    root.right.right = Node(1)

    print(iterative_pre_order_traversal(root))
