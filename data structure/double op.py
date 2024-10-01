class queue:

    def __init__(self,size):

        self.size=size
        self.front=-1
        self.rear=-1
        self.queue=[0]*self.size
        
    def enqueue_rear(self):
        data=int(input("enter your data:"))
        if self.rear==self.size-1:
            print("overflow")
        elif self.rear==-1 and self.front==-1:
            self.rear=self.front=0
            self.queue[self.rear]=data
        else:
            self.rear+=1
            self.queue[self.rear]=data
            
    def enqueue_front(self):
        data=int(input("enter data:"))
        if self.front==self.size-1:
            print("overflow")
        elif self.front==self.rear:
            self.queue[self.rear]=data
            
        else:
            self.rear=self.front
            self.front+=1
            self.queue[self.rear]=data
            self.front=self.rear
            
    def display(self):
        i=self.front
        while True:
            print(self.queue[i],end="->")
            if i==self.rear:
                break
            i=(i+1)%self.size
        print("None")
        
size=int(input("enter size:"))
q=queue(size)
for i in range(size):
    q.enqueue_front()
q.display()
 

    
