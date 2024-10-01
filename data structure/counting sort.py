q=int(input("enter size of the list:"))
arr=[]
for i in range(q):
    m=int(input("enter array elements:"))
    arr.append(m)
n=len(arr) 
k=max(arr)
count=[0]*(k+1)
b=[0]*n
for i in range(n):
    count[arr[i]]=count[arr[i]]+1
for i in range(1,k+1):
    count[i]=count[i-1]+count[i]
for i in range(n-1,-1,-1):
    count[arr[i]]=count[arr[i]]-1
    b[count[arr[i]]]=arr[i]
    arr1=b.copy() 
print("Sorting Array:",arr1)


