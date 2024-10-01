class Queue:
    def __init__(self,size):
        self.size = size 
        self.front = -1
        self.rear = -1 
        self.queue = [0] * self.size
    
    def Enqueue(self, data):
        if self.rear == self.size -1:
            print("Overflow")
        elif self.rear == -1 and self.front == -1:
            self.front = self.rear = 0 
            self.queue[self.rear] = data 
        else:
            self.rear +=1 
            self.queue[self.rear] = data 
        
    def dequeue(self):
        if self.front == -1 and self.rear == -1:
            print("Underflow ")
        elif self.front == self.rear:
            print(f"The deleted element {self.queue[self.rear]}")
            self.front = self.rear = -1 
        else:
            print(self.queue[self.front])
            self.front +=1

    
    def peek(self):
        if self.rear == -1:
            print("Underflow ")
        else:
            print(self.queue[self.rear])
    def display(self):
        if self.rear == -1:
            print("Underflow ")
        else:
            for i in range(self.front,self.rear +1):
                print(self.queue[i])

s = Queue(4)
s.Enqueue(3)        
s.Enqueue(5)        
s.Enqueue(2)
s.display()        
s.dequeue()

print("after deletion")
s.display()
