class MinHeap:
    def __init__(self, capacity):
        """
        Constructor for initializing the heap.
        capacity : Maximum number of elements that can be stored in the heap.
        """
        # Store maximum allowed size
        self.capacity = capacity 
        # Current number of elements
        self.size = 0 
        # Internal array for storing heap elements
        self.arr = [0] * capacity 

    # Return parent index of node at index i
    def parent(self, i):
        return (i - 1) // 2

    # Return left child index of node at index i
    def left(self, i):
        return 2 * i + 1

    # Return right child index of node at index i
    def right(self, i):
        return 2 * i + 2

    # Insert a new key into the heap
    def insert(self, x):
        if self.size == self.capacity:
            print("Binary Heap Overflow")
            return

        # Place new element at the end
        self.arr[self.size] = x
        k = self.size  # index of inserted element
        self.size += 1

        # Bubble up to fix min-heap property
        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k], self.arr[self.parent(k)]
            k = self.parent(k)

    # Heapify function (fix min-heap property starting at index ind)
    def heapify(self, ind):
        li = self.left(ind)
        ri = self.right(ind)
        smallest = ind

        # Check if left child is smaller
        if li < self.size and self.arr[li] < self.arr[smallest]:
            smallest = li
        # Check if right child is smaller
        if ri < self.size and self.arr[ri] < self.arr[smallest]:
            smallest = ri

        # If parent is not smallest, swap and recurse
        if smallest != ind:
            self.arr[ind], self.arr[smallest] = self.arr[smallest], self.arr[ind]
            self.heapify(smallest)

    # Return the minimum element (root of heap)
    def get_min(self):
        if self.size == 0:
            return float("inf")  # Return infinity if heap is empty
        return self.arr[0]

    # Extract minimum element and fix heap
    def extract_min(self):
        if self.size <= 0:
            return float("inf")  # If empty, return infinity
        if self.size == 1:
            self.size -= 1
            return self.arr[0]

        # Store minimum value
        mini = self.arr[0]

        # Move last element to root
        self.arr[0] = self.arr[self.size - 1]
        self.size -= 1

        # Call heapify on root
        self.heapify(0)
        return mini

    # Decrease key value at index i to val
    def decrease_key(self, i, val):
        self.arr[i] = val  # Update value
        # Bubble up until heap property is satisfied
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)

    # Delete element at index i
    def delete(self, i):
        # First decrease its value to -infinity
        self.decrease_key(i, float("-inf"))
        # Then extract minimum (which removes it)
        self.extract_min()

    # Print heap elements
    def print_heap(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()


# Driver code to test
if __name__ == "__main__":
    mh = MinHeap(20)
    mh.insert(4)
    mh.insert(1)
    mh.insert(2)
    mh.insert(6)
    mh.insert(7)
    mh.insert(3)
    mh.insert(8)
    mh.insert(5)

