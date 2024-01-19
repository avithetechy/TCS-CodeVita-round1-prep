n,r=map(int,input().split())
lst=list(map(int,input().split()))
rng=[]
for i in range(r):
    x,y=map(int,input().split())
    rng.append([x,y])
count=[0]*r
for i in range(r):
    for j in lst:
        if j in range(rng[i][0],rng[i][1]+1):
            count[i]+=1
print(*count)