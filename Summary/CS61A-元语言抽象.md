---
title: CS61A-元语言抽象
date: 2021-08-08 15:56:30
tags:
- 程序结构
- CS61
- CS61A
categories:
- CS61A

---

## CS61A 元语言抽象

#### 目录

> Scheme语言
>
> * 表达式
> * 控制结构与列表
> * 定义变量与函数
> * 匿名过程
>
> Scheme语言特性
>
> * 宏
> * 流
>
> 抽象语言的解释器
>
> * 解释器的实现
> * 读取过程
> * 评估过程
> * 输出过程
>

在之前的章节中，我们都是基于一门语言去研究程序的抽象形式，而本 书的最后一个部分直接跳出了语言，讲解一门语言是怎么样抽象的，也就是说，这一章，是在教你如何实现一门语言，我们这里所说的语言是脚本语言，接下来，我们就要以Scheme语言为例，讲解Scheme语言是怎么样一步一步构造出来的。

### Scheme语言

首先我们从使用者的角度了解一下Scheme的语法。

#### 表达式

最基础的表达式可以是数字，布尔值或者符号，这里的符号是我们在Python语言中唯一没有遇到的类型，具体来说，Scheme中的符号也是一种值。

##### 原子表达式

```scheme
scm> 1234    ; integer
1234
scm> 123.4   ; real number
123.4
```

##### 布尔值

```scheme
scm> #t
#t
scm> #f
#f
```

在 Scheme 中，除了特殊的布尔值#f之外的所有值都被解释为真值（与 Python 不同，Python 中有一些像0那样的假值）

##### 符号

其中，符号类型是我们在 Python 中唯一没有遇到的类型。一个 符号的作用很像一个Python的名字，但不完全是。具体来说，Scheme 中的符号也是一种值。在 Python 中，名称仅用作表达式；Python 表达式永远不能计算为名称。

这个过程具体是怎么实现的，我们后面再讲。

```scheme
scm> quotient      ; A name bound to a built-in procedure
#[quotient]
scm> 'quotient     ; An expression that evaluates to a symbol
quotient
scm> 'hello-world!
hello-world!
```

#### 调用表达式

与 Python 一样，Scheme 调用表达式中的运算符位于所有操作数之前。与 Python 不同的是，运算符包含在括号内，并且操作数由空格而不是逗号分隔。然而，Scheme 调用表达式的计算遵循与 Python 完全相同的规则：

1.评估操作符，应该评估为一个过程

2.从左到右评估操作数

3.操作数应用于过程

以下是一些使用内置过程的示例：

```scheme
scm> (+ 1 2)
3
scm> (- 10 (/ 6 2))
7
scm> (modulo 35 4)
3
scm> (even? (quotient 45 2))
#t
```

#### 控制结构与列表

##### if表达式

该if特殊形式使我们能够评估基于谓词两个表达式之一。它接受两个必需的参数和一个可选的第三个参数：

> (if <predicate> <if-true> [if-false])

第一个操作数是Scheme 中所谓的谓词表达式，该表达式的值被解释为#tor 或#f。

计算if特殊形式表达式的规则如下：

1.评估<predicate>。
2.如果<predicate>评估为真值，则评估并返回该值，如果表达式<if-true>. 否则，[if-false]如果提供，则评估并返回值 。

```scheme
scm> (if (> x 3)
         1
         2)
```

在 Scheme 中，您不能编写elif案例。如果要使用if表达式有多个案例，则需要多个分支if表达式：

```scheme
scm> (if (< x 0)
         'negative
         (if (= x 0)
             'zero
             'positive
         )
 )
```

##### cond表达式

使用嵌套if表达式似乎不是处理多种情况的非常实用的方法。相反，我们可以使用cond特殊形式，一种类似于 Python 中的多子句 if/elif/else 条件表达式的通用条件表达式。

```scheme
(cond
    (<p1> <e1>)
    (<p2> <e2>)
    ...
    (<pn> <en>)
    [(else <else-expression>)])
```

评价规则如下：

