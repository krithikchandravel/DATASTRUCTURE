class Node:
    def __init__(self,data):
        self.data = data 
        self.next =  None 

class Stack:
    def __init__(self):
        self.top = None 
        self.temp = None 
    
    def push(self):
        data = int(input("Enter the data "))
        newnode = Node(data)
        if self.top is None:
            self.top = newnode 
        else: 
            newnode.next = self.top 
            self.top = newnode 
    
    def Pop(self):
        self.temp = self.top 
        if self.top is None:
            print("Underflow")
        else:
            self.top = self.top.next 
            print(f"Deleted element {self.temp.data}")
            del(self.temp)
    
    def display(self):
        self.temp = self.top 

        while self.temp.next is not None:
            print(self.temp.data)
            self.temp = self.temp.next 
        print(self.temp.data)

    def peek(self):
        if self.top is None: 
            print("Underflow")
        else:
            print(f"The peek is [{self.top.data}]")

if __name__ == "__main__":
    num = int(input("Enter the "))
    s = Stack()
    for i in range(num):
        s.push()
    s.Pop()
    s.peek()
    s.display()
