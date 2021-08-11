---

title: CS61A-过程抽象
date: 2021-06-12 15:15:32
tags:
- 程序结构
- CS61
- CS61A
categories:
- CS61A
---

## CS61A 过程抽象

#### 目录

>程序设计的基本元素
>
>* 表达式
>* 变量与环境
>* 复合过程与函数
>* 条件表达式与判定符号
>* 过程作为黑箱抽象
>
>过程产生的计算
>
>* 线性递归与迭代
>* 树形递归
>
>高阶函数抽象
>
>* 过程作为参数
>* 过程作为一般性的方法
>* 过程作为返回值
>* 使用匿名函数构造过程



### 程序设计的基本元素

********

一个强有力的语言，需要成为一种框架，使我们能够在里面组织自己的计算思想，为了达成这个目的，语言提供了三种机制：

一是基本的表达形式，也就是表达式，在python中，3，‘s’，这些都是表达式，3 + int('s'),这叫做复合表达式，表达式是语言最简单的个体。

二是组合的方法，通过组合，可以将各种表达式结合起来构造出复杂的元素

三是抽象的方法，通过抽象，我们可以对过程进行命名，并将它们当作单元去使用

#### 表达式 

以python为例，我们先来看一些基本表达式，基本表达式可以是数字，字符，字符串

```python
's',1,'hello'
```

通过将基本表达式进行组合，我们可以得到组合式

>3-1
>
>'s' + 'e'

组合式表示一个过程，将运算符所刻画的过程，应用有关的实际参数，有些嵌套表达式比较复杂，例如

```python
(2+(4*6))*(3+5+7)
```

 对于这个表达式，我们可以采取一棵树的形式来表示，设想运算对象的值向上穿行，而后在越来越高的层次中组合起来，这种计算过程叫做树形积累。

