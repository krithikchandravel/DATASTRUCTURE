class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def creation(self):
        num = int(input("Enter the number of nodes: "))
        for i in range(num):
            data = int(input("Enter the data for node {}: ".format(i + 1)))
            newnode = Node(data)
            if self.head is None:
                self.head = newnode
                self.tail = newnode
                self.tail.next = self.head  # Circular link
            else:
                self.tail.next = newnode
                self.tail = newnode
                self.tail.next = self.head  # Maintain circular link

    def display(self):
        self.temp = self.head
        while self.temp.next != self.head:
            print(self.temp.data, end="->")
            self.temp = self.temp.next
        
        # Print the last node (tail) separately
        print(self.tail.data)

    def insertAtBeg(self):
        data = int(input("Enter the value of new data: "))
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self.tail.next = self.head

    def insertAtEnd(self):
        data = int(input("Enter the num: "))
        newnode = Node(data)
        self.tail.next = newnode
        self.tail = newnode
        self.tail.next = self.head

    def insertAtMid(self):
        data = int(input("Enter the data: "))
        position = int(input("Enter the position: "))
        newnode = Node(data)
        self.temp = self.head
        for i in range(position - 2):
            self.temp = self.temp.next
        newnode.next = self.temp.next
        self.temp.next = newnode

    def deleteAtBeg(self):
        self.temp = self.head
        self.head = self.head.next
        self.tail.next = self.head
        del self.temp 

    def deleteAtEnd(self):
        self.temp = self.head
while self.temp.next != self.tail:
            self.temp = self.temp.next
        self.temp.next = self.head
        del (self.tail)
        self.tail = self.temp

    def deleteAtMid(self):
        position = int(input("Enter the node position you want to delete: "))
        self.temp = self.head
        prev = None
        for i in range(position - 1):
            prev = self.temp
            self.temp = self.temp.next
        prev.next = self.temp.next
        del self.temp

    def count(self):
        count = 1
        self.temp = self.head
        while self.temp.next != self.head:
            count += 1
            self.temp = self.temp.next
        print(count)

cll = CLL()
cll.creation()

print("The linked list is:")
cll.display()
