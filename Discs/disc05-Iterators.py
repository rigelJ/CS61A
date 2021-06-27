#!/usr/bin/python3

def even_weighted(lst):
    return [i*lst[i] for i in range(len(lst)) if i%2==0]

def max_product(lst):
    if lst == []:
        return 1
    elif len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return max(lst)
    else:
        return max(max_product(lst[:-1]),lst[-1]*max_product(lst[:-2]))

#这一题告诉我们找树递归的关系最好还是从后往前找。


def redundant_map(t,f):
    if is_leaf(t):
        return tree(f(label(t)))
    new_label = f(label(t)) 
    new_f = lambda x : f(f(x))
    lst = [redundant_map(b,new_f) for b in branches(t)]
    return tree(new_label,lst)

#这一题告诉我们，如果想对递归中的函数进行嵌套，可以使用匿名函数


def weild_gen(x):
    if x%2 ==0:
        yield x*2
    else:
        yield x
        yield from weild_gen(x-1)

def greeter(x):
    while x%2 != 0:
        print('hello')
        yield x
        print('world')

# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
    


