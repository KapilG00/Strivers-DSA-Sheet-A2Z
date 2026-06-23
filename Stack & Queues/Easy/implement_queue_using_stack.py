# TC: O(n)
# SC: O(n)
class StackQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    # Method to push elements in the queue
    def push(self, x):
        '''Pop out elements from the first stack 
        and push on top of the second stack'''
        while self.st1:
            self.st2.append(self.st1.pop())

        # Insert the desired element
        self.st1.append(x)

        '''Pop out elements from the second stack 
        and push back on top of the first stack'''
        while self.st2:
            self.st1.append(self.st2.pop())

    # Method to pop element from the queue
    def pop(self):
        # If stack is empty.
        if not self.st1:
            print("Stack is empty")
            return -1

        top_element = self.st1.pop()
        return top_element

    # Method to get the front element from the queue
    def peek(self):
        # If stack is empty.
        if not self.st1:
            print("Stack is empty")
            return -1

        return self.st1[-1]

    # Method to find whether the queue is empty
    def is_empty(self):
        return not self.st1




queue = StackQueue()
queue.push(5)
queue.push(10)
print(queue.peek())
queue.pop()
print(queue.is_empty())