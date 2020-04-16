import math


def fibonacci_finder(n):
    # base case
    if n < 2:
        return n
    # recursively call function
    return fibonacci_finder(n - 1) + fibonacci_finder(n - 2)


# Calculate runtime:
# This function runs a loop dependent the size of sqr(n), therefore
#it is O(n)^1/2
def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)


# This function runs a loop in range of a constant variable (which would be constant time)
# and also 2 loops that are dependent of the size of x, therefore it would be O(n^2)
def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += sum
        for j in range(0, x):
            for k in range(x, x + 15):
                sum += 1


# This function has a loop that depends on the size of n, O(n)
def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print('hi')
