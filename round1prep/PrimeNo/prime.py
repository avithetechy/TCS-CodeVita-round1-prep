n=5
l=[3,4,5,2]
q=min(l)
l.remove(q)
p=2
print(l)
res=False
while p<10**10:
    print("p value:",p)
    if p==q:
        continue
    else:
        c=0
        for j in range(1,p+1):
            if p%j == 0:
                c+=1
        print("count:",c)
        if c==2:
            count=0
            for v in l:
                print("v value",v)
                if p%v == q:
                    count+=1
            if count == len(l):
                print("The smallest prime is:",p)
                res=True
                break
            else:
                p+=1
        else:
            p+=1
if res==False:
    print("None")