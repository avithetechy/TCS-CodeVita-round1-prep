# def subsets(s):  
#     if len(s) == 0:  
#         return [[]]  
#     x = subsets(s[:-1])  
#     return x + [[s[-1]] + y for y in x]  
# # Define the set  
# s = ['a','b','c']  
# # Find all subsets  
# result = subsets(s)  

# # Print the subsets  
# print(result)

import itertools

# def find_subsets(string):
    
#     comb = []
#     for i in range(len(string) + 1):
#         comb += itertools.combinations(string, i)
#     subsets = []
#     for c in comb:
#         subset = ''.join(c)
#         if subset != '':
#             subsets.append(subset)
#     return subsets


# string = 'abcdefghijklmnopqrstuvwxyz'
# # subsets = find_subsets(string)
# # for i in subsets:
# #     print(i)

# comb=itertools.combinations(string, 4)
# print(comb)
string = "abcdefghijklmnopqrstuvwxyz"
k=int(input(":"))
n=int(input(':'))
combinations = itertools.combinations(string, n)
lst=[]
for combination in combinations:
    temp=''.join(combination)
    lst.append(temp)
lst.sort()
print(lst[k-1])