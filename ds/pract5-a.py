class Queue:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q=Queue()
print("Before inserting an element")
q.display()
q.enqueue(1)
print("After inserting an element(1)")
q.display()
q.enqueue(2)
print("After inserting an element(2)")
q.display()
q.enqueue(3)
print("After inserting an element(3)")
q.display()
q.enqueue(4)
print("After inserting an element(4)")
q.display()
q.enqueue(5)
print("After inserting an element(5)")
q.display()

q.dequeue()
print("After removing an element")
q.display()
q.dequeue()
print("After removing an element")
q.display()
q.dequeue()
print("After removing an element")
q.display()



