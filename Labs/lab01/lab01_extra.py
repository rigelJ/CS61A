"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    mul = 1
    for i in range(k):
        mul = mul*n
        n=n-1
    return mul

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    n = str(n)
    count = 0
    for i in range(len(n)):
        if n[i] =='8':
            if i !=len(n)-1:
                if n[i+1]=='8':
                    return True
            else:
                continue
        else:
            continue
    return False
