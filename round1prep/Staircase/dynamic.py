def countways(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        ways=[0]*(n+1)
        ways[1]=1
        ways[2]=2
        
        for i in range(3,n+1):
            ways[i] = ways[i-1]+ways[i-2]
        return ways[n]

n=int(input("enter no of steps:"))
no_of_ways=countways(n)
print(f"no of ways to climb {n} steps is:{no_of_ways}")