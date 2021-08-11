---


title: CS61A-数据抽象
date: 2021-06-28 11:25:57
tags:
- 程序结构
- CS61
- CS61A
categories:
- CS61A
---

## CS61A 数据抽象

#### 目录

>数据抽象导引
>
>* 构造器与选择器
>* 序对的表示
>* 抽象屏障与序对的过程性表示
>
>层次性数据和闭包性质
>
>* 序列的表示形式
>* 可变数据与可变函数
>* 层次性结构
>* 迭代器与生成器
>

**带有*号的章节为SICP教材中所涉及的内容，CS61A课程中并未涉及。**

### 数据抽象导引

******************

在课程第一部分过程抽象中，我们通过将一些过程组合起来形成复合过程，并以这种方式构造起各种抽象，然而第一章里的所有过程，操作的都是较为简单的数据，而对于许多问题而言，简单的数据无法满足需求，于是我们引入了数据抽象的概念。

**数据抽象就是指将数据对象组合起来，构成复合数据的形式。**

这是什么意思呢，我们从一个问题来引入，这个例子来自SICP教材，只不过SICP教材中所使用的是scheme语言，结构较为繁琐，因此我们使用Python语言代替来讲解。假设我们要设计一个系统，这个系统能够完成对于有理数的运算，从基本数据出发，一个有理数可以由两个整数来表示，那么如果我们要对两个有理数进行加法，那么我们就要向加法函数中同时传入两个分母和两个分子，即

```python
def adder_without(a,b,c,d):
    return (ad+bc)//bd

如果我们要计算1/3+4/5，那么我们就得这样传入参数

>>adder_without(1,3,4,5)
17/15
```

我们会发现，这样很麻烦，在进行函数过程设计的时候，很容易就忘了a，b，c，d分别是什么，所以我们思考，能不能将一个分子与一个分母粘在一起，形成一个复合结构c和d，那么只需要在参数中传入c和d即可，这样就解决了传参的问题。

但是还有一个 问题，在函数设计过程中，我们也 需要对复合结构中的内容进行提取后使用，那么又该如何提取复合结构数据中的数据呢？

答案就是构建构造函数与选择函数。

#### 构造器与选择器

接着上面的问题，我们首先要将分子与分母放入一个复合结构，实现这个过程的函数叫做构造函数，具体实现如下：

```python
def build(up,down)：
    return [up,down]

于是我们可以利用分子分母构建有理数a和b

a = build(1,3)
b = build(4/5)

```

这个过程也可以使用scheme语言，具体语法不懂的可以看SICP教材。

```scheme
(define (build up down) (cons up down)
```

而后我们要能够将分子分母再从中提取出来，实现这个过程的函数叫做选择函数，Python叫选择器，具体实现如下：

```python
def get_up(x):
    return x[0]
def get_down(x):
    return x[1]

于是我们就可以使用以上两个函数提取数据

a_up = get_up(a)
b_down = get_down(b)

```

利用构造器与选择器重写加法函数

```python
def add(a,b):
    return (get_up(a)*get_down(b)+get_up(b)*get_down(a))/get_down(a)*get_down(b)

使用构造函数
a = build(1,3)
b = build(4,5)

new = add(a,b)
```

这样看起来是不是就清晰多了，这就是构造器和选择器搭配使用的优势，利用这个思路，我们还可以建立`sub`,`mul`,`pow`等运算函数。

#### 序对的表示

其实在上面我们已经在使用序对了，一个序对就是一个复合结构，不同的语言有不同的结构表示方式，Python中序对和序列界限其实很模糊，序对在Python中有字典Dict，元组Tuple，以及上面使用过的列表List：

```python
a = [1,2,3,4]   List
b = (1,2,3,4)   Tuple
c = {'a':1,'b':2} Dict

Python中万物皆对象，所以提取数据的方式非常简单
a[1]
b[1]
c['a']
```

在scheme语言中，序对表示为cons，但是cons只能有两个数据：

```scheme
(define x (cons 1 2)   #相当于x = [1,2],但是scheme没有python高级，实现序列需要cons函数
  
使用 car 和 cdr 提取数据
(car x)
(cdr x)
  
```

#### 抽象屏障与序对的过程性表示

抽象屏障隔离了系统的不同层次，在每一层上这种屏障都把使用数据抽象的程序和实现数据抽象的程序隔离开来，以有理数运算为例，对实现的过程进行分层：

```  
最高层： 使用有理数运算函数的过程

第一层： 有理数运算函数 add() sub() mul() 

第二层： 有理数的构造函数和生成函数 build() get_up() get_down(）
                                             
第三层： 作为序对的有理数 cons() car()  cdr()  /list[]  tuple[]
```

这种构造思想最大的优点就是可修改性好，如果想要对程序的执行结构进行修改，可以直接对相应层中的函数进行修改，上层函数也会因此改变。

