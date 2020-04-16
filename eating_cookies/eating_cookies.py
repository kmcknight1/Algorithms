#!/usr/bin/python

import sys
'''
Spec: 
  -can eat 0, 1, 2, or 3 cookies 
  -how many combinations can be made to make up n number of cookies

  -if n == 0:
    answer -> 1
  
  -if n == 1:
    answer -> 1

  -if n == 2:
    1+1
    2
    answer -> 2

  -if n == 3: 
    1 + 1 + 1
    1 + 2
    2 + 1
    3
    answer -> 4

  -if n == 4:
    1 + 1 + 1 + 1
    1 + 1 + 2
    1 + 2 + 1
    2 + 1 + 1
    3 + 1
    1 + 3
    2 + 2
    answer -> 7

    if n=4, you can calculate answer 7 by adding the values of the three before n,
    (n-1) + (n-2) + (n-3)

    a cache stores the values for previously calculated amounts(n), to then use and calculate ones after, 
    so the recursion tree doesn't have to keep repeating calculations that have already happened
'''


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    if cache is None:
        cache = [0] * (n + 1)
    if n <= 1:
        cache[n] = 1
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]


eating_cookies(5)
print(eating_cookies(20))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
