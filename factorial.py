import sys
from functools import reduce

def fact(n):
    """
    Factorial function

    :arg n: an integer
    :return" factorial of n
    """
    if n == 0:
        return 1
    return reduce(lambda x, y: x *y, range(1, n+1), 1)

def main(n):
    res = fact(n)
    print(res)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))