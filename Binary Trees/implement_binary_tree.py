class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == "__main__":
    root = Node(5)
    root.left = Node(4)
    root.right = Node(3)
    root.left.left = Node(6)
    root.left.right = Node(7)
    root.right.left = Node(2)
    root.right.right = Node(1)



#        5       
#      /   \
#     4     3
#    / \   / \
#   6   7 2   1
