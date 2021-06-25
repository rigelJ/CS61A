#!/usr/bin/python3

def height(t):
    """
    Return the height of a tree

    >>> t=tree(3,tree(5,[tree(1)]),tree(2))
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 1
    else:
        lsp = []
        for b in branches(t):
            lsp += [1+height(b)]
        return max(lsp)

def square_tree(t):
    if is_leaf(t):
        return tree(lable(t)**2)
    else:
        return tree(label(t)**2,[square_tree(b) for b in branches(t)])

def tree_max(t):
    if is_leaf(t):
        return label(t)
    else:
        lsp =[label(t)]
        for b in branches(t):
            lsp +=[tree_max(b)]
        return max(lsp)

def find_path(tree,x):
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b,x)
        if type(path)==list:
            return [label(tree)] + path

"""
True
6
False
[-1,0,1]
...
"""

def add_this_many(x,el,lst):
    for i in range(x):
        lst.append(el)


def group_by(s,fn):
    # return {i:j for i,j in zip([fn(a) for a in s],s)}
    d = {}
    for i in s:
        if fn(i) not in d:
            d[fn(i)] = [i]
        else:
            d[fn(i)].append(i)
    return d
    
