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