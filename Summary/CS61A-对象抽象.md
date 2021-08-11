---
title: CS61A-对象抽象
date: 2021-08-08 15:56:30
tags:
- 程序结构
- CS61
- CS61A
categories:
- CS61A
---

## CS61A 对象抽象

#### 目录

>面向对象编程（OOP）
>
>* 对象和类
>* 类属性与实例属性
>* 消息传递与点表达式
>* 类方法
>
>继承与方法
>
>* 继承与方法重写
>* 多重继承
>* 特殊方法
>
>递归对象的实现
>
>* 链表类
>* 树类



在课程的第一章当中我们提到了使用函数进行抽象，这种方式可以很好的对数据进行处理，然而仅仅只考虑函数式编程往往会产生很多问题，举个例子，假设一家银行仅仅使用变量和函数来对人员的账户进行管理，他们使用xx_money ,xx_name来进行人员账户的登记，利用`transfrom()`函数进行转账操作

```python
Tom_money = 100
Bob_money = 200
Jef_money = 400
David_money = 500

def transform(from_account,to_account,number):
    from_account -= number
    to_account +- number
```

突然有一天，银行的i系统在调试过程中被某个程序员整崩溃了，重新找回数据的时候变成了这样

```python
￥&×.money = 100
%^&.money = 200
...
```

银行傻眼了，这下怎么区分金额属于谁啊，他们只能重新寻找曾经顾客注册登记用的纸质材料，费了好大的功夫才好不容易将数据恢复了回去，经过这次事件，银行的工作人员开始思考，是不是应该换一种方式对数据进行记录，经过长时间的研究讨论，他们决定使用面向对象的编程方式重新组织和记录数据，从此以后，再也没有出现过类似的事情。

面向对象OOP，究竟强大在何处？

接下来我们将对OOP进行深入分析，为大家揭开这个谜底。



### 面向对象编程

#### 对象和类

上面我们讲到，利用面向对象的思考方式，我们可以解决银行账户的问题，那么为什么呢？原因就在于，之前银行储存数据时，没有考虑到数据与数据之间的关联性，仅仅只采用了很弱的关系，统一变量名来进行关联，而利用面向对象的思考方式，是将一个账户看做一个对象，每一个变量都是其对象的对象属性。

什么是对象？对象就是具有同一特征的一类元素，比如，一个人就是一个对象，每个人都有鼻子眼睛嘴巴，而且都能行走和思考，这些具有的同一特征就被称作一个类，类就好像上帝在造人的时候使用的模板。再比如一支笔，无论他是钢笔还是水笔，毛笔，都具有写字这个功能，因此同属于笔这个类，而每一支笔都是一个独立的对象。

下面我们通过一个例子来具体讲解类和对象，Lab8的这个例子很好，我就直接借用了。

Tiffany 迟到了，需要在讲座开始前从旧金山赶到伯克利。她会乘坐 BART，但这会花费太长时间。要是有车就好了 一辆巨型卡车会是最好的。

我们要为Tiffany造一辆汽车，我们首先要创建一个汽车类，用户定义的类是由class语句创建的，它由单个子句组成。class 语句定义类名称，然后包含一组语句来定义类的属性：

```python
class car：
```

接下来我们要对这个类增加一些属性，一辆车有哪些属性呢？品牌，型号，颜色，轮子数，汽油量，那么我们要对这个类附加属性，类的构造函数是一个函数，它创建类所概述的对象的实例或单个实例。在 Python 中，构造函数方法名为init，在Car类的构造函数如下所示：

```python
class car:
   def __init__(self, make, model):
    self.make = make
    self.model = model
    self.color = 'No color yet. You need to paint me.'
    self.wheels = Car.num_wheels
    self.gas = Car.gas
```

该__init__有三个参数。第一个参数self，自动绑定到新创建的Car对象。第二个和第三个参数make和model绑定到传递给构造函数的参数，这意味着当我们创建一个Car对象时，我们必须提供两个参数。

于是，汽车这个类我们就构造完毕了，让我们开始造我们的车。蒂芙尼想开一辆特斯拉 Model S 去上课。所以我们可以构造一个厂家为“Tesla”，型号为“Model S”的汽车实例，Python 允许我们通过类的名称来创建类的实例，而不是显式调用。

```python
>>> tiffanys_car = Car('Tesla', 'Model S')
```

