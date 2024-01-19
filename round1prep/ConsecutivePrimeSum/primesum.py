def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
n=int(input("input:"))
count=0
sum=2
lst=[]
for i in range(3,n+1):
    y=isprime(i)
    if y==True:
        sum+=i
        if isprime(sum)==True:
            if sum<=n:
                lst.append(sum)
                count+=1
            else:
                break
#print(lst)
print(count)