## python3  

* **·列表**：  

  * `append()` 添加元素到列表末尾。

  * `insert()`在任意位置插入元素。

  * `count(s)`返回列表元素中s的数量。

  * `remove()`移除列表中的任意指定值。

  * `reverse()`反转整个列表。

  * `extend(b)`将列表b中的所有元素添加到另一个列表的末尾。

  * `sort()`用于给列表排序，前提是列表的元素是可比较的。

  * `del()`删除指定位置的列表元素。

  * 将列表用作**栈**：  

    * `pop()`弹出末尾的元素。可以使用`pop(i)`弹出第i个元素。

  * 将列表用作**队列**：

    * 使用`pop(0)`弹出列表中的第一个元素。  

  * 创建列表---**列表推导式**：列表推导式为从序列中创建列表提供了一个简单的方法。如果没有列表推导式，一般都是这样创建列表的：通过将一些操作应用于序列的每个成员并通过返回的元素创建列表，或者通过满足特定条件的元素创建子序列。 可以如下创建：  

    ```python
    >>> squares = []
    >>> for x in range(10):
    ...     squares.append(x**2)
    ...
    >>> squares
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

    注意这个 for 循环中的被创建（或被重写）的名为 `x` 的变量在循环完毕后依然存在。使用如下方法，我们可以计算 squares 的值而不会产生任何的副作用：

    ```python
    squares = list(map(lambda x: x**2, range(10)))
    ```

    等价于：  

    ```python
    squares = [x**2 for x in range(10)]
    ```

    列表推导式由包含一个表达式的中括号组成，表达式后面跟随一个 for 子句，之后可以有零或多个 for 或 if 子句。结果是一个列表，由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成。

    例如，如下的列表推导式结合两个列表的元素，如果元素之间不相等的话：

    ```python
    >>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    ```

    等同于： 

    ```python
    >>> combs = []
    >>> for x in [1,2,3]:
    ...     for y in [3,1,4]:
    ...         if x != y:
    ...             combs.append((x, y))
    ...
    >>> combs
    [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
    ```

    列表推导式也可以嵌套:  

    ```python
    >>> a=[1,2,3]
    >>> z = [x + 1 for x in [x ** 2 for x in a]]
    >>> z
    [2, 5, 10]
    ```




* **字符串**：  

  * `split()`函数[split(str="", num=string.count(str))](http://www.runoob.com/python3/python3-string-split.html)  以str为分隔符截取字符串，如果num有指定值，则仅截取num个字符串。str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。num -- 分割次数。分割后的字符串转换为了list。如下：  

    ```python
    >>> s = "We all love Python"
    >>> s.split()
    ['We', 'all', 'love', 'Python']
    >>> x = "shiyanlou:is:waiting"
    >>> x.split(':')
    ['shiyanlou', 'is', 'waiting']
    ```

  * `join()`方法使用指定字符连接多个字符串，需要一个包含字符串元素的列表作为输入，然后连接列表内的字符串元素。  如下：  

    ```python
    >>> "-".join("GNU/Linux is great".split())
    'GNU/Linux-is-great'
    ```

    在上面的例子中，我们基于空格 `" "` 分割字符串 `"GNU/Linux is great"`，然后用 `"-"` 连接它们。 

  * 字符串实现反转的方法：  

    * 使用字符串切片：`result = s[::-1]`
    * 使用列表的reverse（）：`l = list(s) result = “".join(l.reverse())"”`

  * 分几行输入字符串，并且希望行尾的换行符自动包含到字符串当中，可以使用三对引号：`"""..."""` 或 `'''...'''` 。 例如：  

    ```python
    >>> print("""\
    ... Usage: thingy [OPTIONS]
    ...      -h                        Display this usage message
    ...      -H hostname               Hostname to connect to
    ... """)
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    ```

  * 返回字符串的标题版本：`title()` ，即单词首字母大写，其余字母小写。  

  * 使用`upper()`返回字符串的全部大写的版本。使用`lower()`返回字符串的全部小写版本。

  * `swapcase()`返回字符串大小写交换后的版本。

  * `isalnum()`检查所有的字符是否为字母或数字，若全为字母或数字则返回`True`，否则返回`False`。  

  * `isalpha()`检查字符串之中是否只有字母。

  * `isdigit()`检查字符串之中是否只有数字。

  * `islower()`检查字符串之中是否所有字母为小写。

  * `istitle()`检查字符串是否为标题样式。

  * `isupper()`检查字符串中所以字符是否为大写。  

    









* “`Year {} Rs. {:.2f}".format(year, value)` 称为字符串格式化，大括号和其中的字符会被替换成传入 `str.format()` 的参数，也即 `year` 和 `value`。其中 `{:.2f}` 的意思是替换为 2 位精度的浮点数。 

* `divmod(num1, nim2)`返回一个元祖，包含两个值，第一个是num1和num2**相整除**得到的值，第二个是num1和num2**求余**得到的值。

* 手动执行类型转换：  

  我们可以手动的执行类型转换。

  | 类型转换函数    | 转换路径         |
  | --------------- | ---------------- |
  | `float(string)` | 字符串 -> 浮点值 |
  | `int(string)`   | 字符串 -> 整数值 |
  | `str(integer)`  | 整数值 -> 字符串 |
  | `str(float)`    | 浮点值 -> 字符串 |

* count()方法语法：

  ```python
  str.count(sub, start= 0,end=len(string))
  ```

  * sub -- 搜索的子字符串
  * start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
  * end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。  
  * 返回子字符串在字符串中出现的次数。

  

* 如果你想要检查列表是否为空，请这样做：

  ```python
  if list_name: # 列表不为空
      pass
  else: # 列表为空
      pass
  ```

* lambda: 用于创建匿名函数。，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。   

  * lambda的一般形式是关键字lambda后面跟一个或多个参数，然后紧跟一个冒号，最后是一个表达式。**lambda是一个表达式，而不是一个语句**。他可以返回一个值（即一个新的函数）。在只需要编写简单函数的情况下，可以使用它来代替def：  

    ```python
    f = lambda x,y,z : x+y+z  
    print f(1,2,3)  
      
    g = lambda x,y=2,z=3 : x+y+z  
    print g(1,z=4,y=5) 
     
    结果：
    6  
    10  
    ```

  * lambda表达式常用来编写跳转表（jump table），也就是行为的列表或字典（相当于C中的switch...case）：  

    ```python
    L = [(lambda x: x**2),  
        (lambda x: x**3),  
        (lambda x: x**4)]  
    print L[0](2),L[1](2),L[2](2)  
    # 这里的方括号内容对应于L中的每一种情况，圆括号的内容对应于参数的值。
    D = {'f1':(lambda: 2+3),  
        'f2':(lambda: 2*3),  
        'f3':(lambda: 2**3)}  
    print D['f1'](),D['f2'](),D['f3']() 
     
    结果：
    4 8 16  
    5 6 8 
    ```

  * **闭包**---一个定义在函数内的函数，他使得变量即使脱离了该函数的作用于范围也依然能够被访问到。  

    ```python
    >>> def my_add(n):
    ...     return lambda x:x+n
    
    >>> add_3 = my_add(3)
    >>> add_3(7)
    10
    ```

    这里lambda函数就是一个闭包，在全局作用域范围中，add_3(7)可以正常执行且返回值为10，之所以返回10是因为在my_add局部作用域中，变量n的值在闭包的作用使得它在全局作用域也可以被访问到。 

* **map()** 会根据提供的函数对指定序列做映射。

  第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

  map() 函数语法：

  ```python
  map(function, iterable, ...)
  ```

* `sorted()`函数：  

  **sorted()** 函数对所有可迭代的对象进行排序操作。

> **sort 与 sorted 区别：**
>
> sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
>
> list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。  

sorted 语法：

```python
sorted(iterable, key=None, reverse=False)  
```

参数说明：

- iterable -- 可迭代对象。
- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。  

`>>>sorted([5, 2, 3, 1, 4]) [1, 2, 3, 4, 5]                      # 默认为升序`

你也可以使用 list 的 list.sort() 方法。这个方法会修改原始的 list（返回值为None）。通常这个方法不如sorted()方便-如果你不需要原始的 list，list.sort()方法效率会稍微高一些。

`>>>a=[5,2,3,1,4] >>> a.sort() >>> a [1,2,3,4,5]`

另一个区别在于list.sort() 方法只为 list 定义。而 sorted() 函数可以接收任何的 iterable。

`>>>sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}) [1, 2, 3, 4, 5]`

利用key进行倒序排序

要进行反向排序，也通过传入第三个参数 reverse=True：

`>>>example_list = [5, 0, 6, 1, 2, 7, 3, 4] >>> sorted(example_list, reverse=True) [7, 6, 5, 4, 3, 2, 1, 0]`  

* `ord()` 函数：  

  ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。 

- 在 Python 里我们使用文档字符串（*docstrings*）来说明如何使用代码，这在交互模式非常有用，也能用于自动创建文档。下面我们来看看使用文档字符串的例子。

  ```python
  #!/usr/bin/env python3
  import math
  
  def longest_side(a, b):
      """
      Function to find the length of the longest side of a right triangle.
  
      :arg a: Side a of the triangle
      :arg b: Side b of the triangle
  
      :return: Length of the longest side c as float
      """
      return math.sqrt(a*a + b*b)
  
  if __name__ == '__main__':
      print(longest_side.__doc__)
      print(longest_side(4,5))
  ```

- 高阶函数（*Higher-order function*）或仿函数（*functor*）是内部至少含有一个以上步骤的函数：

  - 使用一个或多个函数作为参数
  - 返回另一个函数作为输出

  Python 里的任何函数都可以作为高阶函数。

  ```python
  >>> def high(func, value):
  ...     return func(value)
  ...
  >>> lst = high(dir, int)
  >>> print(lst[-3:])
  ['imag', 'numerator', 'real']
  ```

- #### map 函数

  `map` 是一个在 Python 里非常有用的高阶函数。它接受一个函数和一个序列（迭代器）作为输入，然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果。

  举例：

  ```pythons
  >>> lst = [1, 2, 3, 4, 5]
  >>> def square(num):
  ...     "返回所给数字的平方."
  ...     return num * num
  ...
  >>> print(list(map(square, lst)))
  [1, 4, 9, 16, 25]
  ```

- #### open()函数

  打开文件，需要两个参数：    

  - 一是文件路径或文件名；
  - 二是文件中的打开模式。  
    - `r` ：以只读模式打开，只能读取文件但不能编辑/删除文件的任何内容。
    - `w`：以写入模式打开，如果文件存在将会删除里面的所有内容，然后打开这个文件进行写入。
    - `a`：以追加模式打开，写入文件中的任何数据将自动添加到末尾。    

  > 不要轻易对有内容的文件以写入的方法打开,这样会删掉文件的所有内容.

  默认模式为只读模式。使用`close()`方法来关闭文件。  

- #### read()函数

  使用`read()`方法来一次性读取整个文件。在调用一次`read()`后，再次使用只会返回一个空字符串，因为他已经读取完了整个文件。

  `read(size)`有一个可选的参数`size`，用于指定字符串长度。如果没有指定或者指定为负数，就会读取并返回整个文件。当文件大小为当前机器内存两倍时，就会产生问题。反之，会尽可能按比较大的`size`读取和返回数据。  

  - `readline()`能帮助每次读取文件的一行。

  - `readlines()`读取所有行到一个列表中。  

    可以使用一个程序接受用户输入的字符串作为将要读取的文件的文件名，并且在屏幕上打印文件内容。

    ```python
    #!/usr/bin/env python3
    name = input("Enter the file name: ")
    fobj = open(name)
    print(fobj.read())
    fobj.close()
    ```

- #### write()函数：

  可以使用`write()`函数打开一个文件然后写入一些文本。  

- #### sys模块：

  `sys.argv`包含了所有命令行参数。它的第一个值是命令本身的名字[0]。

- #### enumerate（iterableobject）函数：

  在序列中循环时，可以使用它同时得到索引位置和对应值。  

  *对任意给定文本文件中的制表符、行、空格进行计数。代码写入文件 `/home/shiyanlou/parsefile.py`：*

  ```python
  #!/usr/bin/env python3
  
  import os
  import sys
  ```

  def parse_file(path):
      """
      分析给定文本文件，返回其空格、制表符、行的相关信息

```
  :arg path: 要分析的文本文件的路径

  :return: 包含空格数、制表符数、行数的元组
  """
  fd = open(path)
  i = 0
  spaces = 0
  tabs = 0
  for i,line in enumerate(fd):
      spaces += line.count(' ')
      tabs += line.count('\t')
  # 现在关闭打开的文件
  fd.close()

  # 以元组形式返回结果
  return spaces, tabs, i + 1
```

  def main(path):
      """
      函数用于打印文件分析结果

```
  :arg path: 要分析的文本文件的路径
  :return: 若文件存在则为 True，否则 False
  """
  if os.path.exists(path):
      spaces, tabs, lines = parse_file(path)
      print("Spaces {}. tabs {}. lines {}".format(spaces, tabs, lines))
      return True
  else:
      return False
```

  if __name__ == '__main__':
      if len(sys.argv) > 1:
          main(sys.argv[1])
      else:
          sys.exit(-1)
      sys.exit(0)

```
* #### with语句：  

  尝试使用 `with` 语句处理文件对象，它会在文件用完后会自动关闭，就算发生异常也没关系。它是 try-finally 块的简写：

  ```python
  >>> with open('sample.txt') as fobj:
  ...     for line in fobj:
  ...         print(line, end = '')
  ... 
  I love Python
  I love shiyanlou
```

- 我们使用 `try...except` 块来处理任意异常。基本的语法像这样：

  ```python
  try:
      statements to be inside try clause
      statement2
      statement3
      ...
  except ExceptionName:
      statements to evaluated in case of ExceptionName happens
  ```

  它以如下方式工作：

  - 首先，执行 `try` 子句 （在 [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) 和 [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) 关键字之间的部分）。

  - 如果没有异常发生，`except` 子句 在 [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) 语句执行完毕后就被忽略了。

  - 如果在 `try` 子句执行过程中发生了异常，那么该子句其余的部分就会被忽略。

    如果异常匹配于 [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) 关键字后面指定的异常类型，就执行对应的 `except` 子句。然后继续执行 [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) 语句之后的代码。

  - 如果发生了一个异常，在 [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) 子句中没有与之匹配的分支，它就会传递到上一级 [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) 语句中。

    如果最终仍找不到对应的处理语句，它就成为一个 *未处理异常*，终止程序运行，显示提示信息。

- 使用 `raise` 语句抛出一个异常。

  ```python
  >>> raise ValueError("A value error happened.")
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: A value error happened.
  ```

  我们可以捕获任何其它普通异常一样，来捕获这些异常。

  ```python
  >>> try:
  ...     raise ValueError("A value error happened.")
  ... except ValueError:
  ...     print("ValueError in our code.")
  ...
  ValueError in our code.
  ```

- `try` 语句还有另一个可选的 `finally` 子句，目的在于定义在任何情况下都一定要执行的功能。例如:

  ```python
  >>> try:
  ...     raise KeyboardInterrupt
  ... finally:
  ...     print('Goodbye, world!')
  ...
  Goodbye, world!
  KeyboardInterrupt
  Traceback (most recent call last):
    File "<stdin>", line 2, in ?
  ```

  不管有没有发生异常，`finally` 子句 在程序离开 `try` 后都一定会被执行。当 `try` 语句中发生了未被 `except` 捕获的异常（或者它发生在 `except` 或 `else` 子句中），在 `finally`子句执行完后它会被重新抛出。

  在真实场景的应用程序中，`finally` 子句用于释放外部资源（文件或网络连接之类的），无论它们的使用过程中是否出错。

  ### python类：

  - 在写你的第一个类之前，你应该知道它的语法。我们以下面这种方式定义类：

    ```python
    class nameoftheclass(parent_class):
        statement1
        statement2
        statement3
    ```

    在类的声明中你可以写任何 Python 语句，包括定义函数（在类中我们称为方法）。

    ```python
    >>> class MyClass(object):
    ...     """A simple example class"""
    ...     i = 12345
    ...     def f(self):
    ...         return 'hello world'
    ```

- 类的实例化使用函数符号。只要将类对象看作是一个返回新的类实例的无参数函数即可。例如（假设沿用前面的类）:

  ```python
  x = MyClass()
  ```

  以上创建了一个新的类实例并将该对象赋给局部变量 `x`。

  这个实例化操作创建一个空的对象。很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 `__init__()` 的特殊方法，像下面这样:

  ```python
  def __init__(self):
      self.data = []
  ```

  类定义了 `__init__()` 方法的话，类的实例化操作会自动为新创建的类实例调用 `__init__()` 方法。所以在下例中，可以这样创建一个新的实例:

  ```python
  x = MyClass()
  ```

  当然，出于弹性的需要，`__init__()` 方法可以有参数。事实上，参数通过`__init__()` 传递到类的实例化操作上。例如：

  ```python
  >>> class Complex:
  ...     def __init__(self, realpart, imagpart):
  ...         self.r = realpart
  ...         self.i = imagpart
  ...
  >>> x = Complex(3.0, -4.5)
  >>> x.r, x.i
  (3.0, -4.5)
  ```

- 当一个类继承另一个类时，它将继承父类的所有功能（如变量和方法）。这有助于重用代码。

在下一个例子中我们首先创建一个叫做 `Person` 的类，然后创建两个派生类 `Student` 和 `Teacher`。当两个类都从 `Person` 类继承时，它们的类除了会有 `Person` 类的所有方法还会有自身用途的新方法和新变量。

#### 2.3.1 student_teacher.py

代码写入文件 `/home/shiyanlou/student_teacher.py`：

```python
#!/usr/bin/env python3

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
```

 一个类可以继承自多个类，具有父类的所有变量和方法，语法如下：

```python
class MyClass(Parentclass1, Parentclass2,...):
    def __init__(self):
        Parentclass1.__init__(self)
        Parentclass2.__init__(self)
        ...
        ...
```

- 现在我们已经知道怎样创建对象，现在我们来看看怎样删除一个对象。我们使用关键字 `del` 来做到这个。

```python
>>> s = "I love you"
>>> del s
>>> s
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 's' is not defined
```

`del` 实际上使对象的引用计数减少一，当对象的引用计数变成零的时候，垃圾回收器会删除这个对象。

- 在 Python 里请不要使用属性（*attributes*）读取方法（*getters*和 *setters*）。如果你之前学过其它语言（比如 Java），你可能会想要在你的类里面定义属性读取方法。请不要这样做，直接使用属性就可以了，就像下面这样：

```python
>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...
>>> std = Student("Kushal Das")
>>> print(std.name)
Kushal Das
>>> std.name = "Python"
>>> print(std.name)
Python
```

- 你可能想要更精确的调整控制属性访问权限，你可以使用 `@property` 装饰器，`@property` 装饰器就是负责把一个方法变成属性调用的。

下面有个银行账号的例子，我们要确保没人能设置金额为负，并且有个只读属性 cny 返回换算人名币后的金额。

代码写入文件 `/home/shiyanlou/property.py`

```python
#!/usr/bin/env python3

class Account(object):
    """账号类,
    amount 是美元金额.
    """
    def __init__(self, rate):
        self.__amt = 0
        self.rate = rate

    @property
    def amount(self):
        """账号余额（美元）"""
        return self.__amt

    @property
    def cny(self):
        """账号余额（人名币）"""
        return self.__amt * self.rate

    @amount.setter
    def amount(self, value):
        if value < 0:
            print("Sorry, no negative amount in the account.")
            return
        self.__amt = value

if __name__ == '__main__':
    acc = Account(rate=6.6) # 基于课程编写时的汇率
    acc.amount = 20
    print("Dollar amount:", acc.amount)
    print("In CNY:", acc.cny)
    acc.amount = -100
    print("Dollar amount:", acc.amount)
```

- #### 模块：

  模块是包括Python定义和声明的文件。文件名就是模块名加上`.py`后缀。

你可以由全局变量 `__name__` 得到模块的模块名（一个字符串）。

现在我们来看看模块是怎样工作的。创建一个 `bars.py` 文件。文件内容如下：

```python
"""
Bars Module
============
这是一个打印不同分割线的示例模块
"""
def starbar(num):
    """打印 * 分割线

    :arg num: 线长
    """
    print('*' * num)

def hashbar(num):
    """打印 # 分割线

    :arg num: 线长
    """
    print('#' * num)

def simplebar(num):
    """打印 - 分割线

    :arg num: 线长
    """
    print('-' * num)
```

现在我们启动解释器然后导入我们的模块。

```python
>>> import bars
>>>
```

我们必须使用模块名来访问模块内的函数。

```python
>>> bars.hashbar(10)
##########
>>> bars.simplebar(10)
----------
>>> bars.starbar(10)
**********
```

- 导入模块

有不同的方式导入模块。我们已经看到过一种了。你甚至可以从模块中导入指定的函数。这样做：

```python
>>> from bars import simplebar, starbar
>>> simplebar(20)
--------------------
```

你也可以使用 `from module import *` 导入模块中的所有定义，然而这并不是推荐的做法。

- #### 包：

  含有 `__init__.py` 文件的目录可以用来作为一个包，目录里的所有 `.py` 文件都是这个包的子模块。  

  `mymodule` 是一个包名并且 `bars` 和 `utils` 是里面的两个子模块。

  首先创建 mymodule 目录：

  ```python
  $ cd /home/shiyanlou
  $ mkdir mymodule
  ```

  然后将上一节编写的 `bars.py` 拷贝到 mymodule 目录下，然后可以使用 `touch` 创建一个 `utils.py` 文件。

  使用 `touch` 命令创建一个空的 `__init__.py` 文件。

  ```python
  $ touch mymodule/__init__.py
  ```

  如果 `__init__.py` 文件内有一个名为 `__all__` 的列表，那么只有在列表内列出的名字将会被公开。

  因此如果 `mymodule` 内的 `__init__.py` 文件含有以下内容：

  ```python
  from mymodule.bars import simplebar
  __all__ = [simplebar, ]
  ```

  那么导入时将只有 `simplebar` 可用。

  `from mymodule import *` 只能工作在模块级别的对象上，试图导入函数或类将导致 syntax error。

  - #### os模块：

    [`os`](http://docs.python.org/3/library/os.html#module-os) 模块提供了与操作系统相关的功能。你可以使用如下语句导入它：

    ```python
    >>> import os
    ```

    `getuid()` 函数返回当前进程的有效用户 id。

    ```python
    >>> os.getuid()
    500
    ```

    `getpid()` 函数返回当前进程的 id。`getppid()` 返回父进程的 id。

    ```python
    >>> os.getpid()
    16150
    >>> os.getppid()
    14847
    ```

    `uname()` 函数返回识别操作系统的不同信息，在 Linux 中它返回的详细信息可以从 `uname -a` 命令得到。`uname()` 返回的对象是一个元组，`（sysname, nodename, release, version, machine）`。

    ```python
    >>> os.uname()
    ('Linux', 'd80', '2.6.34.7-56.fc13.i686.PAE', '#1 SMP Wed Sep 15 03:27:15 UTC 2010', 'i686')
    ```

    getcwd() 函数返回当前工作目录。`chdir(path)` 则是更改当前目录到 path。在例子中我们首先看到当前工作目录是 `/home/shiyanlou`，然后我们更改当前工作目录到 `/Code` 并再一次查看当前工作目录。

    ```python
    >>> os.getcwd()
    '/home/shiyanlou'
    >>> os.chdir('Code')
    >>> os.getcwd()
    '/home/shiyanlou/Code'
    ```

    所以现在让我们使用 os 模块提供的另一个函数来创建一个自己的函数，它将列出给定目录下的所有文件和目录。

    ```python
    def view_dir(path='.'):
        """
        这个函数打印给定目录中的所有文件和目录
        :args path: 指定目录，默认为当前目录
        """
        names = os.listdir(path)
        names.sort()
        for name in names:
            print(name, end =' ')
        print()
    ```

    使用例子中的 `view_dir()` 函数。

    ```python
    >>> view_dir('/')
    .bashrc .dockerenv .profile bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var
    ```

- #### Request模块：

  [Requests](http://docs.python-requests.org/zh_CN/latest/) 是一个第三方 Python 模块，其官网的介绍如下：

  > Requests 唯一的一个**非转基因**的 Python HTTP 库，人类可以安全享用。
  >
  > **警告**：非专业使用其他 HTTP 库会导致危险的副作用，包括：安全缺陷症、冗余代码症、重新发明轮子症、啃文档症、抑郁、头疼、甚至死亡。

  第三方模块并不是默认的模块，意味着你需要安装它，我们使用 `pip3` 安装它。

  首先要安装 `pip3`：

  ```python
  $ sudo apt-get update
  $ sudo apt-get install python3-pip
  ```

  然后用 `pip3` 安装 `requests`

  ```python
  $ sudo pip3 install requests
  ```

  上面的命令会在你的系统中安装 Python3 版本的 Requests 模块。

  #### 4.2.1 获得一个简单的网页

  你可以使用 `get()` 方法获取任意一个网页。

  ```python
  >>> import requests
  >>> req = requests.get('https://github.com')
  >>> req.status_code
  200
  ```

  `req` 的 `text` 属性存有服务器返回的 HTML 网页，由于 HTML 文本太长就不在这里贴出来了。

  使用这个知识，让我们写一个能够从指定的 URL 中下载文件的程序。

  代码写入文件 `/home/shiyanlou/download.py`：

  ```python
  #!/usr/bin/env python3
  import os
  import os.path
  import requests
  
  def download(url):
      '''从指定的 URL 中下载文件并存储到当前目录
  
      :arg url: 要下载的文件的 URL
      '''
      req = requests.get(url)
      # 首先我们检查是否存在文件
      if req.status_code == 404:
          print('No such file found at %s' % url)
          return
      filename = url.split('/')[-1]
      with open(filename, 'wb') as fobj:
          fobj.write(req.content)
      print("Download over.")
  
  if __name__ == '__main__':
      url = input('Enter a URL: ')
      download(url)
  ```

可以看到目录下已经多了一个 sample.txt 文件。

你可能已经注意到了 `if __name__ == '__main__':` 这条语句，它的作用是，只有在当前模块名为 `__main__` 的时候（即作为脚本执行的时候）才会执行此 `if` 块内的语句。换句话说，当此文件以模块的形式导入到其它文件中时，`if` 块内的语句并不会执行。

你可以将上面的程序修改的更友好些。举个例子，你可以检查当前目录是否已存在相同的文件名。[os.path](http://docs.python.org/3/library/os.path.html#module-os.path) 模块可以帮助你完成这个。**使用`os.path.exist(path)`来判断是否存在相同的文件名或目录。**  

- #### `argparse`命令行参数处理模块：

  可以传递不同的选项作为命令行参数。

  这里是用到的模块是 `sys`，命令行传入的所有参数都可以使用 `sys.argv` 获取。如果希望对参数进行处理可以使用 `argparse` 模块，阅读这篇 [文档](https://docs.python.org/3/howto/argparse.html) 学习。 

- #### `tab`补全：

  首先创建一个文件：`~/.pythonrc` ，文件内写入如下内容：

  ```python
  import rlcompleter, readline
  readline.parse_and_bind('tab: complete')
  ```

  history_file = os.path.expanduser('~/.python_history')
  readline.read_history_file(history_file)

  import atexit
  atexit.register(readline.write_history_file, history_file)

```
  下一步在 `~/.bashrc` 文件中设置 PYTHONSTARTUP 环境变量指向这个文件：

  ```python
  $ export PYTHONSTARTUP=~/.pythonrc

```

  现在，从今以后每当你打开 bash shell，你将会有 TAB 补全和 Python 解释器中代码输入的历史记录。

  要在当前 shell 中使用，source 这个 bashrc 文件。

```python
  $ source ~/.bashrc
```

- #### `counter`模块：

  在这个实验我们会学习 `Collections` 模块。这个模块实现了一些很好的数据结构，它们能帮助你解决各种实际问题。

  ```python
  >>> import collections
  ```

  这是如何导入这个模块，现在我们来看看其中的一些类。

  `Counter` 是一个有助于 *hashable* 对象计数的 dict 子类。它是一个无序的集合，其中 *hashable* 对象的元素存储为字典的键，它们的计数存储为字典的值，计数可以为任意整数，包括零和负数。

  我们可以这样查看 `Counter` 的帮助信息，事实上这些信息来源于 Counter 的文档字符串（`collections.Counter.__doc__`）。

下面我们来看一个例子，例子中我们查看 Python 的 LICENSE 文件中某些单词出现的次数。

#### Counter 示例

```python
>>> from collections import Counter
>>> import re
>>> path = '/usr/lib/python3.4/LICENSE.txt'
>>> words = re.findall('\w+', open(path).read().lower())
>>> Counter(words).most_common(10)
[('the', 80), ('or', 78), ('1', 66), ('of', 61), ('to', 50), ('and', 48), ('python', 46), ('in', 38), ('license', 37), ('any', 37)]
```

Counter 对象有一个叫做 `elements()` 的方法，其返回的序列中，依照计数重复元素相同次数，元素顺序是无序的。

```python
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> list(c.elements())
['b','b','a', 'a', 'a', 'a']
```

`most_common()` 方法返回最常见的元素及其计数，顺序为最常见到最少。

```python
>>> Counter('abracadabra').most_common(3)
[('a', 5), ('r', 2), ('b', 2)]
```

- #### `defaultdict`：

  `defaultdict` 是内建 `dict` 类的子类，它覆写了一个方法并添加了一个可写的实例变量。其余功能与字典相同。

  `defaultdict()` 第一个参数提供了 `default_factory` 属性的初始值，默认值为 `None`，`default_factory` 属性值将作为字典的默认数据类型。所有剩余的参数与字典的构造方法相同，包括关键字参数。

  同样的功能使用 `defaultdict` 比使用 `dict.setdefault` 方法快。

  **defaultdict 用例**

  ```python
  >>> from collections import defaultdict
  >>> s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
  >>> d = defaultdict(list)
  >>> for k, v in s:
  ...     d[k].append(v)
  ...
  >>> d.items()
  dict_items([('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])])
  ```

  在例子中你可以看到，即使 `defaultdict` 对象不存在某个*键*，它会自动创建一个空列表。  

  - #### `namedtuple`

    命名元组有助于对元组每个位置赋予意义，并且让我们的代码有更好的可读性和自文档性。你可以在任何使用元组地方使用命名元组。在例子中我们会创建一个命名元组以展示为元组每个位置保存信息。

    ```python
    >>> from collections import namedtuple
    >>> Point = namedtuple('Point', ['x', 'y'])  # 定义命名元组
    >>> p = Point(10, y=20)  # 创建一个对象
    >>> p
    Point(x=10, y=20)
    >>> p.x + p.y
    30
    >>> p[0] + p[1]  # 像普通元组那样访问元素
    30
    >>> x, y = p     # 元组拆封
    >>> x
    10
    >>> y
    20
    ```

### 类挑战实验：  

## 介绍

我们之前通过3个课程学习了 Python 的类，模块和Collection 模块的知识。这次我们通过一个简单的挑战实验来测试一下我们对之前知识点的掌握程度。

## 目标

**改写**我们在第11节`类`这个模块当中 2.3 继承 部分的 `student_teacher.py` 脚本，在Person()类中增添函数`get_grade()`。对于教师类，该函数可以自动统计出老师班上学生的得分情况并按照频率的高低以`A: X, B: X, C: X, D: X` 的形式打印出来。对于学生类，该函数则可以以`Pass: X, Fail: X` 来统计自己的成绩情况（A,B,C 为 Pass, 如果得了 D 就认为是 Fail）。

`student_teacher.py` 文件可以通过在Xfce 终端中输入如下代码来获取

```
wget http://labfile.oss.aliyuncs.com/courses/790/student_teacher.py
```

要求

- 请把最终的`student_teacher.py` 代码文件放在 `/home/shiyanlou/Code/` 路径下
- 根据命令行中的第一个参数 `teacher` 或者 `student` 来判断最终输出的格式。
- 命令行中第二个输入的参数是需要统计的字符串

举例： ![此处输入图片的描述](wm-1534567224412.png)

## 提示语

- `import sys`
- `collections` 中的 `Counter` 子类
- `format()` 以及 `join`

## 知识点

- 类
- Collection 模块
- 注意最终的打印形式

![1534566729042](1534566729042.png)![1534567208350](1534567208350.png)