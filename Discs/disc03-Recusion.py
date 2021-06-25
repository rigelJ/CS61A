#!/usr/bin/python3

def Mull(m,n):
    """
    >>>Mull(4,3)
    12
    """
    if n==1:
        return m
    else:
        return m+Mull(m,n-1)
'''
 Mull(4,3)==4+4+4
 Mull(4,2)==4+4
 MUll(4,3)==4+Mull(4,2)
 Mul(m,n)==m+Mull(m,n-1)
'''

def is_Prime(x):
    """
    >>> is_Prime(7)
    True
    """
    def is_is(x,n):
        if x==1:
            return True
        elif x%n==0:
            return False and is_is(x-1,n)
        elif x%n!=0:
            return True and is_is(x-1,n)

def make_func_repeater(f,x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def g(n):
        if x==1:
            return f(x)
        else:
            return g(g(n-1))
    return g

'''
f(3) = f(f(f(x)))
f(2) = f(f(x))
f(3) = f(f(2,n))
f(m) = f(f(m-1))
'''

def count_stairs_ways(n):
    """
    >>>count_stairs_ways(4)
    5
    """
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n<0:
        return 0
    else:
        return count_stairs_ways(n-1)+count_stairs_ways(n-2)

'''
stairs(1)= 1

stairs(2)= stair(0)+stairs(1)

stairs(3)=stair(2)+stair(1)

stairs(4)= stair(2)+stair(3)

stairs(n)= stairs(n-1)+stairs(n-2)
'''

def count_k(n,k):
    """
    >>> count_k(3,3)
    4
    """
    if k=1:
        return 
    else:
        return count_stairs_ways(n-k)+count_k(n,k-1)
'''
stairs(1)=1
stairs(0)=1
stairs(n,k)=stairs(n-1)+stairs(n-2)+...+stairs(n-k)
'''
