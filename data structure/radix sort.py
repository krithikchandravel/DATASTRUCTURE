(n    n=len(arr) 
    k=10
    count=[0]*(k)
    b=[0]*n
    for i in range(n):
        count[(arr[i]//dig)%10]=count[(arr[i]//dig)%10]+1
    for i in range(1,k):
        count[i]=count[i-1]+count[i]
    for i in range(n-1,-1,-1):
        count[(arr[i]//dig)%10]=count[(arr[i]//dig)%10]-1
        b[count[(arr[i]//dig)%10]]=arr[i]
    return b 
   


arr=[432,8,530,99,699,54,78]
max_value=max(arr)
dig=1
while max_value/dig>0:
    arr=count(arr,dig)
    dig*=10

print(arr)
    
