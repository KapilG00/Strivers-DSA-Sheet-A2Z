class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data: int) -> None:
        """
        Insert node at the head/start of a linkedlist.
        """
        current_node = Node(data)
        current_node.next = self.head
        self.head = current_node
    
    def insert_at_end(self, data: int) -> None:
        """
        Insert node at the tail/end of a linkedlist.
        """
        new_node = Node(data) 
        
        # If linkedlist has no elements
        if not self.head:
            self.head = new_node
            return

        current_node = self.head

        # Until we reach the end of a linkedlist
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node

    def insert_at_kth_position(self, data: int, k: int) -> None:
        """
        Insert node at some arbitrary position inside a linkedlist.
        """
        if k < 0:
            raise IndexError("Position cannot be negative")

        if k == 0:
            self.insert_at_beginning(data)
            return

        current_node = self.head
        idx = 0
        
        # Traversing until (k-1)th node in the linkedlist.
        while current_node and idx < k-1:
            current_node = current_node.next
            idx += 1
        
        if current_node is None:
            raise IndexError("Position out of range")
        
        new_node = Node(data)
        new_node.next = current_node.next
        current_node.next = new_node
   
    def delete_at_beginning(self) -> None:
        """
        Delete node from the head/start of a linkedlist.
        """
        if self.head is None:
            return

        current_node = self.head
        self.head = current_node.next
 
    def delete_at_end(self) -> None:
        """
        Delete node from the tail/end of a linkedlist.
        """
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head

        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        
        previous_node.next = None
        
    def delete_at_kth_position(self, k: int) -> None:
        """
        Delete node from some arbitrary position inside a linkedlist.
        """
        if self.head is None or k < 0:
            return

        if k == 0:
            current_node = self.head
            self.head = self.head.next
            return

        current_node = self.head

        for _ in range(k-1):
            if current_node.next is None:
                return
            current_node = current_node.next
        
        if current_node.next is None:
            return

        node_to_delete = current_node.next
        current_node.next = node_to_delete.next
    
    def calculate_length_of_ll(self) -> int:
        """
        Calculates length of a linked list
        """
        if self.head is None:
            return 0

        current_node = self.head
        length_of_ll = 0

        while current_node:
            current_node = current_node.next
            length_of_ll += 1
        
        return length_of_ll

    def search_in_ll(self, data: int) -> bool:
        """
        Search in a linkedlist
        """
        if self.head is None:
            print("Linked list is empty")
            return False

        current_node = self.head

        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        
        return False

    def display_ll(self) -> None:
        """
        Traverse and print each element of a linkedlist.
        """
        current_node = self.head
        ll_elements = []

        while current_node:
            ll_elements.append(str(current_node.data))
            current_node = current_node.next
        
        print(" -> ".join(ll_elements) + " -> None")



if __name__ == "__main__":

    # Initialize the linkedlist
    ll = LinkedList()

    # Add elements
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(10)
    ll.insert_at_end(40)
    ll.insert_at_kth_position(30, 2)
    ll.insert_at_beginning(50)
    ll.insert_at_beginning(60)
    ll.display_ll()

    # Delete elements
    ll.delete_at_beginning()
    ll.display_ll()
    ll.delete_at_end()
    ll.display_ll()
    ll.delete_at_kth_position(2)
    
    # Print linked list
    ll.display_ll()

    # Calculate length of a linkedlist
    print(ll.calculate_length_of_ll())

    # Search in linkedlist
    print(ll.search_in_ll(340))