在这里，'Tesla'作为 make传入，“Model S”作为model传入， 请注意，我们没有传递参数self，因为它的值始终是正在创建的对象，一个对象是类的一个实例。在这种情况下， tiffanys_car现在绑定到一个Car对象，或者换句话说，绑定到Car类的一个实例。

这样，我们就创建了一个Car类，并且通过Car类创建了一个tiffanys_car的实例对象。

#### 实例属性与类属性

我们继续来看我们上面创建的Car类：

```python
class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas
```

我们会发现，诶，除了我们刚刚利用构造函数所创建的属性，上面怎么还多了几行？

这里就涉及到实例属性和类属性两个概念了，什么是类属性？类属性就是同属于一个类的对象所共有的属性 ，比如，只要是汽车，肯定都是四个轮子，两个头灯，一个后备箱，这些是所有汽车共有的属性，所以被称作类属性。而不同的汽车有不同的型号，品牌，颜色和汽油量，因此这些属性就被称作实例属性。每创建一个实例对象，都会自动将类属性附加给该实例。

#### 消息传递与点表达式

上面，我们为tiffany造了一辆车，但如果有一天，tiffany说，我不想开Tesla了，我想换辆Benz开开，那该怎么办呢？我们当然可以重新利用Car类创造一个新的实例对象，但这太麻烦了，有没有什么办法可以对已有的车辆属性进行改变呢？

有的，利用点符号就可以。

例如，我们可以访问Car类的类属性size

```python
>>> Car.size
'Tiny'
```

同样也可以对Car类的属性进行改变

```python
>>> Car.size = 'Big'
'Tiny'
```

对实例属性的改变也是同样如此，在以下行中，我们访问tiffanys_car的make属性：

```python
>> tiffanys_car.make 
'Tesla'
```

而后我们将make属性修改为‘Benz’:

```python
>>> tiffanys_car.make = 'Benz'
```

这样，我们就成功改造了tiffany的车子，是不是很简单呢？

#### 类方法

让我们再为Car类增加一些东西

```python
class Car(object):
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)
```

这些def叫做类的方法，他们可以调用类的属性，并且输出给外界。方法是特定于类的函数，只有类的一个实例可以使用它们，那么，我们如何在实例上调用方法？你猜对了，点符号！

```python
>>> tiffanys_car.paint('black')
'Tesla Model S is now black'
>>> tiffanys_car.color
'black'
```

上面是一个调用paint方法的过程，我们仔细看一下这个方法，它需要两个参数，那么为什么我们不需要传递两个参数呢？就好像我们在init构造函数中看到的那样，一个类的所有方法都有一个self参数，python会自动将调用该方法的实例绑定到该参数，在这里，self绑定到tiffanys_car这个实例，并调用paint函数改变实例属性

您还可以使用类名和点符号来调用方法；例如，

```python
>>> Car.paint(tiffanys_car, 'red')
'Tesla Model S is now red'
```

请注意，与我们将 Tiffany 的汽车漆成黑色不同，这次我们必须传入两个参数：一个 self和一个 color。这是因为当您使用点表示法从实例调用方法时，Python 知道要自动绑定到哪个实例self。但是，当您使用类中的点表示法调用方法时，Python 不知道Car我们要绘制哪个实例 ，因此我们也要将实例作为参数传入。

### 继承与方法重写

61A讲继承的时候举了一个很有意思的例子，大家小时候都玩过宝可梦吧，让我们来创建一个宝可梦的类

```python
class Pokemon:
    basic_attack = 'tackle'
    damage = 40
    def __init__(self, name, trainer):
        self.name, self.trainer = name, trainer
        self.level, self.hp = 1, 50
        self.paralyzed = False
    def speak(self):
        print(self.name + '!')
    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, 'used', self.basic_attack, '!')
            other.receive_damage(self.damage)
    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')   
```

噢我们可以看见，一个宝可梦类有类属性damage，basic_attack，有实例属性name，level，paralyzed，还有一些类方法。

现在我们再来创建一个电属性的宝可梦类

```python
class ElectricType:
    basic_attack = 'thunder shock'
    damage = 40
    prob = 0.1
    def __init__(self, name, trainer):
          self.name, self.trainer = name, trainer
          self.level, self.hp = 1, 50
          self.paralyzed = False
    def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.receive_damage(self.damage)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, 'is paralyzed!')
    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, 'fainted!')   
```

