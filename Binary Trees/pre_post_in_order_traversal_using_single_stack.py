class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(3n); where "n" is number of nodes in a BT.
# SC: O(4n); 3 traversal stacks and 1 other stack.
def pre_post_in_order_traversal(node: Node):
    pre_order, in_order, post_order = [], [], []

    # If the tree is empty, return empty traversals
    if node is None:
        return []

    # Stack to maintain nodes and their traversal state
    stack = [(node, 1)]

    while stack:
        node, state = stack.pop()

        # This is part of pre-order
        if state == 1:
            # Store the node's data in the pre-order traversal
            pre_order.append(node.data)

            # Move to state 2 (in-order) for this node
            stack.append((node, 2))

            # Push left child onto the stack for processing
            if node.left:
                stack.append((node.left, 1))

        # This is a part of in-order
        elif state == 2:
            # Store the node's data in the in-order traversal
            in_order.append(node.data)

            # Move to state 3 (post-order) for this node
            stack.append((node, 3))

            # Push right child onto the stack for processing
            if node.right:
                stack.append((node.right, 1))

        # This is part of post-order
        else:
            # Store the node's data in the postorder traversal
            post_order.append(node.data)

    # Returning the traversals
    return [pre_order, in_order, post_order]   



if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(2)
    root.right.right = Node(1)

    traversals = pre_post_in_order_traversal(root)

    # Extracting and printing the traversals
    pre_order = traversals[0]
    in_order = traversals[1]
    post_order = traversals[2]

    print("Preorder traversal:", *pre_order)
    print("Inorder traversal:", *in_order)
    print("Postorder traversal:", *post_order)