![image-20210612194156857](https://i.loli.net/2021/06/12/BCrLjKNHeXEtiW3.png)



#### 变量与环境

我们在设计程序的时候会遇到这样一个问题，假设我们需要计算一个半径为2的圆的面积，我们使用`pi*(2**2)`进行计算，当我们想要计算的半径变为3时，我们又得写表达`pi*(3**2)`,为了避免这种情况的出现，我们将值2与名称r关联起来，而后我们只需要使用`pi*(r**2)`就可以计算半径为r对应值的圆的面积，我们把定义的名称r叫做变量。

不同语言定义变量的方式不同

Lisp

```lisp
(define r 2)
```

Python

````python
r = 2
````

C

```C
int r = 2
```

变量是语言抽象里最简单的一种方式，进一步思考，我们既然可以将值与符号相关联，这说明解释器必须维持某种储存能力，以保证一对一的关系，这种储存叫做环境。

#### 复合过程与函数

由上文可知，数和算数运算是基本的数据和过程，组合式的嵌套提供了一种组织多个操作的方法，而定义是一种受限的抽象手段，仅仅只能对值进行抽象

那么如果我们要对过程进行抽象该怎么办呢？

过程定义是一种威力更大的抽象技术，通过它可以为复合过程提供名称，而后便可以利用名称调用所对应的复合过程，这个复合过程在高级语言中被叫做函数，**为了方便大家观看，接下来所有定义的复合过程我们均使用函数这个名称。**

例如，我们要求某个数的平方，因此我们给求平方的过程取一个名字叫做square

不同语言定义函数/复合过程名称的方式不同

*Lisp*

```lisp
(define (square x) (* x x))
```

*Python*

```python
def square(x):
    return x**2
```

定义好之后就可以使用square进行调用

```python
(sqare 21)
square(2)
```

我们可以利用已定义好的函数去构建其他过程，以python为例

```python
def sum_sq(x,y):
    return square(x) + square(y)
```

还可以利用sum_sq去构造其他过程

```python
def f(a):
    return sum_aq(a,a)
```

#### 条件表达式与符号

至此我们能定义的函数还是很有限，因为没法去做检测，而后依据结果去进行分支操作，因此我们需要条件表达式

不同的语言中条件表达式不同

*Lisp*

```lisp
(define (abs x)
     (cond  (> x 0)x)
            (= x 0)0)
            (< x 0)(-x))
     )
)
```

Python没有switch语句，可以用if..elif...替代

```python
def abs(x):
    if x > 0:
        return x
    elif x = 0:
        return 0
    else x <0:
        return -x
```

if是一种特殊形式，是条件表达式的一种受限形式，适用于分情况分析只有两种情况的情况下。

除了><=之外，还可以使用and，or，not进行判断，and表达式从左到右依次求值，如果某个值为假则表达式为假，后面不再求值，or表达式如果某个表达式为真，则表达式为真，后面也不在再求值。

例如Lisp中

```lisp
(and(> x 5)(< x 10))
```

#### 函数作为黑箱抽象

sqrt的例子可以自然的分解成若干个子问题，每一个工作都分配给独立的一个过程完成，因此sqrt的实现过程如图，它们直接反映了原问题是如何分解成为子问题并解决的

![image-20210612202953454](https://i.loli.net/2021/06/12/u4zixB95rycdopg.png)

这一分解的重要性，在于分解中的每个函数都完成了一件可以清楚标明的工作，因此可以进行替换和修改。用户在使用的过程中，不需要知道是如何实现的 。

##### 内部定义与块结构

为了突出重点，我们可以把辅助所使用的good-enough，imporve等辅助函数放入sqrt函数中，这种嵌套的定义称为块结构，因为x在sqrt内部是受约束的，而辅助过程都定义在sqrt里面，也就是说辅助过程都可以使用x的值。



### 函数产生的计算

*****

#### 线性递归与迭代

我们以函数的阶乘为例，讲解函数的递归和迭代。

首先，我们使用递归来计算阶乘

考虑阶乘函数：

```python
n! = n*(n-1)*(n-2)...1
(n-1)! = (n-1)*(n-2)...1
n! = n*(n-1)! 
```

这样，我们就能通过算出(n-1)!，i进而计算出n！

```python
def factorial(n):
     return n*factorial(n-1)
```

但是这就出现了一个问题，这个函数会陷入无限循环，因为没有一个标志告诉函数什么时候停下来，所以我们需要一个base_case去限制递归终止的条件。

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
```

这个过程如图所示

![image-20210612215413983](https://i.loli.net/2021/06/12/EoGL5rvkQ8ilTzX.png)



于是我们总结出迭代所需要的三个要素：

*一是base_case也就是迭代终止条件*

*二是可迭代拆分的结构，比如`factorial(n)`的结果就可以分解成为`n * factorial(n-1)`

*三是可以连续传递*，验证n与n-1的规则是否通用。



但是，在设计迭代结构的过程中可能会遇到，由于存在其他规则，使得过程非单一方向，传入的参数无法进行迭代，比如

>乒乓序列从 1 开始计数，并且总是向上计数或向下计数。在元素 处k，如果k是 7 的倍数或包含数字 7 ，则方向切换。 下面列出了乒乓序列的前 30 个元素，方向交换在第 7、第 14、第 17、第 21、第 27 处用括号标记，和第 28 个元素：
>
>1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6,
>
>def pingpong(n): ?

这里的`pingpong(n)`和`pingpong(n-1)`无法形成迭代关系，因为每逢7就要切换方向，因此，我们在函数中再定义一个函数itera，利用itera来代替pingpong进行迭代,n仅作为base_case。

```python

def pingpong(n):
    def itera(out,index=1,adder=1)
        if index == n:
            return out
        if index%7==0:
            return itera(out+adder,index+1,adder=-adder)
        else:
            return itera(out+adder,index+1,adder=adder)
    out = itera(1,1,1)
    return out 
            
```

这样就实现了迭代，这里的迭代只针对内部函数itera，n在itera中相当于一个常数。



而后，我们再使用迭代对阶乘进行计算：

```python
def factorial(n):
    a = 1
    for i in range(n):
        a = a*i
    return a
```

由上文可知，迭代的计算并没有重复调用自身，而是在单个函数框架内部控制了一个重复运行的结构，并利用for循环设置停止条件。

迭代的表示如下：

![image-20210613110228758](https://i.loli.net/2021/06/13/SmeKwilTO8B7Z2t.png)



迭代和递归是两种最常见的循环过程，其主要不同点在于：

一是框架，迭代的整个过程都是在函数建立的单个框架内部执行的，而递归由于不断重复调用自身，所以不断的建立新的函数框架，使用Pythontutor可以清晰的看到这两个过程。

迭代：

![image-20210613110437725](https://i.loli.net/2021/06/13/X86tKiEOypvATkb.png)

递归：

![image-20210613110636563](https://i.loli.net/2021/06/13/rLJNnMR8fzq2SBX.png)

二是过程，迭代实际上是一个过程中的一部分，而递归是一个完整的过程，也就是说递归中可能包含迭代，但是迭代中肯定不会包含递归。



#### 树形递归

树形递归是一种特殊的递归形式，我们以斐波纳契数列为例，讲解树形递归的实现方式。

首先我们以递归的思路来考虑

`feb(n)`和`feb(n-1)`有什么关系？

貌似没有关系，但是我们知道`feb(n)=feb(n-1)+feb(n-2)`

因此我们可以这样设计递归

```python
def feb(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
        
```

这个过程同时进行了两个方向的递归，这种递归叫做树递归，表示如下：

![image-20210613112437233](https://i.loli.net/2021/06/13/NnIUPVbqSmXe4lB.png)

树形递归的作用就是同时进行多个方向的递归，有些函数需要多个递归过程相加，例如HW02中的河内塔问题

> Q7：河内塔
> 一个名为河内塔的经典谜题是一种游戏，它由三根杆和许多可以滑到任何杆上的不同大小的圆盘组成。谜题开始时，n圆盘在start棒上按尺寸升序排列整齐，最小的在顶部，形成圆锥形状。
>
> ![image-20210613154038670](https://i.loli.net/2021/06/13/BeUAztOT3pEMG9L.png)
>
> 拼图的目标是将整个堆栈移动到一根end杆上，遵守以下规则：
>
> 一次只能移动一个磁盘。
> 每次移动都包括从一根棒上取下顶部（最小）圆盘并将其滑到另一根棒上，位于该棒上可能已经存在的其他圆盘的顶部。
> 任何磁盘都不能放置在较小磁盘的顶部。
> 完成 的定义move_stack，它打印出在不违反规则的情况下将n圆盘从start杆移动到杆所需的步骤end。提供的print_move函数将打印出将单个磁盘从给定的移动origin到给定的步骤destination。
>
> 题目给出了两个内置函数
>
> ```python
> def print_move(origin, destination):
>     """Print instructions to move a disk."""
>     print("Move the top disk from rod", origin, "to rod", destination)
> 
> def move_stack(n, start, end):
>     """Print the moves required to move n disks on the start pole to the end
>     pole without violating the rules of Towers of Hanoi.
> ```

我们仔细思考这个过程，我们知道，如果要把一个三层河内塔从Bar1移动到Bar3，那么我们应该`move_stack(3,1,3)`,而`move_stack(3,1,3)`这个过程可以分解为

一.先将上面两层移动至2,即`move_stack(2,1,2)`

二.将底层移动到3,即`move_stack(1,1,3)`

三.将在2的两层移至3,即`move_stack(2,2,3)`

我们会发现实际上`move_stack(n,a,c)`可以分解为`move_stack(n-1,a,b)`，`move_stack(1,a,c)`,`move_stack(n-1,b,c)`

因此这个递归函数是一个树递归，三个递归同时在运行，最终合并得出最终结果。

具体实现如下：

```python
def move_stack(n,start,end):
        bars = [1,2,3]
    if n == 1:
        print_move(start,end)
    else:
        c=[bar for bar in bars if bar not in [start,end] ]
        c = c[0]
        a = start
        b = end 
        move_stack(n-1,a,c)
        move_stack(1,a,b)
        move_stack(n-1,c,b)

```

这里的base_case就是n==1。



### 高阶函数抽象

******

#### 函数作为参数

思考一下以下两个函数

第一个 sum_naturals函数计算最大为n的自然数之和

```python
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + [k], k + 1
    return total

```

第二个sum_pi计算系列中的项的总和

```python
def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + [8 / ((4*k-3) * (4*k-1))], k + 1
    return total
```

我们发现，他们实际上都共有一个框架，唯一不同的实际上是一个关于k的函数

```python
def xx (n):
    total, k = 0, 1
    while k <= n:
        total, k = total + <term>(k), k + 1
    return total
```

因此我们可以将这个关于k的函数作为参数传入主函数，这样就实现了填充同一个模板中的槽来生成每个函数，具体实现如下：

```python
def sum(n,term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def natural(k):
    return k

def pi(k):
    return 8 / ((4*k-3) * (4*k-1))

```

这样一来，我们就将整个结构抽象了出来，通过传入不同函数对过程进行控制。



#### 函数作为一般性方法



刚才我们说到，函数可以作为参数传递给函数，我们再来看一个例子，这个例子是计算黄金分割率的。

```python
1	def improve(update, close, guess=1):
2	    while not close(guess):
3	        guess = update(guess)
4	    return guess
5	
6	def golden_update(guess):
7	    return 1/guess + 1
8	
9	def square_close_to_successor(guess):
10	    return approx_eq(guess * guess,
11	                     guess + 1)
12	
13	def approx_eq(x, y, tolerance=1e-3):
14	    return abs(x - y) < tolerance
15	
16	phi = improve(golden_update,
17	              square_close_to_successor)
```

我们会发现，虽然结果没有问题，但是整个函数结构显得很凌乱，为了解决这个问题，我们引入了嵌套定义的概念，为了解决函数结构不整齐的问题，于是上文的函数结构就可以改变为：

```python
	def improve(guess=1):
	    def golden_update(guess):
	        return 1/guess + 1
        
	    def square_close_to_successor(guess):
            return approx_eq(guess * guess,guess + 1)
	
	    def approx_eq(x, y, tolerance=1e-3):
	        return abs(x - y) < tolerance
        
        while not square_close_to_successor(guess):
	        guess = golden_update(guess)
	    return guess
	
	phi = improve()
```

这样一来整体的函数结构就清晰多了。



#### 函数作为返回值

通过创建返回值本身就是函数的函数，我们可以在我们的程序中实现更强大的表达能力。词法作用域编程语言的一个重要特性是本地定义的函数在返回时保持其父环境。以下示例说明了此功能的实用性。

一旦定义了许多简单的函数，函数组合就是包含在我们的编程语言中的自然组合方法。也就是说，给定两个函数f(x)和g(x)，我们可能想要定义h(x) = f(g(x))。我们可以使用现有工具定义函数组合：

```python
def compose1(f, g):
        def h(x):
            return f(g(x))
        return h
```

这时候返回的函数就是f(g(x))

函数作为返回值的一个重要应用就是函数的柯里化，我们可以使用高阶函数将带有多个参数的函数转换为每个带有一个参数的函数链。更具体地说，给定一个函数f(x, y)，我们可以定义一个函数g使得g(x)(y)等价于f(x, y)。这里，g是一个高阶函数，它接受单个参数x并返回另一个接受单个参数y 的函数。这种转换称为柯里化。

柯里化的具体实现过程如下：

```python
def curi_pow(x):
    def f(y):
        return pow(x,y)
    return f

```

当调用`curi_pow(2)(3)`时，首先计算curi_pow(2),返回的函数实际上就是 `lambda  x: pow(2,x)`，这个结构可能大家现在还看不懂，不过后面讲到lambda匿名函数的时候就懂了。因此`curi_pow(2)（3）`实际上是`lambda x:pow(2,x)(3)`也就是pow(2,3)

我们可以将柯里化的过程也抽象成一个函数，使得其可以对所有拥有两个参数的函数进行柯里化

```python
def curi(f):
    def g(x):
        def h(y):
            return f(x,y)
        return h
    return g
```

具体推导过程 如下：

要使得  s(x)(y) = f(x,y)，则s = lambda x:lambda y :f(x,y)，将lambda函数转为正常函数即可。

柯里化也可以反向进行，具体实现过程为：

```python
def uncuri(g):
     def h(x,y):
            return g(x)(y)
     return h
```

同理，要使得 f(x,y) = g(x)(y)，则 f = lambda x,y : g(x)(y)，将lambda函转换为正常函数即可。



#### 使用匿名函数构造过程

到目前为止，每次我们想要定义一个新函数时，我们都需要给它一个名字。但是有一种函数不需要命名就可以调用，这种函数被称作匿名函数，在 Python 中，我们可以使用lambda 表达式动态创建函数值，这些表达式的计算结果为未命名的函数。一个 lambda 表达式的计算结果是一个函数，它有一个返回表达式作为它的主体。

lambda 表达式的结果称为 lambda 函数。它没有内在名称（因此 Python 打印<lambda>作为名称），但除此之外它的行为与任何其他函数一样。

```python
s = lambda x:x*x
s(2) = 4
```

这相当于把s这个名称指向一个函数，这个函数是匿名函数lambda。

一些程序员发现使用来自 lambda 表达式的未命名函数更短、更直接。然而，众所周知，复合lambda表达式难以辨认，尽管它们很简洁。下面的定义是正确的，但是很多程序员很难快速理解它。

```python
 compose1=lambda f,g:lambda x:f(g(x))
```

匿名函数还可以是带递归的匿名函数，这个结构较为复杂，我们以阶乘为例，来讲解一下这个结构。

我们知道，使用递归来进行阶乘的计算如下所示：

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

```

那么如果使用匿名函数来进行递归，结构又该是什么样的呢？

我们先来看一个简单一点的方案。

```python
fact = lambda n:1 if n==1 else n*fact(n-1)
```

这样的话我们只需要使用fact(3)就可以进行调用循环，但是这里有个问题就是，如果我们改变了左侧的名称，这个结构就没法用了，为了能够构建一个更加通用的匿名函数，我们需要将这个函数进一步改造，首先，我们将函数本身作为匿名的参数传入,我们这里将函数命名为f

```python
lambda n,f:1 if n==1 else n*f(n-1,f) 
```

于是这个函数体就是我们所需要的匿名函数体，问题在于，如果这样构建匿名函数的话，我们需要传入一个参数f，也就是函数体本身，那么又无法通用了，因为如果你令fact= lambda n,f:1 if n==1 else n*f(n-1,f)，那么你要使用fact(n,fact)进行调用，这样还是无法满足通用性,因为我们要实现的是<random name>(n) 调用。

解决这个问题的方法是在函数外再套一层函数，将构建的函数f当作参数传入。

fact = lambda n:(lambda g:g(n,f))(lambda n,f:1 if n==1 else n*f(n-1,f))

这个结构的原理是这样的，fact(3)首先等于`(lambda f:f(3,f))`，然而由于后i面还有一个`(lambda n,f:1 if n==1 else n*f(n-1,f))`因此f函数的值被填充为匿名函数，成为f(3,f) 其中 `f(n,f)=(lambda n,f:1 if n==1 else n*f(n-1,f))`。