有些人会说好麻烦，为什么不直接在原来的基础上修改，说的好，这就是继承的概念，我们会发现电属性宝可梦类和宝可梦类只有

类属性部分

```
 prob = 0.1
```

attack方法

```python
def attack(self, other):
        self.speak()
        print(self.name, 'used', self.basic_attack, '!')
        other.receive_damage(self.damage)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, 'is paralyzed!')
```

这两个模块是不同的，其他都是相同的，所以我们可以这样来写电属性宝可梦类。

```python
class ElectricType(Pokemon):
    basic_attack = 'thunder shock'
    prob = 0.1
    def attack(self, other):
        Pokemon.attack(self, other)
        if random() < self.prob and type(other) != ElectricType:
            other.paralyzed = True
            print(other.name, 'is paralyzed!')
```

这里的`class <Class Name>(<Superclass Name>):`结构就是继承，通过继承，我们可以在新创建的类中保留下原有的类属性和实例属性

```python
>>> Pica = ElectricType('pica','me')
>>> Pica.hp
50
```

可以看得出，新类所创建的实例拥有和被继承类相同的实例属性。

我们还可以看到，attack方法被重写了，原来attack的方法被覆盖了，这种情况叫做方法重写，新类可以创建与被继承类相同名称的方法，将会覆盖原有方法.

```python
>>>Pica.attack(Yib)
'Yib is paralyzed!'
```

这时候有人会问，那如果需要增加或删除实例属性项，是不是要重写一遍构造函数？

当然，重写固然没有问题，但是还有更简便的方法。

我们举一个61A Project ant的例子

假设我们有一个昆虫类

```python
class Insect(object):
    """An Insect, the base class of Ant and Bee, has armor and a Place."""
    
    is_ant = False
    damage = 0
    is_watersafe = False
    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, armor, place=None):
        """Create an Insect with an ARMOR amount and a starting PLACE."""
        self.armor = armor
        self.armor = armor
        self.place = place  

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the insect from its place if it
        has no armor remaining.

        >>> test_insect = Insect(5)
        >>> test_insect.reduce_armor(2)
        >>> test_insect.armor
        3
        """
        self.armor -= amount
        if self.armor <= 0:
            self.place.remove_insect(self)

```

接下来我们要创建一个新的Ant类，这个Ant类是Insert类的一个子类，它继承了Insert类的一些方法和属性，不同的是，我们要修改一下Ant类当中amor属性的默认值。

```python
class Ant(Insect):
    """An Ant occupies a place and does work for the colony."""

    is_ant = True
    implemented = False  # Only implemented Ant classes should be instantiated
    food_cost = 0
    blocks_path = True
    is_container = False
    is_double = False
    # ADD CLASS ATTRIBUTES HERE

    def __init__(self, armor=1):
        """Create an Ant with an ARMOR quantity."""
        Insect.__init__(self, armor)

    def can_contain(self, other):
        return False

```

我们使用了`Insert.__init__(self,armor=1)`来修改父类的构造函数

我们再以Ant为父类，创建一个名为HungryAnt的子类

```python
class HungryAnt(Ant):
    """HungryAnt will take three turns to digest a Bee in its place.
    While digesting, the HungryAnt can't eat another Bee.
    """
    name = 'Hungry'
    food_cost = 4
    time_to_digest = 3
    # BEGIN Problem 6
    implemented = True  # Change to True to view in the GUI
    # END Problem 6

    def __init__(self, armor=1):
        # BEGIN Problem 6
        Ant.__init__(self, armor)
        self.digesting = 0
        # END Problem 6

    def eat_bee(self, bee):
        # BEGIN Problem 6
        bee.armor = 0
        self.place.remove_insect(bee)
        self.digesting = self.time_to_digest
        # END Problem 6

    def action(self, colony):
        # BEGIN Problem 6
        if self.digesting == 0:
            if random_or_none(self.place.bees) !=None:
                self.eat_bee(random_or_none(self.place.bees))
            else:
                pass
        else:
            self.digesting -= 1
        # END Problem 6
```

我们看到，这里我们使用`Insert.__init__(self,armor)`继承了父类的所有实例属性，并且在这基础上又增加了一个digesting属性作为该类独有的实例属性。

#### 多重继承

