class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


def create_ll(ll_elements: list[int]) -> Node:
    """
    Helper function to create a linkedlist.
    """
    head_node = Node(ll_elements[0])
    current_node = head_node

    for ele in ll_elements[1:]:
        current_node.next = Node(ele)
        current_node = current_node.next
    
    return head_node

def print_ll(head_node: Node) -> None:
    """
    Prints all the nodes of a linkedlist.
    """
    current_node = head_node

    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    
    print("None")

def reverse_ll_brute_force(head_node: Node) -> None:
    """
    Reverse a linked list using stack in brute-force approach.
    TC: O(2n), taken by both the loops O(n) each.
    SC: O(n), taken by stack.
    """
    stack = []
    temp_node = head_node

    while temp_node:
        stack.append(temp_node.data)
        temp_node = temp_node.next
    
    temp_node = head_node
    while temp_node:
        temp_node.data = stack.pop()
        temp_node = temp_node.next   

def reverse_ll_optimal(head_node: Node) -> Node:
    """
    Reverse a linkedlist in-place.
    TC: O(n)
    SC: O(1)
    """
    current_node = head_node
    previous_node = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    
    return previous_node



if __name__ == "__main__":
    head_node = create_ll([1,2,3,4,5])
    print_ll(head_node)

    #reverse_ll_brute_force(head_node)
    new_head_node = reverse_ll_optimal(head_node)
    print_ll(new_head_node)
