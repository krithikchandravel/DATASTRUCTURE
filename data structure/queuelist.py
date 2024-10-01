class node:
    def __init__(self,size):
        self.size=size
        self.rear=-1
        self.front=-1
        self.queue=[-1]*self.size
    def dequeue_front(self):
        if self.front==-1 and self.rear==-1:
            print("underflow")
        elif self.front==self.rear:
            print(f"deleted element{self.rear}")
            self.front=self.rear=-1
        elif(self.front==self.size-1):
            self.front=0
        else:
            self.front+=1
    def dequeue_rear(self):
        if self.front==-1 and self.rear==-1:
            print("underflow")
        elif self.rear==0:
            self.rear==self.size-1
        else:
            self.rear=1
    def enqueue_front(self):
        if(self.rear+1)%self.size)==self.front:
            print("overflow")'
        elif self.front==0:
            self.front=self.size-1
            self.queue[self.front]=data
        else:
            self.front=-1
            self.queue[self.front]=data
    def enqueue_rear(self):
        if ((self.rear+1)%self.size)==self.front:
            print("overflow")
            
            
            
