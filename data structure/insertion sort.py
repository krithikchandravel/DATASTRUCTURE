def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key   
    return arr    
num=int(input("Enter the number of array elements:"))
arr=[int(input()) for i in range(num)]
print("Array list:",arr)
insertion_sort(arr)
print("sorted list",arr)


def selectionsort(alist):
    for i in range(0,len(alist)-1):
        min_i=i
        for j in range(i+1,len(alist)):
            if alist[j]<alist[min_i]:
                min_i=j
        temp=alist[i]
        alist[i]=alist[min_i]
        alist[min_i]=temp
alist=[9,6,8,2,6,5,8,2,3,1,5,7,8,0,97,7]
selectionsort(alist)
print("sorted array",alist)



def count(a,digit,n):
    k = 10
    count = [0]*(k)
    b = [0]*n
    for i in range(n):
        count[(a[i] //digit)%10] += 1

    for j in range(1,k+1):
        count[j] = count[j-1]+count[j]

    for k in range(n-1,-1,-1):
        count[(a[i]//digit)%10]=count[(a[i]//digit)%10]-1
        b[count[(a[i]//digit)%10]] = a[i]
    return(b)

arr=[423,8,530,90,231,11,45,670]
max_value = max(arr)
digit = 1
while(max_value/digit>0):
    arr=count(arr,digit,len(arr))
    digit=digit*10
print(arr)
