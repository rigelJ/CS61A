# UCB-CS61A-SU19
经过一个多月的奋战，终于结束了CS61A的学习，整个学习过程还算是比较平缓，没有遇到什么特别困难地方，Lab和Hw除了Final懒得写了，还有SQL的lab没做，其他都完成了，包括四个大项目。（马虎的我可能偶尔没存档，所以可能有些题空的）

一个多月的时间，一大半都是在整理博客和书写教程，以及看了《两周实现脚本语言》这本书，真正用来刷题和听课的时间并不多。推荐有Python基础的朋友25天左右完成，0基础的朋友45-60天完成，集中精力攻克难题。

我觉得国外课程最好的一点就是具有极强的发散性思维，在不断引导你去探索未知的领域，学习学习，其本质的内驱动力还是兴趣，如果没兴趣去探索，那么计算机学习真的是很困难。

这门课最牛的地方是改变了你的思考方式，看之前你是这样写程序的

```python

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
```

看完之后，你发现你开始这样写程序

```scheme
(define (uncompress s)
    (if (null? s)
        nil
        (my-append (replicate (car(car s)) (car(cdr (car s)))) (uncompress (cdr s)))
```

这样写程序

```python
def replace_leaf(t, old, new):
    if is_leaf(t):
        if label(t)==old:
            return tree(new)
        else:
            return tree(label(t))
    else:
        return tree(label(t),[replace_leaf(b,old,new) for b in branches(t)])
```

甚至这样写程序

```scheme
(define (sub-all s olds news)
  (define (zip xs ys)
   (if (or (null? xs) (null? ys))
     nil
     (cons
       (list (car xs) (car ys))
       (zip (cdr xs) (cdr ys)))))
  (define zips
    (zip olds news))
  (define (action s zip_olds_news)
    (if (null? zip_olds_news)
	s
	(action (substitute s (car(car(zip_olds_news))) (cdr(car(zip_olds_news)))) (cdr zip_olds_news))))
  (action s zips)
```

本书所使用的教材是经典的SICP，即计算机程序的构造与解释，原书所使用的语言是Lisp，而课程使用了更加广泛应用的python，降低了学习的门槛。

![image-20210811191721017](https://i.loli.net/2021/08/11/9CXOZgnys6KIhiD.png)

首先，课程通过讲解函数式编程引入过程抽象思想，介绍了表达式，变量，函数等概念，又从函数框架的层面讲解了函数作用域的概念，最后对函数式编程的几种主要方式进行了介绍，引入了递归调用的概念。

其次课程讲解了数据抽象的概念，从构造器和选择器讲到层次性结构，最后实现了一个基于构造器和生成器的抽象数据类型，树。

而后，课程转入对象抽象，对象抽象是课程中最重要的部分，其直接的表现形式就是面向对象编程，把一组过程抽象（函数）作为类的方法集中考虑，并加入内部状态（类的变量），就是一个数据抽象，每个数据抽象对外通过一组接口进行调用，这样在调用时就不需要考虑函数内部情况，只需要知道函数实现的功能并进行合理调用即可。

最后，课程讲述了语言抽象的过程，主要是讲解如何从零开始构建一门语言，定义这门语言的语法，并实现该语言的解释器或编译器，这一部分涉及编译原理，可能需要对编译原理进行拓展阅读，这其中最让我感觉精妙的就是Frame类和Procedure类的设计，实在让我感受到了编译原理的精妙。

```python
class Frame(object):
    """An environment frame binds Scheme symbols to Scheme values."""

    def __init__(self, parent):
        """An empty frame with parent frame PARENT (which may be None)."""
        self.bindings = {}
        self.parent = parent

    def __repr__(self):
        if self.parent is None:
            return '<Global Frame>'
        s = sorted(['{0}: {1}'.format(k, v) for k, v in self.bindings.items()])
        return '<{{{0}}} -> {1}>'.format(', '.join(s), repr(self.parent))

    def define(self, symbol, value):
        """Define Scheme SYMBOL to have VALUE."""
        # BEGIN PROBLEM 3
        self.bindings[symbol]=value
        # END PROBLEM 3

    def lookup(self, symbol):
        """Return the value bound to SYMBOL. Errors if SYMBOL is not found."""
        # BEGIN PROBLEM 3
        try:
            return self.bindings[symbol]
        except KeyError:
            if self.parent is not None:
                return self.parent.lookup(symbol)
        # END PROBLEM 3
        raise SchemeError('unknown identifier: {0}'.format(symbol))

    def make_child_frame(self, formals, vals):
        """Return a new local frame whose parent is SELF, in which the symbols
        in a Scheme list of formal parameters FORMALS are bound to the Scheme
        values in the Scheme list VALS. Raise an error if too many or too few
        vals are given.

        >>> env = create_global_frame()
        >>> formals, expressions = read_line('(a b c)'), read_line('(1 2 3)')
        >>> env.make_child_frame(formals, expressions)
        <{a: 1, b: 2, c: 3} -> <Global Frame>>
        """
        # BEGIN PROBLEM 11
        match_dict = {}
        if len(formals)!=len(vals):
            raise SchemeError('The number of argument values does not match')
        else:
            for _ in range(len(formals)):
                match_dict[formals.first] = vals.first
                formals = formals.second
                vals = vals.second
        new_frame = Frame(self)
        for key,value in match_dict.items():
            new_frame.define(key,value)
        return new_frame
        # END PROBLEM 11

```

```python
class LambdaProcedure(Procedure):
    """A procedure defined by a lambda expression or a define form."""

    def __init__(self, formals, body, env):
        """A procedure with formal parameter list FORMALS (a Scheme list),
        whose body is the Scheme list BODY, and whose parent environment
        starts with Frame ENV."""
        self.formals = formals
        self.body = body
        self.env = env

    def make_call_frame(self, args, env):
        """Make a frame that binds my formal parameters to ARGS, a Scheme list
        of values, for a lexically-scoped call evaluated in environment ENV."""
        # BEGIN PROBLEM 12
        new_frame = self.env.make_child_frame(self.formals,args)
        return new_frame
        # END PROBLEM 12

    def __str__(self):
        return str(Pair('lambda', Pair(self.formals, self.body)))

    def __repr__(self):
        return 'LambdaProcedure({0}, {1}, {2})'.format(
            repr(self.formals), repr(self.body), repr(self.env))
```

在学习的过程中，我也对四个部分进行了总结和提炼，并且细化了课程中没有讲解透彻的一些概念和思想，供各位学习者参考借鉴，也希望大家能够批评指正，我们共同进步。

[CS61A-过程抽象](Summary/CS61A-过程抽象.md)

[CS61A-数据抽象](Summary/CS61A-数据抽象.md)

[CS61A-对象抽象](Summary/CS61A-对象抽象.md)

[CS61A-元语言抽象](Summary/CS61A-元语言抽象.md)

Thanks！

