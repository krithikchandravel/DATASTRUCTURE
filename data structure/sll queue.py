class node:

    def __init__(self,data):

        self.data=data
        self.next=None

class queue:

    def __init__(self):
        self.front=None
        self.rear=None

    def creation(self):
        n=int(input("enter no of nodes:"))
        for i in range(n):
            data=int(input("enter data for the nodes:"))
            newnode=node(data)

            if self.front is None:

                self.front=newnode
                self.rear=newnode
            else:
                self.rear.next=newnode
                self.rear=newnode
                
    def display(self):

        self.rear=self.front
        while(self.rear is not None):
            print(self.rear.data)
            self.rear=r=self.rear.next
        print("none")

                
    def enqueue(self):
        data=int(input("enter data to insert:"))
        newnode=node(data)
        while self.rear is not None:
            self.rear=self.rear.next
        self.rear.next=newnode
        
    def dequeue(self):
            self.rear=self.front
            self.front=self.rear.next
            del(self.rear)
        
    def display(self):

        self.rear=self.front
        while(self.rear is not None):
            print(self.rear.data)
            self.rear=r=self.rear.next
        print("none")

        
s = queue()
s.creation()
s.display()
s.enqueue()
s.display()
s.dequeue()
s.display()