多重继承顾名思义，就是从多个父类继承的子类，比如，作为你父母的孩子，你既继承了你父亲的身高智慧，又继承了你母亲的高鼻梁大眼睛，因此在你这个类当中，既有父亲传给你的属性，又有母亲传给你的属性。

Python 支持子类从多个基类继承属性的概念，这种语言特性称为多重继承。

恩，突然一下子想不出什么特别好的例子，大家可以在CS61A的一些习题当中找一些例子来看。

#### 特殊方法

在 Python 中，某些特殊名称会在特殊情况下由 Python 解释器调用。例如，每当构造对象时，都会自动调用类的__init__方法。每当打印对象时会自动调用__str__方法，在交互式会话到显示值会调用repr方法。

假设我们有一个类A

```python
class A:
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def __str__(self):
        return '<' + self.name + '>'
    def __repr__(self):
        return self.name
```

那么我们在打印A类所构造的实例对象时，就会自动调用__str__函数打印，交互式对话输入自动调用repr

```python
>>> a = A('alien',4)
>>> print(a)
<alien>
>>> a
alien
```

我们用Link对象举个例子

```python
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
```

虽然我们还没有讲到链表类，但是我们可以看到，Link类也重写了str和repr方法，因此Link类实现 方法的实现如下

```python
>>>s = Link(2, Link(3, Link(4)))
>>>s
Link(2, Link(3, Link(4)))
>>>print(s)
< 2 3 4>
```

除了最基本的str和repr特殊方法之外，python也支持对其他特殊方法进行修改，我们这里以contain特殊方法为例进行介绍,contain特殊方会在对实例使用in指令时自动调用

```python
def __contains__(self,x):
    if self.first == x：
        return True
    elif self.rest is Link.empty:
        return False
    return x in self.rest
```

这样我们就改写了contain特殊方法

```python
>>>l=Link(1,Link(2,Link(3)))
>>>2 in l
True
>>>4 in l
False
```

下面是一些常见的特殊方法，大家可以对其进行改写试一试。

![image-20210809105526287](https://i.loli.net/2021/08/09/eG2QDp4y7vlIH9a.png)



### 递归对象的实现

对象可以有其他对象作为属性值。当某个类的对象具有同一个类的属性值时，它就是递归对象。

常见的递归对象有链表类和树类两种

#### 链表类

本章前面已经提前给出Link类的概念，我们再次回顾一下，链表由第一个元素和列表的其余部分组成，链表的其余部分只能是一个链表，链表是一个序列，它的长度是有限的，并且支持按索引选择元素。

我们可以实现一个Link类，表示一个链表对象。每个Link实例都有两个实例属性，first和rest。

````python
class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
````

我们可以看出，链表第一个元素没有限制，但是第二个元素只能是一个链表或空链表，由于每个链表的第二个元素都是链表，所以链表是一个递归对象

让我们通过一个例子来进一步加深印象，这道题是61A的题目。

> 编写一个函数store_digits，接收一个整数n并返回一个链表，其中链表的每个元素都是 的一个数字n。

```python
def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    # In iteration
    new_link = Link.empty
    while n !=0:
        new_link = Link(n%10,new_link)
        n = n//10
    return new_link
```

这道题目就利用了Link递归的特性，通过递归过程对不断加长拓展链表，最终构成一个单一数字的链表。

#### 树类

回想一下，树是一种递归抽象数据类型，它具有label（存储在树根中的值）和branches（根正下方的树列表）两种不同类型的值，在数据抽象一章中，我们曾经使用将树视为列表的构造函数和选择器函数实现过树。

```python
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
```

但是我们会发现使用这种方式创建的树是不可更改的，因为我们无法为调用表达式赋值，为了能够实现对树的修改，我们将构造器的功能用树类实现，而将选择器的功能用访问实例属性的点表达式实现

```python
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
```

这样一来，我们就可以方便的创建树对象和修改树对象的label和branches属性，而不需要通过调用函数来获得树对象的各项属性，同时我们还可以在树类中任意增加各种方法，同样也只需要对实例进行方法调用即可。

此外，使用构造选择函数和列表实现的树ADT与使用类与对象实现的树ADT还有如下的区别

![image-20210809154119551](https://i.loli.net/2021/08/09/q6QKxZFmIGuWihL.png)

总的来说，利用类实现的树ADT具有可变的特点，因此使用起来要比函数式的ADT更加便捷。









