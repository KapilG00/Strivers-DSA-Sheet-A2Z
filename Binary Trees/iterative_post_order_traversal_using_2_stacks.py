class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(n); where "n" is number of nodes in a BT.
# SC: O(2n); two stacks (stack 1 & stack 2)
def iterative_post_order_traversal(node: Node):
    stack_1 = [node]
    stack_2 = []
    post_order_traversal_list = []
    
    while stack_1:
        top_most_node_of_stack_1 = stack_1.pop()
        stack_2.append(top_most_node_of_stack_1.data)
         
        if top_most_node_of_stack_1.left:
            stack_1.append(top_most_node_of_stack_1.left)
        if top_most_node_of_stack_1.right:
            stack_1.append(top_most_node_of_stack_1.right)

    while stack_2:
        post_order_traversal_list.append(stack_2.pop())     
    
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
