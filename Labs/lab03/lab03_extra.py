

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def isTF(n,m):
        if m == 1:
            return True
        else:
            if n%m == 0:
                return (False and isTF(n,m-1))
            elif n%m != 0:
                return (True and isTF(n,m-1))
    return isTF(n,n-1)


def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if b==0:
        print(a)
    else:
        return gcd(b,a%b)

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    #ten_pair(n)和ten_pair(n-1)的关系是 
    #如果取 最后一个 数字，那么需要与前面每一个数字都进行对比
    #也就是 n//10 和 n%10 逐个对比
    #这里实际上用了两个递归，一个是用来对比最后一个数字和前面数字组的，一个是用来向前推进计算下一个数字的

    if n<10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10,10-n%10)

def count_digit(n,digit):
    if n ==0:
        return 0
    elif n%10 == digit:
        return count_digit(n//10,digit) + 1
    else:
        return count_digit(n//10,digit)
