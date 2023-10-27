class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def insertAtBegening(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            temp.next=self.head
            self.head=temp
            
    def insertAtEnd(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=temp

    def InsertAtGivenPosition(self,data,position):
        count=1
        curr=self.head
        while count < position-1 and curr!=None:
            curr=curr.next
            count+=1
        temp=Node(data)
        temp.next=curr.next
        curr.next=temp

    def traverse(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
            
    def delFromBegining(self):
        try:
            if self.head==None:
                raise Exception("Empty Linked List")
            else:
                temp=self.head
                self.head=self.head.next
                del temp
        except Exception as e:
            print(str(e))

    def delFromEnd(self):
        try:
            if self.head==None:
                raise Exception("Empty Linked List")
            else:
                curr=self.head
                prev=None
                while curr.next!=None:
                    prev=curr
                    curr=curr.next
                prev.next=curr.next
                del curr
        except Exception as e:
            print(str(e))

    def delAtPosition(self,position):
        try:
            if self.head==None:
                raise Exception("Empty Linked List")
            else:
                curr=self.head
                prev=None
                count=1
                while curr.next!=None and count < position:
                    prev=curr
                    curr=curr.next
                    count+=1
                prev.next=curr.next
                del curr
        except Exception as e:
            print(str(e))

L1=linkedList()
print("Linked list before Insertion")
L1.traverse()
L1.insertAtBegening(10)
L1.insertAtBegening(20)
print("Linked list after Insertion")
L1.traverse()
L1.insertAtBegening(50)
L1.insertAtBegening(40)
print("Linked list after Inserting 30 & 40")
L1.traverse()
L1.insertAtEnd(50)
print("Linked list after Inseting 50 at end")
L1.traverse()
L1.insertAtBegening(60)
print("Linked list after Inserting 60 at start")
L1.traverse()
L1.InsertAtGivenPosition(70,3)
print("Linked list after Inseting 70 at position 3")
L1.traverse()
L1.delFromBegining()
print("Linked list after deleting from begining")
L1.traverse()
L1.delFromEnd()
print("Linked list after deleting from end")
L1.traverse()
L1.delAtPosition(4)
print("Linked list after deleting from position 4")
L1.traverse()


