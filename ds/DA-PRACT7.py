class newNode():
    def __init__(self,data):
       self.key=data
       self.left=None
       self.right=None

def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.key,end=" ")
    inorder(temp.right)

def insert(temp,key):
    if not temp:
        root=new_node(key)
        return
    q=[]
    q.append(temp)
    while(len(q)):
        temp=q[0]
        q.pop(0)

        if(not temp.left):
            temp.left=newNode(key)
            break
        else:
            q.append(temp.left)
        if(not temp.right):
            temp.right=newNode(key)
            break
        else:
            q.append(temp.right)

def deleteDeepest(root,d_node):
    q=[]
    q.append(root)
    while(len(q)):
        temp=q.pop(0)
        if temp is d_node:
            temp=None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right=None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left=None
                return
            else:
                q.append(temp.left)

def deletion(root,key):
    if root== None:
        return None
    if root.left==None and root.right==None:
        if root.key==key:
            return None
        else:
            return root
    key_node=None
    q=[]
    q.append(root)
    temp=None
    while(len(q)):
        temp=q.pop(0)
        if temp.key==key:
            key_node=temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
                q.append(temp.right)
    if key_node:
        x=temp.key
        deleteDeepest(root,temp)
        key_node.key=x
    return root

if __name__=='__main__':
    root=newNode(10)
    root.left=newNode(11)
    root.left.left=newNode(7)
    root.left.right=newNode(12)
    root.right=newNode(9)
    root.right.left=newNode(15)
    root.right.right=newNode(8)
    print("Inorder traversal before insertion:",end=" ")
    inorder(root)
    key=12
    insert(root,key)
    print()
    print("Inorder traversal before insertion:",end=" ")
    inorder(root)
    print()
    print("The Tree before the deletion:")
    inorder(root)
    key=11
    root=deletion(root,key)
    print()
    print("The Tree after the deletion:")
    inorder(root)
    
    
    
    
