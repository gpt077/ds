class Stack:
    def __init__(self):
        self.elements =[ ]
    def push(self,data):
        self.elements.append(data)
        return data
    def pop(self):
        if stack.is_empty():
            print('Stack is Empty.')
        else:
            print('Popped Value:' ,self.elements[-1])
            self.elements.pop(-1)
    def peek(self):
        return self.elements[-1]
    def is_empty(self):
        return  len(self.elements) ==0
    def display(self):
        print(self.elements)
stack = Stack()
print(stack.is_empty())
stack.display()
print("Stack after push(1)")
stack.push(1)
print(stack.peek())
stack.display()
print("Stack after push(2)")
stack.push(2)
print(stack.peek())
stack.display()
print("Stack after push(3)")
stack.push(3)
print(stack.peek())
stack.display()
print("Stack after push(4)")
stack.push(4)
print(stack.peek())
stack.display()
print("Stack after push(5)")
stack.push(5)
print(stack.peek())
stack.display()
print(stack.is_empty())
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
print(stack.is_empty())
stack.display()







