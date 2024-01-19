def prime(n):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
    if cnt==2:
        return True
    else:
        return False

d,p=map(int,input().split())
q=d//p
num=1
l=[]
for i in range(p):
    temp=[]
    for j in range(q):
        temp.append(num)
        num+=1
        
    l.append(temp)
#print(l)


length=len(l)
total=0
#print('q;',q)
#print('p:',p)
for i in range(q):
    count=0
    for j in range(p):
        #print(l[j][i],end=' ')
        if prime(l[j][i]):
            count+=1 
        else:
            break
    #print(count)
    #print()
    if count==p:
        total+=1
print(total)
