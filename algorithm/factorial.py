
def factorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total
print(factorial(5))

def recursion(num):
    if num <= 1:
        return 1
    return num * recursion(num-1)