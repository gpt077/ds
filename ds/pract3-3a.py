class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def insertAtEnd(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = temp
            temp.prev = curr

    def traverse(self):
        curr = self.head
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

    def insertAtGivenPosition(self,data,position):
        count = 1
        curr = self.head
        while count<position-1 and curr != None:
            curr = curr.next
            count += 1
        temp = Node(data)
        temp.next =curr.next
        temp.next.prev = temp
        curr.next = temp
        temp.prev = curr

    def delFromBegin(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                temp = self.head
                self.head = temp.next
                self.head.prev=None
                temp.next = None
                del temp
        except Exception as e:
            print(str(e))

    def delFromEnd(self):
        try:
            if self.head == None:
                raise Exception("Empty Linked List")
            else:
                curr = self.head
                prev = None
                while curr.next != None:
                    curr = curr.next
                curr.prev.next = None
                curr.prev = None
                del curr
        except Exception as e:
            print(str(e))


    def delAtPosition(self,position):
        try:
            if self.head == None:
                 raise exception("Empty Linked List")
            else:
                temp = self.head
                count=1
                while (count < position  and temp!= None):
                    curr = temp
                    temp = temp.next
                    count += 1
                curr.next = temp.next
                temp.next.prev = curr
                temp.next = None
                temp.prev = None
                del curr
        except Exception as e:
            print(str(e))


ll = DoublyLinkedList()
ll.insertAtBegin(10)
ll.insertAtBegin(20)
print("Doubly Linked list after insertion at begining")
ll.traverse()
ll.insertAtBegin(30)
ll.insertAtBegin(40)
print("Doubly Linked list after insertion at begining")                    
ll.traverse()                
ll.insertAtEnd(50)
print("Doubly Linked list after insertion at End")  
ll.traverse()
ll.insertAtBegin(60)
print("Doubly Linked list after insertion at begining")
ll.traverse()
ll.insertAtGivenPosition(70,3)
print("Doubly Linked list after insertion at Given position 3")
ll.traverse()
ll.delFromBegin()
print("Doubly Linked list after Deletion from begining")
ll.traverse()
ll.delFromEnd()
print("Doubly Linked list after Deletion from End")
ll.traverse()
ll.delAtPosition(4)
print("Doubly Linked list after Deletion from given position 4")
ll.traverse()







                    



                



            
