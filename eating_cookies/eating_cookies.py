#!/usr/bin/python

import sys
'''
Spec: 
  -can eat 0, 1, 2, or 3 cookies 
  -how many combinations can be made to make up n
  -if n == 3: 
    1 & 1 & 1
    1 & 2
    2 & 1
    3
'''


# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    # base case
    if n <= 1:
        return 1
    elif n == 2:
        return 2

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


eating_cookies(5)
print(eating_cookies(5))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')