例如，我们想将输出的有理数约分到最简的形式，就可以在第二层中对有理数的构造函数build进行修改：

```python
def build(up,down): 
    g = gcd(up,down)
    return [up/g,down/g]
```

这样就完成了约分有理数的过程。

一般而言，我们总可以将复合数据定义为一组适当的选择函数和构造函数，以及使得这些过程成为一套合法表示，这一观点不仅可以服务于高层数据对象，同样也可以用于低层的数据对象，比如scheme语言中的序对这个概念，我们在前面用序对定义有理数，而cons，car和cdr也是函数，只要是函数就一定还能解释单个过程，那么cons函数会由哪些过程构成呢？

````scheme
(define (cons x y))
  (define (dispatch m))
    (cond (= m 0) x)
    (cond (= m 1) y)
    (else (error))
    dispatch)
(define (car z) (z 0))
(define (cdr z) (z 1))
````

由此我们可以看出，序对的概念实际上也可以解释为，由`(cons x y)`返回的值是一个选择过程，并根据参数是0还是1，返回x和y，虽然scheme语言并非这样来定义序对的，但是这也说明了所有数据都可以被定义为一组适当的选择器和构造器。

SICP教材中有一道题目很有意思，既然我们知道所有的复合数据都可以被定义为一组适当的构造函数和选择函数，那么对于基础数据呢？基础数据是不是也能由构造函数和选择函数定义？

答案是可以，这一表示形式被称为Church计数，其名字来源于发明人Alonzo Church，在SICP中使用scheme实现Church计数太过复杂，CS61A毕竟是入门课，所以使用Python来实现这个过程，首先我们实现构造函数：

```python
def zero(f):
    return lambda x:x

def one(f):
    return lambda x:f(x)

def two(f):
    return lambda x:f(f(x))

```

使用匿名函数嵌套的方式去定义构造函数，但是这样定义很累，所以我们思考用一个类似迭代的方式去实现，我们发现，实际上`one(f) = return lambda x:f(x) = return lambda x:f(zero(f)(x) `),把这个结构抽象出来就得到：

```python
我们要实现 two = successor(one)
所以 two = lambda f:lambda x:f(one(f)(x))
令one = n 则有

def successor(n):
    return lambda f:lambda x:f(n(f)(x))

```

选择器要实现的过程就是将构造的zero转变为0，将one转变为1，我们使用选择器函数：

```
def church_to_int(n):
    return n(lambda x:x+1)(0)

这个函数的意思是令初始值x为0,然后按照构造函数的嵌套层数对x嵌套执行匿名函数，此处的匿名函数为add_one,同时也可以另其为add_ten等等，那么zero对应的就是0,one对应10

>>>church_to_int(one)
1
>>>church_to_int(three)
3
```

同样也可以对church对象进行加法运算

```python
def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    #church_to_int() if return 5 then five return five(f)
    #so we have to make add_church(two,three) like five(f)
    #five(f) return lambda x:f(f(f(f(f(x)))))  
    return lambda f: lambda x: n(f)(x) +m(f)(x)

```

SICP中有church计数的scheme实现过程，大体类似。

### 层次性数据和闭包性质

我们可以建立元素本身也是序对/序列的序列，我们把语言的这种性质叫做闭包性质，通过复合数据的闭包性质，可以实现复合结构的再复合。

#### 序列的表示形式

在scheme语言中，序列需要由基本的序对构成，通过嵌套的cons形成的序列称为一个表，Scheme为方便表的构造，引入了一个基本操作list，使用list可以实现序对嵌套形成的序列，具体实现过程如下：

```scheme
(cons 1 
   (cons 2 
       (cons 3 nil)))

or

list(1,2,3)

def lists (list(1,2,3)):
```

通过上面的方式构建起`lists`这个表对象，而后使用cdr和car对表对象包含的数据进行调用

```scheme
(car lists)
1
(cdr lists)
(2,3)
(car(cdr lists))
2
```

我们也可以构建函数返回表中的第n个项：

```scheme
(define (list-n list n))
(if (= n 0)
      (car list)
      (list-n (cdr items) (- n 1))

于是对lists对象使用
    
(list-n lists 2)
2
```

scheme实现表操作的方式很麻烦，需要构建函数，需要自己设计过程，而Python生成序列的方式就明显高级很多了：

```python
同样的过程只需要

lists = [1,2,3]

调用返回第n项也只需要

a = lists[1]

>>>a
2
```

而且python还可以生成字典，元组等序列，序列之间也可以直接嵌套：

```python
lists1 = [1,2,3,[2,3,[1,1]]]
```



#### 可变数据与可变函数

由于scheme对于序列的聚合太过繁杂，故我们直接使用python进行序列操作的介绍，对于python来说，序列聚合有很多种方式，也有很多函数可以进行操作：

