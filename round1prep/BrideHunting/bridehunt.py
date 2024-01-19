# 2 9
# 1 0 1 1 0 1 1 1 1
# 0 0 0 1 0 1 0 0 1
#CALCULATING QUALITIES
def check(x,y):
    if(x<0 or x>r-1 or y<0 or y>c-1):
        return 0
    return l[x][y]

def calc_quality(x,y):
    if (l[x][y]==0):
        return 0
    return check(x-1,y)+check(x+1,y)+check(x,y-1)+check(x,y+1)+check(x-1,y-1)+check(x-1,y+1)+check(x+1,y-1)+check(x+1,y+1)


#GETTING INPUT
r,c=map(int,input().split())
l=[]
for i in range(r):
    temp=list(map(int,input().split()))
    l.append(temp)

#CHECKING THE QUALITIES
#l[0][0]=0
bride={}
for i in range(r):
    for j in range(c):
        quality=0
        if (i!=0 or j!=0):
            quality=calc_quality(i,j)
        if quality!=0:
            bride[i+1,j+1]=quality






#FINDING MAXIMUM QUALITY
max_qual=-1
for coordinate in bride:
    current_qual=bride[coordinate]
    if(current_qual>max_qual):
        max_qual=current_qual
print(max_qual)
#FINDING MIN DISTANCE
#OUTPUT
