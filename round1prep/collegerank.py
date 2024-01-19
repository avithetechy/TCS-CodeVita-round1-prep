c,n=map(int,input().split())
vacancy=list(map(int,input().split()))
info=[]
for i in range(n):
    temp=list(map(str,input().split(",")))
    info.append(temp)
#print(*info)

sorted_info=sorted(info, key=lambda x: x[1], reverse=True)
#print(*sorted_info)
for i in sorted_info:
    i[1]=float(i[1])
#print(*sorted_info)

for i in sorted_info:
    stud_name=i[0]
    stud_id=int(stud_name.split('-')[1])
    i[0]=stud_id
for student in sorted_info:
    print(student)

d={}
for i in range(c):
    d_key='C-'+str(i+1)
    d[d_key]=vacancy[i]
#print(d)

allocated_d={}
for student in sorted_info:
    for i in range(2,len(student)):
        preference=student[i]
        if d[preference]>0:
            allocated_d[preference]=student[1]
            d[preference]-=1
            break
print(allocated_d)

for key in d:
    if key in allocated_d:
        print(key,allocated_d[key])
    else:
        print(key,'N/A')