```python
sum([1,2,3],<stat>)
add(1,2,3)
min(1,2,3,key=)
all()
any()
bool()
```

以上都是对python的序列进行聚合的方式，还有很多就不赘述了，有需要可以参考Roonob网站教程。那么，当我们需要修改一个序列的时候，我们该怎么实现呢？这就涉及可变性的问题了，python的序列当中，列表和字典属于**可变序列**，而字符串和元组属于不可变序列，那么什么是可变呢？可变就是能够任意修改序列的内容，比如，我们要在序列后加入‘a’这个元素：

```python
可变序列：
[1,2,3].append('a')   
dicts['a'] = 'a'
不可变序列
'abc'.append('a')    Error
(1,2,4).append('a')   Error
```

具有可变性的序列可以直接使用内置函数直接修改序列本身，而不需要返回值来传递，这个在函数作用下效果明显，假设我们有一个列表`list1 = [1,2,3,4]`：

```python
def func(x):
    list1.append(x)
    list1.append(x)

执行func(3)后list1会改变吗？

<<<func(3)
<<<list1
[1,2,3,3,3]

会改变，因为列表具有可变性，调用append内置函数后，列表自动修改。
```

有时候我们不仅需要可变序列，我们还需要可变函数，比如我们往银行存了100块钱，我们要每次从银行中取出20元，如果我们不使用可变函数我们就必须：

```python
def get_money(my_money):
     my_money -=20
     return my_money

>>>my_money = 100
>>>my_money = get_money(20)
>>>my_money = get_money(20)
>>>my_money
60
```

我们会发现这种方式很麻烦，因为要不断返回和重新赋值给`my_money`变量，有没有一种方法，使得不用返回值就能直接得出剩余钱数呢？

有的，那就是**可变函数**。

```python
def make_draw(balance):
    def with_draw(acount):
        nonlocal balance
        if acount > balance
            return "error"
        else:
            balance = balance - acount
            return balance
    return with_draw

这样我们就可以实现

>>>with_draw = make_draw(100)
>>>with_draw(20)
80
>>>with_draw(20)
60

```

这里出现了一个新的类型`nonlocal`，意思是非本地，也就是说，定义为`nonlocal`的变量会直接去父框架寻找变量，并且所有的变量更改直接同步父框架，基于这个性质 `nonlocal`必须满足以下几个条件才能使用：

>1.nonlocal 声明的变量必须存在于父框架
>
>2.nonlocal 声明的变量不能在本地变量已经绑定值后再声明，这样python无法判断该变量的位置。

我们知道，框架中可以直接调用和修改父框架内的值，那么为什么还要使用nonlocal来声明？

答案就是，python在进行运行前就已经对变量进行了判断，是位于本框架还是父框架，如果没有对变量进行nonlocal声明，python就会基于`balance=balance-accont`这个表达式判断balance是本地变量，而后在`if account > balance`中报错。（讲的有些不太清楚，这里其实我也有点没理解透，后面再翻书查查。）

有没有办法能够不使用nonlocal进行可变函数的使用，有的，那就是改绑定值为修改值，利用序列的性质，具体实现如下：

```python
def make_draw(balance):
    b= []
    b[0] = balance
    def with_draw(acount):
        nonlocal balance
        if acount > balance
            return "error"
        else:
            b[0] = b[0] - acount
            return b[0]
    return with_draw

这样我们就可以实现

>>>with_draw = make_draw(100)
>>>with_draw(20)
80
>>>with_draw(20)
60

```

这样，减少值的过程就变成了修改序列第一位的值，而非修改balance变量的绑定，也就不会报错。



#### 层次性结构

序列按照层次性结构相互组合就会形成具有层次性的序列，最典型的层次性结构序列就是树，我们知道复合结构都可以用构造器和选择器定义，下面给出树的定义：

```python
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree
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

```

以上是树的定义，树每个的节点都由标签label和分支branch组成，没有分支的节点称为树叶节点，这种数据组织的方式，可以很清晰的看清上下层次的关系，可以用于解决很多实际问题，比如斐波纳契数列。

递归是处理树结构问题的一种常用方式，由于树的每一个分支都是子树或树叶，因此很容易实现自上而下的递归，以base_case作为终止条件。

我们来看几个关于树结构的问题

