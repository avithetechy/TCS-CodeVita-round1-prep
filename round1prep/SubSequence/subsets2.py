import itertools

def find_kth_combination(string, n, k):
    count = 0
    for combination in itertools.combinations(string, n):
        count += 1
        if count == k:
            return ''.join(combination)

string = "abcdefghijklmnopqrstuvwxyz"
n = int(input("Enter the value of 'n': "))
k = int(input("Enter the value of 'k': "))

result = find_kth_combination(string, n, k)
print(result)
