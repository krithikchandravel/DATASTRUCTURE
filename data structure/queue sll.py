class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self,size):
        self.size = size
        self.front = None
        self.rear = None
        

    def enqueue(self):
        data = int(input("enter the data"))
        Newnode = Node(data)
        if self.front == None and self.rear == None:
            self.front = self.rear = Newnode
        else:
            self.rear.next = Newnode
            self.rear = Newnode

    def dequeue(self):
        if self.front == None and self.rear == None:
            print("Underflow")   
        elif(self.front == self.rear):
            self.temp = self.front
            self.front = self.rear = None
            del(self.temp)
        else:
            self.temp = self.front  
            self.front =  self.front.next
            del(self.temp)
            
    def peek(self):
        if self.rear==-1:
            print("underflow")
        else:
            self.rear=self.front
            print(self.rear.data)

    def display(self):
        self.temp = self.front
        while(self.temp != None):
            print(self.temp.data,end="->") 
            self.temp = self.temp.next  
        print("None")         

size = int(input("Enter the size :"))
Q = Queue(size)
for i in range(size):
    Q.enqueue()
#Q.display()
#Q.dequeue()
Q.peek()
Q.display()
