class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# TC: O(logn)
# SC: O(1)
def search_ceil_binary_search_tree(node: Node, target: int):
    ceil = float('inf')
    while node:
        if target == node.data:
            ceil = node.data
            return ceil
        
        if target > node.data:
            node = node.right
        else:
            ceil = node.data
            node = node.left    

    return ceil


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(5)
    root.right = Node(12)
    root.left.left = Node(4)
    root.left.right = Node(7)
    root.left.right.left = Node(6)
    root.right.left = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    print(search_ceil_binary_search_tree(root, 10))
    print(search_ceil_binary_search_tree(root, 11))

