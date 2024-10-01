class Node:
    def __init__ (self,coeff,expo):
        self.coeff = coeff
        self.expo = expo
        self.next = None
class poly:
    def __init__(self):
        self.head = None
        self.temp = None
    def creation(self,coeff,expo):    
            newnode = Node(coeff,expo)
            if self.head is None or newnode.expo>self.head.expo:
                newnode.next=self.head
                self.head=newnode
            else:
                self.temp=self.head
                while self.temp.next is not None and newnode.expo<self.temp.next.expo:
                    self.temp=self.temp.next
                newnode.next=self.temp.next
                self.temp.next=newnode
    def display(self):
        self.temp = self.head
        while(self.temp != None):
            print(f"{self.temp.coeff}x^{self.temp.expo}")
            self.temp = self.temp.next    
        
            
p1 = poly()  
num = int(input("enter the number of nodes for poly1:"))
for i in range(num):
    coeff = int(input("enter the coefficient:"))
    expo = int(input("enter the exponent:"))
    p1.creation(coeff,expo)

p2=poly()
num = int(input("enter the number of nodes for poly2:"))
for i in range(num):
    coeff = int(input("enter the coefficient:"))
    expo = int(input("enter the exponent:"))
    p2.creation(coeff,expo)


sub=poly()
def poly_sub(p1,p2):
    l1=p1.head
    l2=p2.head
    while l1 and l2:
        if l1.expo==l2.expo:
            sub.creation(l1.coeff-l2.coeff,l1.expo)
            l1=l1.next
            l2=l2.next
        elif l1.expo>l2.expo:
            sub.creation(l1.coeff,l1.expo)
            l1 = l1.next
        else:
            sub.creation(l2.coeff,l2.expo)
            l2 = l2.next
    while l1:
        sub.creation(l1.coeff,l1.expo) 
        l1=l1.next 
    while l2:
        sub.creation(l2.coeff,l2.expo)  
        l2=l2.next          
poly_sub(p1,p2)
sub.display()
