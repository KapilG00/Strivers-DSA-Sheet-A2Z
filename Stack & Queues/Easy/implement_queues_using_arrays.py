
# TC: O(1)
# SC: O(1)
class ArrayQueue:
    def __init__(self):
        self.ds = [0] * 10
        self.start = -1 
        self.end = -1
        self.current_size = 0
        self.max_size = 10
    
    def push(self, ele):
        # Check if queue is full.
        if self.current_size == self.max_size:
            print("Queue is full!!")
            return 1
        # Check if queue is empty.
        if self.end == -1:
            self.start = 0
            self.end = 0
        else:
            #
            self.end = (self.end + 1) % self.max_size

        self.ds[self.end] = ele
        self.current_size += 1
    
    def pop(self):
        if self.start == -1:
            print("Queue is empty!!")
            return 1
        
        poped_ele = self.ds[self.start]
        
        if self.current_size == 1:
            self.start = -1
            self.end = -1
        else:
            #
            self.start = (self.start + 1) % self.max_size

        self.current_size -= 1
        return poped_ele    

    def dequeue(self):
        if self.start == -1:
            print("Queue is Empty")
            return 1
        return self.ds[self.start]

    def isEmpty(self):
        if self.current_size == 0:
            return True
        return False



queue = ArrayQueue(5)
queue.push(5)
queue.push(10)
print(queue.peek())
queue.pop()
print(queue.isEmpty())
print(queue.ds)