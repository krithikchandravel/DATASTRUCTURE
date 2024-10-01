n=int(input("enter size of the array:"))
li=[]
for i in range(n):
    k=int(input("enter array elements:"))
    li.append(k)
m=int(input("enter element to search:"))
flag=0
for i in li:
    if(m==i):
        flag=1
if(flag==1):
    print("element found")
else:
    print("element not found")
