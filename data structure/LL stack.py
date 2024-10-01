class Node:

    def __init__(self,data):

        self.data = data
        self.next = None
        
class stack:

    def __init__(self):

        self.top = None
        self.temp = None
        
    def push(self,data):

        newnode = Node(data)
        if self.top is None:
            self.top=newnode
        else:
            newnode.next = self.top
            self.top = newnode
            
   
    


    def display(self):
        self.temp=self.top
        while self.temp.next is not None:
            print(self.temp.data,end="->")
            self.temp=self.temp.next
        print(self.temp.data)

            
    def creation(self):
        num=int(input("enter size of the stack:"))
        for i in range(num):
            data=int(input("enter elements for the stack:"))
            newnode=Node(data)
            if self.top is None:
                self.top=newnode
                
            else:
                newnode.next=self.top
                self.top=newnode



s=stack()
s.creation()
s.display()
s.push(4)
        
