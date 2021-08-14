class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
    def insertNode(self,rootNode,val):
        if val<=rootNode.info:
            if rootNode.left is None:
                rootNode.left=Node(val)
            else:
                self.insertNode(rootNode.left,val)
        else:
            if rootNode.right is None:
                rootNode.right=Node(val)
            else:
                self.insertNode(rootNode.right,val)

    def insert(self, val):
        if self is None:
            self=BinarySearchTree()
            self.root=Node(val)
        elif self.root is None:
            self.root=Node(val)    
        else:
            self.insertNode(self.root,val)
        return
            

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