```python
问题一：替换具有指定数据的树节点

def replace_leaf(t, old, new):
    """Returns a new tree where every leaf value equal to old has
    been replaced with new.

    >>> yggdrasil = tree('odin',
    ...                  [tree('balder',
    ...                        [tree('thor'),
    ...                         tree('freya')]),
    ...                   tree('frigg',
    ...                        [tree('thor')]),
    ...                   tree('thor',
    ...                        [tree('sif'),
    ...                         tree('thor')]),
    ...                   tree('thor')])
    >>> laerad = copy_tree(yggdrasil) # copy yggdrasil for testing purposes
    >>> print_tree(replace_leaf(yggdrasil, 'thor', 'freya'))
    odin
      balder
        freya
        freya
      frigg
        freya
      thor
        sif
        freya
      freya
    >>> laerad == yggdrasil # Make sure original tree is unmodified
    True
    """
    if is_leaf(t):
        if label(t)==old:
            return tree(new)
        else:
            return tree(label(t))
    else:
        return tree(label(t),[replace_leaf(b,old,new) for b in branches(t)])

可以看出，通过递归的方式可以对树的每个节点进行遍历，而后替换制定标签的数值
```

```python
问题二：在每个叶节点上插入新子树

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
        return tree(label(t),[tree(s) for s in vals ])
    else:
        '''
        lsb = []
        for b in branches(t):
            lsb += sprout_leaves(b,vals)
        return [tree(label(t),lsb)]
        '''
        return tree(label(t),[sprout_leaves(b,vals) for b in branches(t)])
```

下一个问题比较麻烦，实现过程也比较复杂，基本上囊括了递归的所有知识，如果能够独立完成，基本上对于树的概念和递归的概念已经理解较深了。

```python
问题三：对应树的相加

def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
    if is_leaf(t1) and is_leaf(t2):
        return(tree(label(t1)+label(t2)))
    elif is_leaf(t1):
        return tree((label(t1)+label(t2)),branches(t2))
    elif is_leaf(t2):
        return tree((label(t1)+label(t2)),branches(t1))
    else:
        lsp = []
        node = label(t1)+label(t2)
        zips = list(zip(branches(t1),branches(t2)))
        if len(zips) == len(branches(t1)):
            for b in zips:
                lsp += [add_trees(b[0],b[1])]
            lsp +=branches(t2)[len(zips):]
            return tree(node,lsp)
        if len(zips) == len(branches(t2)):
            for b in zips:
                lsp += [add_trees(b[0],b[1])]
            lsp +=branches(t1)[len(zips):]
            return tree(node,lsp)

```

这里所用到的zip函数请自行查阅python指南，解答过程如上。

#### 迭代器与生成器

Python和许多其他编程语言提供了一种统一的方式来顺序处理容器值的元素，称为迭代器，一个迭代器是提供对值顺序访问。

迭代器对象由两个部分组成，一个是迭代值iterable，另一个是迭代器iterator，迭代值提供迭代器顺序迭代的范围，迭代器提供一个检索对象。

````python
prime = [1,2,3,4]   迭代值
iters = iter(prime)  迭代器
````

利用迭代器的next方法来获取迭代器对象所指位置的数据，而后将指针后移一位

```python
>>>next(iters)
1
>>>next(iters)
2
>>>next(iters)
3
>>>next(iters)
4
>>>next(iters)
StopIteration 
```

当到达处理序列末尾后再次调用`next`方法将会引发StopIteration异常，说明序列已经迭代完毕。

两个独立的迭代器可以跟踪同一序列的两个不同位置，同一迭代器赋值给另一变量，两个变量名称共享一个位置。

```python
>>> r  =  range ( 3 ,  13 ) 
>>> s  =  iter ( r )   # 第一个迭代器s
>>> next ( s ) 
3 
>>> next ( s ) 
4 
>>> t  =  iter ( r )   # 第二个迭代器t 
>>> next ( t ) 
3 
>>> next ( t ) 
4 
>>> u  =  iter(t)  # 第二个迭代器的替代名称
>>> next ( u ) 
5 
>>> next ( u ) 
6
```

这里有一个利用迭代器计算斐波纳契数列的实例。

````python
def fib_iter(n):
    prev,curr=0,1
    list = [prev,curr]
    index = 2
    while index < n:
        prev,curr = curr,prev+curr
        list +=[curr]
        index ++
    return iter(list)
````

使用如上的迭代器对象，可以轻松完成简单序列的迭代，然而，对于复杂的序列，next方法很难在计算中保存位置，生成器允许我们利用Python的特性来定义更复杂的迭代。

生成器函数与常规函数的区别在于，它们的主体中不包含return语句，而是使用yeild返回系列的元素

生成器不使用对象的属性来跟踪它们在一系列中的进度，相反，它们控制生成器函数的执行，该函数一直运行得到每次调用生成器的next方法时执行下一个yeild语句。

```python
def letters_generator():
    current = 'a'
    while current <='d':
        yield current
        current =chr(ord(current)+1)

>>>letters = letters_generator()
>>>next(letters)
a
```

再复杂一点可以这样使用生成器：

```python
def natural():
    x=0
    while True:
        yield x
        x+1
>>>ns1,ns2=natural(),natural()
>>>[next(ns1)*next(ns2) for _ in range(5)]
[0,1,4,9,16]
```