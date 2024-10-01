class Node:
    def init(self,data):
        self.data = data
        self.next = None

class SLL:
    def init(self):
        self.head = None
        self.temp = None
    
    def creation(self):
        num = int(input("Enter the no of nodes"))
        for i in range(num):
            data = int(input("Enter the data for nodes"))
            newnode = Node(data)
            if self.head is None:
                self.head=newnode
                self.temp = newnode
            else:
                self.temp.next = newnode
                self.temp = newnode
   

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data,end = "->")
            self.temp = self.temp.next

    def insertionatbeg(self):
        data=int(input("enter data to insert"))
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode


    def insertatlast(self):
        self.temp = self.head
        data=int(input("enter data to insert at last "))
        newnode=Node(data)
        while(self.temp.next is not None):
            self.temp = self.temp.next
        self.temp.next = newnode
    
    def insertatmid(self):
        self.temp = self.head
        data=int(input("enter data to insert at middle"))
        newnode=Node(data)
        for i in range(2-1):
            prev = self.temp
            self.temp = self.temp.next
        newnode.next = self.temp
        prev.next = newnode

    def deletionatbeg(self):
        self.temp=self.head
        self.temp=self.temp.next
        
        


        
linkedlist=SLL()

linkedlist.creation()

linkedlist.insertiontbeg()
linkedlist.insertatlast()
linkedlist.insertatmid()
linkedlist.display()
