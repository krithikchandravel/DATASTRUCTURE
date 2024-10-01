class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.temp = None
        

    def creation(self):
        num = int(input("Enter the number of nodes: "))
        for i in range(num):
            data = int(input("Enter the data for node {}: ".format(i + 1)))
            newnode = Node(data)
            if self.head is None:
                self.head = newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                newnode.prev = self.temp
                self.temp = newnode
                
                
    def display(self):
        self.temp = self.head
        while self.temp.next is not None:
            print(self.temp.data)
            self.temp = self.temp.next
        print(self.temp.data)

    def insertATBeg(self):
        data = int(input("Enter the value of new data: "))
        newnode = Node(data)
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

    def insertAtEnd(self):
        data = int(input("Enter the num: "))
        newnode = Node(data)
        self.temp = self.head
        while(self.temp.next is not None):
            self.temp = self.temp.next
        self.temp.next = newnode
        newnode.prev = self.temp

    def insertAtMid(self):
        data = int(input("Enter the data: "))
        newnode = Node(data)
        position = int(input("Enter the position: "))
       
        self.temp = self.head
        for i in range(position - 2):
            self.temp = self.temp.next
        newnode.next = self.temp.next
        newnode.prev = self.temp
        self.temp.next = newnode

    def deleteAtBeg(self):
        self.temp = self.head
        self.head = self.head.next
        del(self.temp)
        

    def deleteAtEnd(self): 
        self.temp = self.head
        while(self.temp.next is not None):
            self.temp = self.temp.next
        self.temp.prev.next = None
        del(self.temp)    
    def deleteAtMid(self):
        position = int(input("enter the position to delete"))
        self.temp = self.head
        for i in range(position-1):
            self.temp = self.temp.next 
        self.temp.prev.next = self.temp.next
        self.temp.next.prev = self.temp.prev
        del(self.temp)    

dll = DLL()
dll.creation()
dll.deleteAtMid()
print("The linked list is:")

dll.display()  
