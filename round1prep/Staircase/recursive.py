n = int(input("Enter number of Stairs:"))
def calc(x):
    if x <= 1:
        return x
    return calc(x - 1) + calc(x - 2)


def count(n):
    return calc(n + 1)


print("Number of ways:", count(n))