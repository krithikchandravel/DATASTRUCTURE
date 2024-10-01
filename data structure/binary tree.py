class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.temp=None
        self.temp1=None

    def insert(self,data):
        data=int(input("enter a data:"))
        newnode=Node(data)
        if self.root is None:
            self.root=newnode

        else:
            temp=temp1=self.root
            flag=0
            while True:
                if self.temp.left is None:
                    self.temp.left=newnode
                    break
                elif self.temp.right is next:
                    self.temp.right=newnode
                    break
                elif flag==0:
                    temp=temp1.left
                    flag=1
                else:
                    temp=temp1.right
                    flag=0
                    temp1=temp1.left
    
