lst=[]
n,k=map(int,input().split(','))
for i in range(n,0,-1):
    if n%i==0:
        lst.append(i)
for i in lst:
    print(i)
#k=int(input("enter the k:"))
print(lst[k-1])

