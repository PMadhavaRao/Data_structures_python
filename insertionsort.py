l=[]
n=int(input("enter number of elements of list"))
for i in range(n):
    x=int(input("enter data"))
    l.append(x)
print(l)
for c in range(1,len(l)):
    temp=l[c]
    d=c-1
    while d>=0 and temp<l[d] :
                l[d+1]=l[d]
                d-=1
    l[d+1]=temp
mylist=[]
print("sorted array is :")
for i in range(len(l)):
    mylist.append(l[i])
print(mylist)
    
              
