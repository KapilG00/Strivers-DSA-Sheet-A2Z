class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(2n); where "n" is number of nodes in a BT.
# SC: O(n)
def iterative_post_order_traversal(node: Node):
    stack = []
    post_order_traversal_list = []
    
    while node is not None or stack:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            temp = stack[-1].right

            if temp is None:
                temp = stack.pop()
                post_order_traversal_list.append(temp.data)
                
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    post_order_traversal_list.append(temp.data)
            else:
                node = temp

    return post_order_traversal_list            



if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(2)
    root.right.right = Node(1)

    print(iterative_post_order_traversal(root))
