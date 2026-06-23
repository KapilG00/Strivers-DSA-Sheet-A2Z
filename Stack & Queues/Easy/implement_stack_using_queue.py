from queue import Queue


# TC: O(1)
# SC: O(1)
class QueueStack:
    def __init__(self):
        # Queue
        self.q = Queue()

    # Method to push element in the stack.
    def push(self, ele):
        s = self.q.qsize()
        self.q.put(ele)

        # Move elements before new element to back.
        for _ in range(s):
            self.q.put(self.q.get())

    # Method to pop element from stack
    def pop(self):
        n = self.q.queue[0]
        print(n)
        self.q.get()
        return n

    # Method to return the top of stack
    def top(self):
        return self.q.queue[0]

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.q.empty()



stack = QueueStack()
stack.push(5)
stack.push(10)
print(stack.top())
stack.pop()
print(stack.isEmpty())
print(stack.q.queue)