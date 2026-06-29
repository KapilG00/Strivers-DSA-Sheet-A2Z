class MaxHeap:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        # Current number of elements
        self.size = 0 
        # Internal array for storing heap elements
        self.arr = [0]*capacity
    
    # Return parent node index of node at index idx
    def parent(self, idx: int):
        return (idx-1)//2

    # Return left child index of node at index idx
    def left(self, idx: int):
        return 2*idx+1

    # Return right child index of node at index idx
    def right(self, idx: int):
        return 2*idx+2
    
    # Insert element at end of a heap
    def insert(self, node_value: int) -> None:
        if self.size == self.capacity:
            print("Heap is full!!")
            return

        # Insert 
        self.arr[self.size] = node_value
        bubbled_up_elements_idx = self.size
        self.size += 1

        # Make it max-heap if it is not after insertion
        while bubbled_up_elements_idx != 0 and self.arr[self.parent(bubbled_up_elements_idx)] < self.arr[bubbled_up_elements_idx]:
            self.arr[self.parent(bubbled_up_elements_idx)], self.arr[bubbled_up_elements_idx] = self.arr[bubbled_up_elements_idx], self.arr[self.parent(bubbled_up_elements_idx)]
            # bubbled_up_elements_idx is not representing the size of the heap.
            # It is representing the current position of the newly inserted element.
            # Hence, we need to update the bubbled_up_elements_idx value to keep track
            # of the bubbling up node.
            bubbled_up_elements_idx = self.parent(bubbled_up_elements_idx)
    
    # Heapify down
    def heapify(self, ind):
        li = self.left(ind)
        ri = self.right(ind)
        largest = ind

        if li < self.size and self.arr[li] > self.arr[largest]:
            largest = li

        if ri < self.size and self.arr[ri] > self.arr[largest]:
            largest = ri

        if largest != ind:
            self.arr[ind], self.arr[largest] = (
                self.arr[largest],
                self.arr[ind]
            )
            self.heapify(largest)

    # Return maximum element
    def get_max(self):
        if self.size == 0:
            return float("-inf")
        return self.arr[0]

    # Extract maximum element
    def extract_max(self):
        if self.size <= 0:
            return float("-inf")

        if self.size == 1:
            self.size -= 1
            return self.arr[0]

        maxi = self.arr[0]

        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1

        self.heapify(0)

        return maxi

    # Increase key
    def increase_key(self, i, val):
        self.arr[i] = val

        while i != 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = (
                self.arr[i],
                self.arr[self.parent(i)]
            )
            i = self.parent(i)

    # Delete element at index i
    def delete(self, i):
        self.increase_key(i, float("inf"))
        self.extract_max()

    def print_heap(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()
        
   
          

    



if __name__ == "__main__":
    mh = MaxHeap(10)
    mh.insert(4)
    mh.insert(1)
    mh.insert(2)
    mh.insert(6)
    mh.insert(7)
    mh.insert(3)
    mh.insert(8)
    mh.insert(5)