1.对谓词<p1>, <p2>, ...,<pn>进行求值，直到达到求值为真 y 值的谓词为止。
2.如果您到达一个计算结果为真值的谓词，请计算并返回子句中的相应表达式。
3.如果没有一个谓词是真y并且有一个else子句，则评估并返回<else-expression>。

```scheme
scm> (cond
        ((> x 0) 'positive)
        ((< x 0) 'negative)
        (else 'zero))
```

##### 列表

###### cons

Scheme 列表与我们在 Python 中使用的链表非常相似。就像链表是由一系列Link 对象构建的一样，Scheme 列表是由一系列对构建的，这些对是由构造函数创建的cons，是一种可递归对象。

Scheme列表要cdr是另一个列表或nil空列表。列表在解释器中显示为值序列（类似于对象的 __str__表示Link）。

```scheme
scm> (cons 1 (cons 2 (cons 3 nil)))
(1 2 3)
```

具体的实现方式用图像来表示就是

![image-20210810094539083](https://i.loli.net/2021/08/10/Le2kpYIwaAgWN8E.png)

我们可以使用car和cdr从我们的列表中检索值，现在它的工作方式类似于 PythonLink的first和rest属性。

````scheme
scm> (define a (cons 1 (cons 2 (cons 3 nil))))  ; Assign the list to the name a
scm> a
(1 2 3)
scm> (car a)
1
scm> (cdr a)
(2 3)
scm> (car (cdr (cdr a)))
3
````

如果您没有将 pair 或 nil 作为第二个参数传递给cons，则会出错：

```scheme
scm> (cons 1 2)
Error
```

###### List

另一种创建列表的方式是利用list，该list过程接受任意数量的参数并使用这些参数的值构造一个列表

```scheme
scm> (list 1 2 3)
(1 2 3)
scm> (list 1 (list 2 3) 4)
(1 (2 3) 4)
scm> (list (cons 1 (cons 2 nil)) 3 4)
((1 2) 3 4)
```

请注意，此表达式中的所有操作数在放入结果列表之前都会进行评估。

###### Quote

我们还可以使用引用形式来创建一个列表，通过引用形式创建的列表不进评估

```scheme
scm> '(1 2 3)
(1 2 3)
scm> '(cons 1 2)           ; Argument to quote is not evaluated
(cons 1 2)
scm> '(1 (2 3 4))
(1 (2 3 4))
```

#### 定义变量与函数

在Python中定义变量使用=号进行，而定义变量使用def进行，而在Scheme中定义变量和过程都使用define语法，这个在后期解释器的构造中我也会着重细讲。

定义变量，我们使用语法

```scheme
(define <name> <expression>)
```

评估这个表达式的规则是

1.评估<expression>.
2.将其值绑定到<name>当前Frame中。
3.返回<name>。

定义过程，我们使用语法

```scheme
(define (<name> <param1> <param2> ...) <body> )
```

要评估此表达式：

1.使用给定的参数和 来创建一个 lambda 过程<body>。
2.将过程绑定到<name>当前帧中的 。
3.返回<name>。

以下两个表达式是等价的：

```scheme
scm> (define foo (lambda (x y) (+ x y)))
foo
scm> (define (foo x y) (+ x y))
foo
```

#### 匿名过程

所有 Scheme 过程都是 lambda 过程。要创建 lambda 过程，我们可以使用lambda特殊形式

```scheme
(lambda (<param1> <param2> ...) <body>)
```

```scheme
scm> (lambda (x y) (+ x y))        ; Returns a lambda function, but doesn't assign it to a name
(lambda (x y) (+ x y))
scm> ((lambda (x y) (+ x y)) 3 4)  ; Create and call a lambda function in one line
7
```

一个过程可以接受任意数量的参数。该<body>可以包含多个表达式。return Scheme 中没有 Python语句的等效版本。该函数将简单地返回正文中最后一个表达式的值。

### Scheme语言特性

#### 宏

##### Define-macro

宏是一个不好理解的概念，但是却是一个非常重要的概念，我们刚才已经介绍了define的用法，下面我们使用define来定义一个过程

```scheme
(define twice(f)
  (begin f f))
```

当我们输入`（twice （print 'woof））`我们希望能输出两次woof，然而

```scheme
scm> (twice (print 'woof))
woof
```

这是怎么回事呢？

我们一步一步来，首先我们对操作符twice进行评估，返回我们定义的twice过程，而后我们对`(print 'woof)`进行评估，打印woof，而后将返回的undefined值绑定到f，而后将操作数字应用于操作符，得到表达式`（begin undefined undefined）`对该表达式进行评估，无返回值

那么我们该怎么样修改才能得到正确输出呢？

我们想要最终评估的表达式是这样的，`begin （print 'woof）(print 'woof)` ，因此，我们想到一种办法

```scheme
(define (twice f)
  (eval (list 'begin f f))
```

为了保证最终评估的表达式是`begin （print 'woof）(print 'woof)` ，我们稍微改变了一下输入的值

```scheme
scm> (twice '(print 'woof))
woof
woof
```

这样我们就通过eval list返回的列表，完成了正确输出。

但是肯定有人会想，为什么要这么麻烦，在进入函数的时候用‘防止被eval，结果在出来的时候又得加个eval，那索性就直接让操作数不评估不就行了。

诶，没错，这个问题，前人已经考虑到了，而且他们还设计了一种语法来解决这个问题，这种语法被叫做macro，宏。

```scheme
scm> (define-macro (twice f) (list 'begin f f))
twice
scm> (twice (print 'woof))
woof
woof
```

define-macro允许我们定义macro，这是我们将未计算的输入表达式组合到另一个表达式中的一种方式。当我们调用宏时，操作数不会被评估，而是被视为 Scheme 数据。这意味着任何作为调用表达式或特殊形式表达式的操作数都被视为列表。

在我们的例子中，我们需要一个如下所示的begin 表达式

```scheme
(begin (print 'woof) (print 'woof))
```

作为 Scheme 数据，这个表达式实际上只是一个包含三个元素的列表：begin和(print 'woof)两次，这正是(list 'begin f f)返回的内容。现在，当我们调用 时twice，这个列表被评估为一个表达式并被(print 'woof)评估两次。

回顾一下，宏的调用方式与常规过程类似，但评估它们的规则不同。我们通过以下方式评估了 lambda 过程：

>1.评估运算符
>2.评估操作数
>3.将运算符应用于操作数，评估过程的主体

但是，评估对宏过程调用的规则是：

>1.评估运算符
>2.将运算符应用于未计算的操作数
>3.评估宏在调用它的框架中返回的表达式。

这种特性使得scheme语言具有很强的扩展性，可以随意设计各种不同的语法来进行运算，举个例子，如果我们想把Scheme的定义语法用Python的风格写出来，该怎么做呢？

这时候我们就可以利用宏来实现。

```scheme
(define-macro (def func bindings body)
    (list 'define (cons func bindings) body))
```

```scheme
scm< (def f(x y) (+ x y))
f
```

这样我们就可以使用具有Python风格的语法来定义scheme函数了。

##### Quasiquote

回想一下，quote特殊形式会阻止 Scheme 解释器执行表达式,如果我们试图构建具有许多嵌套列表的复杂 Scheme 表达式，这种形式似乎会派上用场。

考虑我们将twice宏重写如下

```scheme
(define-macro (twice f)
  '(begin f f))
```

这似乎会产生相同的效果，但由于quote 表单阻止了任何评估，我们创建的结果表达式实际上是`(begin f f)`，这不是我们想要的。

乍一看，quasiquote（可以用反引号`或quasiquote特殊形式调用）与quote的行为完全相同。但是，使用quasiquote可以使用逗号，从引用的上下文中删除一个表达式，对其进行评估，然后将其放回原处。

下面是我们如何使用 quasiquote 来重写我们之前的示例：

```scheme
(define-macro (twice f)
  `(begin ,f ,f))
```

同样我们重写def实例：

```scheme
(define-macro (def func bindings body)
    `(define ,(cons func bindings) ,body))
```

其执行结果不变。

#### 流

在Python当中，我们使用迭代器和生成器来实现惰性求值

```python
def ints(first):
    while True:
        yield first
        first += 1
```

```python
>>> s = ints(1)
>>> next(s)
1
>>> next(s)
2
```

然而，在Scheme语言中，没有迭代器和生成器，让我们看看如果我们使用scheme列表来进行循环迭代求值会产生什么情况。

```scheme
(define (ints first)
    (cons first (ints (+ first 1)))
```

```scheme
scm> (ints 1)
maximum recursion depth exceeded
```

由于cons是一个连续求值的过程，在cons结构建立之前，需要对所有值进行逐个评估，因此我们不能用cons创建一个无限循环的列表，然而，scheme解释器引入了流，流是一个特殊的scheme列表，在进行评估时，第一个值会进行评估，而第二个值会被保留，直到我们需要进行评估时才执行，在程序编写范式中，这种模式被称作惰性求值。

我们使用以下语法结构创建一个流

```scheme
(cons-stream <operand1> <operand2>)
```

我们以自然数无限循环列表为例讲解流的操作

```scheme
(define (ints first)
    (cons-stream first
                 (ints (+ first 1)))
```

```scheme
scm> (ints 1)
(1 . #[promise (not forced)])
```

可以看出，流在进行评估的时候，只会评估第一个值，而保留第二个值，而后返回一个列表。

我们首先将循环列表返回的值赋给一个变量a

```scheme
scm>(define a (int 1))
```

而后我们对列表进行操作，如果我们仅使用cdr

```scheme
scm> (cdr (int 1))
#[promise (not forced)]
```

我们发现依然没有评估，因为我们需要使用cdr-stream，才能让列表第二个值评估后返回。

```scheme
scm> (cdr-stream a)
(2 . #[promise (not forced)])
```

这样我们就能得到第二个值评估后的结果。

利用流能做些什么呢？我们举一个例子

假设我们有一个自然数循环列表，我们需要得到一个对每个值都运用函数后返回值构成的循环列表，那么我们该怎么做呢？

```scheme
(define (naturals n)
  (cons-stream n (naturals (+ n 1))))

(define nat (naturals 0))

(define (map-stream f s)
  (cons-stream (f (car s)) (map-stream f (cdr-stream s))))

(define evens (map-stream (lambda (x) (* x 2)) nat))

```

首先，我们创建一个循环列表，并将其赋给变量`nat`，而后我们创建一个`map-stream`函数，引入循环列表和一个匿名函数作为参数，再将返回的列表赋给变量`even`由于cons-stream惰性求值的性质，我们在得到第一个值后并不会继续评估，因此`even`就变成了返回两倍自然数的循环列表，是不是很有趣呢？

以上统统扯淡，看文档都能会，接下来进入正题。

### 抽象语言的解释器

#### 解释器的实现

这是一个非常庞大的项目，CS61A利用Python构建了一个Scheme的解释器，也就是说，当完成这个解释器之后，我们就可以利用自己写的解释器进行scheme文档的解释与输出了，其实所有的编程语言本质都是解释器，你必须要采用合理的解释器将计算机无法理解的语言转换成计算机可以理解的语言，这样才能实现各种功能。

整个解释器分为三个步骤，Read，Eval，Print，我们着重讲解前两个步骤。

单个Read部分，这一步将用户的输入解析为解释器内部的一种抽象数据类型，我们在Python中构建了Pair这个类来将用户的输入从字符串转换成类的实例对象，以便于下一步对输入的整个表达式进行操作，主要有词法分析和句法分析两个步骤。

Eval部分，这一步评估Scheme表达式以获得相应的值，我们知道，对于基础表达式例如 数字，布尔值，符号等来说，只需要对其进行评估后返回即可，而对于有操作符和操作数的调用表达式来说，我们要遵循调用表达式评估的顺序，忘记了？我们再来回顾一遍。

>1.评估操作符，应该评估为一个过程
>
>2.从左到右评估操作数
>
>3.操作数应用于过程

操作符评估后，将会返回相应的过程，如果被求值的表达式是特殊形式，比如if,cond等等，将调用相应的函数进行操作，而后对操作数进行评估，注意，如果操作数也是调用表达式，那么依然要按顺序进行评估后返回。接下来就是将评估后的操作数应用于过程了，这里的过程有两种，一是内置过程，二是我们自己创建的Lambda过程，在后面我们会详细介绍如何分别实现这两种过程的应用。

Print部分，这部分就不细讲了，就是使用str打印获得值即可。

还有一个问题就是，我们需要让整个解释器循环起来，总不能每次输入一次表达式得出结果就终止了程序吧，所以我们需要一个逻辑循环函数。

OK，从Read开始讲起。

#### Read部分

##### Pair类

前面我们讲到，Read部分是将用户输入的字符串，通过词法分析和句法分析转换成某种抽象数据类型，以供后续的分析

首先我们来定义一种能够接收并存储用户输入字符串的数据类型Pair

```python
class Pair(object):
    """A pair has two instance attributes: first and second. Second must be a Pair or nil

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        from scheme_builtins import scheme_valid_cdrp, SchemeError
        if not (second is nil or isinstance(second, Pair) or type(second).__name__ == 'Promise'):
            raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(second))
        self.first = first
        self.second = second

    def __repr__(self):
        return 'Pair({0}, {1})'.format(repr(self.first), repr(self.second))

    def __str__(self):
        s = '(' + repl_str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += ' ' + repl_str(second.first)
            second = second.second
        if second is not nil:
            s += ' . ' + repl_str(second)
        return s + ')'

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError('length attempted on improper list')
        return n

    def __eq__(self, p):
        if not isinstance(p, Pair):
            return False
        return self.first == p.first and self.second == p.second

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError('ill-formed list (cdr is a promise)')
```

我们可以看出，Pair的结构非常像Link，其实本质也是一种迭代对象，只不过在link的基础上增加了一些内置方法，用于对Pair对象进行各种操作。

##### 词法分析

当用户输入一个字符串 

```scheme
scm> (+ 1 2)
```

解释器首先要对其进行词法分析，在该项目中，我们使用tokenize_lines函数和Buffer类进行词法分析，最终返回一个Buffer对象src

```scheme
next_line = buffer_input

src = next_line()
```

根据函数调用的顺序，涉及的函数调用如下：

```python

获取字符串
def buffer_input(prompt='scm> '):
    """Return a Buffer instance containing interactive input."""
    return Buffer(tokenize_lines(InputReader(prompt)))
    
#获取输入字符串，逐个字符传入tokenize_line函数执行    
def tokenize_lines(input):
    """An iterator over lists of tokens, one for each line of the iterable
    input sequence."""
    return (tokenize_line(line) for line in input)

#获取tokenize_line函数执行返回结果构成的列表，并将其转为Buffer类的实例对象
class Buffer(object):
    def __init__(self, source):
        self.index = 0
        self.lines = []
        self.source = source
        self.current_line = ()
        self.current()

    def remove_front(self):
        """Remove the next item from self and return it. If self has
        exhausted its source, returns None."""
        current = self.current()
        self.index += 1
        return current

    def current(self):
        """Return the current element, or None if none exists."""
        while not self.more_on_line:
            self.index = 0
            try:
                self.current_line = next(self.source)
                self.lines.append(self.current_line)
            except StopIteration:
                self.current_line = ()
                return None
        return self.current_line[self.index]

    @property
    def more_on_line(self):
        return self.index < len(self.current_line)

    def __str__(self):
        """Return recently read contents; current element marked with >>."""
        # Format string for right-justified line numbers
        n = len(self.lines)
        msg = '{0:>' + str(math.floor(math.log10(n))+1) + "}: "

        # Up to three previous lines and current line are included in output
        s = ''
        for i in range(max(0, n-4), n-1):
            s += msg.format(i+1) + ' '.join(map(str, self.lines[i])) + '\n'
        s += msg.format(n)
        s += ' '.join(map(str, self.current_line[:self.index]))
        s += ' >> '
        s += ' '.join(map(str, self.current_line[self.index:]))
        return s.strip()
```

Buffer实例有两个核心方法remove_front和current，这两个方法可以对Buffer对象里的值进行有序输出。

```scheme
>>> buf = Buffer(iter([['(', '+'], [15], [12, ')']]))
>>> buf.remove_front()
'('
>>> buf.remove_front()
'+'
>>> buf.current()
15
>>> print(buf)
1: ( +
2:  >> 15
>>> buf.remove_front()
15
```

经过词法分析，用户输入的字符串被转换成了可有序输出的Buffer实例对象，就好像排列在内存中的数据一样，但是有一个问题就在于，对于这些存在实例对象中的数据，数据之间的相互关联并没有建立，就好像在游乐园等待入场的队列，虽然有序，但是相互之间毫无关联。

因此我们要进行句法分析。

##### 句法分析

在该项目中，我们使用scheme_read进行句法分析，最终返回一个Pair对象expression

```scheme
expression = scheme_read(src)
```

我们来看一下scheme_read的逻辑流程

```python
def scheme_read(src):
    """Read the next expression from SRC, a Buffer of tokens.

    >>> scheme_read(Buffer(tokenize_lines(['nil'])))
    nil
    >>> scheme_read(Buffer(tokenize_lines(['1'])))
    1
    >>> scheme_read(Buffer(tokenize_lines(['true'])))
    True
    >>> scheme_read(Buffer(tokenize_lines(['(+ 1 2)'])))
    Pair('+', Pair(1, Pair(2, nil)))
    """
    if src.current() is None:
        raise EOFError
    val = src.remove_front() # Get the first token
    if val == 'nil':
        # BEGIN PROBLEM 2
        return nil
        # END PROBLEM 2
    elif val == '(':
        # BEGIN PROBLEM 2
        return read_tail(src)
        # END PROBLEM 2
    elif val in quotes:
        # BEGIN PROBLEM 7
        return Pair(quotes[val],Pair(scheme_read(src),nil))
        # END PROBLEM 7
    elif val not in DELIMITERS:
        return val
    else:
        raise SyntaxError('unexpected token: {0}'.format(val))

def read_tail(src):
    """Return the remainder of a list in SRC, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    """
    try:
        if src.current() is None:
            raise SyntaxError('unexpected end of file')
        elif src.current() == ')':
            # BEGIN PROBLEM 2
            src.remove_front()
            return nil
            # END PROBLEM 2
        else:
            # BEGIN PROBLEM 2
            return Pair(scheme_read(src),read_tail(src))
            # END PROBLEM 2
    except EOFError:
        raise SyntaxError('unexpected end of file')

quotes = {"'":  'quote',
          '`':  'quasiquote',
          ',':  'unquote'}
        
```

我们可以看出，对于不同的结构，scheme_read有不同的方案去构造，主要可以分为三种，一种是普通的基础表达式，比如123，nil和布尔值，一种是调用表达式，scheme_read函数规定当遇到‘（’时会自动进入read_tail函数，最终返回一个完整的Pair结构，第三种就是符号，函数会判断这个符号是Quote，Quasiquote还是unquote，并将这三个模式传入以供后期评估使用。

最终输入如下

```python
>>> scheme_read(Buffer(tokenize_lines(['(+ 1 2)'])))
Pair('+', Pair(1, Pair(2, nil)))
```

可以看出，经过句法分析，我们建立了字符之间的关联性，同属于一个调用表达式的字符被整合进 了独立的一个Pair实例，就好比，让在排队的人，夫妻合并成一组，家庭或朋友合并成一组，再进行排队。

经过第一部分Read，我们拥有了具有关联性的Pair对象，在接下来的Eval部分中，我们将要对这个对象进行评估。

#### Eval 部分

在整个评估过程中，有两个类发挥着重要作用，一个类是Frame，Frame类是一个环境框架，我们学习Python作用域的时候学习过，程序开始时候是在Global Frame下，当调用函数时候，会创建一个Frame，并且在该Frame下创建的变量和传入的参数是不能在Global Frame下被使用的，Scheme同样如此，所以我们创建了一个Frame类用于分离不同作用域。一个类是Procedure，Procedure类是过程类，他有两个子类，一个是BuiltinProcedure，即内置过程，比如我们使用的if，cons，cond都是内置过程，另一个是LambdaProcedure，即匿名过程，这是用来创建并绑定用户定义过程的。

##### Frame类

EFrame类实现了环境框架，在对解释器进行初始化的时候，会调用create_global_frame创建一个Frame环境框架。

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

Frame框架类从外界引入一个父环境Frame实例，并维护一个binding列表，在初始化时候，会在初始Frame环境中调用define方法引入内置过程，在后面的过程中，如果需要引入用户过程，可以通过define引入，查找内置过程，可以通过lookup方法实现。

```python
def create_global_frame():
    """Initialize and return a single-frame environment with built-in names."""
    env = Frame(None)
    env.define('eval',
               BuiltinProcedure(scheme_eval, True, 'eval'))
    env.define('apply',
               BuiltinProcedure(complete_apply, True, 'apply'))
    env.define('load',
               BuiltinProcedure(scheme_load, True, 'load'))
    env.define('procedure?',
               BuiltinProcedure(scheme_procedurep, False, 'procedure?'))
    env.define('map',
               BuiltinProcedure(scheme_map, True, 'map'))
    env.define('filter',
               BuiltinProcedure(scheme_filter, True, 'filter'))
    env.define('reduce',
               BuiltinProcedure(scheme_reduce, True, 'reduce'))
    env.define('undefined', None)
    add_builtins(env, BUILTINS)
    return env
```

当子环境创建需要引入一个Frame实例时，Frame可以调用make_child_frame创建一个子Frame并返回。

```python
def make_call_frame(self,args,env):
        return env.make_child_frame(self.formals, args)
```

##### Procedure类

```python
class BuiltinProcedure(Procedure):
    """A Scheme procedure defined as a Python function."""

    def __init__(self, fn, use_env=False, name='builtin'):
        self.name = name
        self.fn = fn
        self.use_env = use_env

    def __str__(self):
        return '#[{0}]'.format(self.name)

    def apply(self, args, env):
        """Apply SELF to ARGS in ENV, where ARGS is a Scheme list.

        >>> env = create_global_frame()
        >>> plus = env.bindings['+']
        >>> twos = Pair(2, Pair(2, nil))
        >>> plus.apply(twos, env)
        4
        """
        if not scheme_listp(args):
            raise SchemeError('arguments are not in a list: {0}'.format(args))
        # Convert a Scheme list to a Python list
        python_args = []
        while args is not nil:
            python_args.append(args.first)
            args = args.second
        # BEGIN PROBLEM 4
        if self.use_env:
            python_args.append(env)
        try:
            return self.fn(*python_args)
        except TypeError:
            raise SchemeError("Invalid number of arguments to {0}".format(self.name))
        # END PROBLEM 4

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

内置过程表示为BuiltinProcedure实例，BuiltinProcedure具有两个实例属性，fn是实施内置方案程序的Python功能，use_env是一个布尔标志，指示这个内置程序是否会期望当前环境作为最后一个参数传递。例如，需要环境来实施内置eval程序。

用户定义的程序表示为LambdaProcedure实例。LambdaProcedure具有三个实例属性，formals是命名程序参数的正式参数（符号）的方案列表。body是一个方案列表的表达式，程序的主体。
env是定义程序的Frame环境。

##### 评估仅内置过程的表达式

当我们评估只有内置过程的表达式的时候，我们会进行这个过程

```python
if scheme_symbolp(first) and first in SPECIAL_FORMS:
        return SPECIAL_FORMS[first](rest, env)
```

这里的SPECIAL_FORMS就是内置过程的列表，我们通过first变量传入操作符名称，当我们发现评估的操作符是个内置过程的时候，我们就会调用这段代码找到对应调用内置过程的函数。

```python
SPECIAL_FORMS = {
    'and': do_and_form,
    'begin': do_begin_form,
    'cond': do_cond_form,
    'define': do_define_form,
    'if': do_if_form,
    'lambda': do_lambda_form,
    'let': do_let_form,
    'or': do_or_form,
    'quote': do_quote_form,
    'define-macro': do_define_macro,
    'quasiquote': do_quasiquote_form,
    'unquote': do_unquote,
}
```

我们以评估define内置过程为例来讲解。

```python
def do_define_form(expressions, env):
    """Evaluate a define form."""
    check_form(expressions, 2)
    target = expressions.first
    if scheme_symbolp(target):
        check_form(expressions, 2, 2)
        # BEGIN PROBLEM 6
        value = scheme_eval(expressions.second.first,env)
        env.define(target,value)
        return target
        # END PROBLEM 6
    ...
    else:
        bad_target = target.first if isinstance(target, Pair) else target
        raise SchemeError('non-symbol: {0}'.format(bad_target))
```

do_define_form函数引入了两个参数，根据调用函数可知，传入的expression参数是调用表达式的操作数部分，因此就把操作数评估后的结果在全局环境下与设定的变量绑定了，其关键代码为

```python
 env.define(target,value)
```

这就是实现一个内置过程的办法，接下来我们来看看该如何实现用户定义函数。

##### 评估带有用户定义的表达式

我们先来看看如何使用内置过程`define`定义一个用户过程。

```python
def do_define_form(expressions, env):
    """Evaluate a define form."""
    check_form(expressions, 2)
    target = expressions.first
    if scheme_symbolp(target):
        check_form(expressions, 2, 2)
        # BEGIN PROBLEM 6
        value = scheme_eval(expressions.second.first,env)
        env.define(target,value)
        return target
        # END PROBLEM 6
    elif isinstance(target, Pair) and scheme_symbolp(target.first):
        # BEGIN PROBLEM 10
        name = target.first
        formal = target.second
        body = expressions.second
        process = LambdaProcedure(formal,body,env)
        env.define(name,process)
        return name
        # END PROBLEM 10
    else:
        bad_target = target.first if isinstance(target, Pair) else target
        raise SchemeError('non-symbol: {0}'.format(bad_target))
```

我们看到，这个define函数比之前仅能定义变量的函数多了elif的部分，在这个过程中，函数首先将整个定义代码段分成name函数名称，formal函数参数，和body函数主体三个部分，而后将这三个部分放入LambdaProcedure类创建一个实例，最后调用Frame的define过程将新定义的过程实例与过程名绑定，以便后期lookup函数的查找。

我们来看看创建新过程的实例时候，发生了什么。

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

可以看到，lambda维护着一个方法，当调用到用户实例的时候，就会调用这个方法，打开一个新Frame进行运算。

最后对调用表达式执行apply操作

````python
def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    environment ENV."""
    check_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        return procedure.apply(args, env)
    else:
        new_env = procedure.make_call_frame(args, env)
        return eval_all(procedure.body, new_env)

def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    environment ENV and return the value of the last."""
    # BEGIN PROBLEM 8
    if expressions == nil:
        return None
    else:
        value = expressions.map((lambda x:scheme_eval(x,env)))
        while value is not nil:
            now = value.first
            value = value.second
        return now
````

至此，整个解释器就写完了，再加上内置的自循环函数，一个可以运行Scheme程序的python解释器就大功告成了。在61A 的Scheme项目中，还有如宏和流这种复杂的过程，大家可以自行学习，不过本质还是和内置过程的评估相差不大。学习这个项目的目的不是真的要完成一个解释器，而是要让你学会和理解解释器是如何”翻译“一种语言的，这样你才能更好的去理解各种编程范式，例如函数式编程，面向对象编程等等。



