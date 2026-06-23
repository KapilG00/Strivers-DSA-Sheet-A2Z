
# TC: O(1)
# SC: O(n)
class ArrayStack:
    def __init__(self, size=100):
        self.ds = [0] * size
        self.capacity = size
        self.topIndex = -1
    
    def push(self, ele):
        if self.topIndex >= self.capacity - 1:
            print("Stack overflow")
            return
        self.topIndex += 1
        self.ds[self.topIndex] = ele

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        top_element = self.ds[self.topIndex]
        self.topIndex -= 1
        return top_element

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return -1
        return self.ds[self.topIndex]

    def isEmpty(self):
        if self.topIndex == -1:
            return True
        return False



stack = ArrayStack(5)
stack.push(5)
stack.push(10)
print(stack.peek())
stack.pop()
print(stack.isEmpty())
print(stack.ds)