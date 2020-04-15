#!/usr/bin/python
import argparse

'''
Spec:
  -accepts a list of prices (integers)
  -find the max profit that can be made 
  -you must "buy" first (cannot buy after selling, duh)


calculate all "profits" that can be made from pairs
will never "buy" the last item (nothing comes after it)

nested loop

'''


def find_max_profit(prices):
    p = prices[1] - prices[0]

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)-1):
            if (prices[j] - prices[i]) > p:
                p = prices[j] - prices[i]

    return p


find_max_profit([100, 90, 80, 50, 20, 10])
print(find_max_profit([1050, 270, 1540, 3800, 2]))

# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
