n=int(input("no of elements:"))
x=int(input("constraints:"))
l=list(map(int,input().split()))
maxi=0
sums=0
# for i in range(0,x):
#     for j in range(0,n):
#         if l[j]>maxi:    
#             maxi=l[j]
maxi=max(l)
    # for a in range(0,n):
    #     if l[a]==maxi:
    #         l[a]=maxi//2
place=l.index(maxi)
l[place]=maxi//2
sums=sums+sum(l)
print(l)
print(sums)
print(l.index(20))