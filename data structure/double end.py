class queue:
    def __init__(self):
        self.size=size
        self.front=-1
        self.rear=-1
        self.queue=[0]*self.size
        
    def enqueue_rear(self):
        data=int(input("enter data :"))
        if self.rear==self.size-1:
            print("overflow")
        elif self.front==-1 and self.rear==-1:
            self.front=self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear+=1
            self.queue[self.rear]=data
    def enqueue_front(self):
        data=int(input("enter data:"))
        if self.front==-1 and self.rear==-1:
            self.front=self.size-1
            self.rear=self.size-1
            self.queue[self.rear]=data
            
        elif self.front==0:
            print("overflow")
        else:
            self.front-=1
            self.queue[self.front]=data
    def dequeue_front(self):
        if self.rear==-1 and self.front==1:
            print("underflow")
        elif self.rear==0 and self.front==0:
            print(f"deleted element{self.front}")
            self.front=self.rear=-1
        else:
            print(self.queue[self.front])
            self.front+=1
    def dequeue_rear(self):
        if self.rear==-1 and self.front==-1:
            print("underflow")
        elif self.rear==self.front:
            print(self.queue[self.rear])
            self.rear-=1
        else:
            print(self.queue[self.rear])
            self.rear-=1
    def display(self):
        i=self.front
        while True:
            print(self.queue[i],end="->")
            if i==self.rear:
                break
            i=(i+1)%self.size
        print("None")
size=int(input("enter size:"))
q=queue()
for i in range(size):
    q.enqueue_rear()
q.display()
q.dequeue_rear()
q.dequeue_front()
q.display() 
