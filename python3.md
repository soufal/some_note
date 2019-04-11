# python3

## `math()`模块：

* `round()` 方法返回浮点数`x` 的四舍五入值。  

  ```python
  round( x, n)
  #x--数学表达式
  #n---表示从小数点位数，默认为0.
  ```

  from math import ceil, log, sqrt
  def isPP(n):
  for b in xrange(2, int(sqrt(n)) + 1):
  e = int(round(log(n, b)))
  if b ** e == n:
  return [b, e]
  return None

## `re`模块：  

Python通过re模块提供对正则表达式的支持。使用re的一般步骤是先将正则表达式的字符串形式编译为Pattern实例，然后使用Pattern实例处理文本并获得匹配结果

**常用的re函数：**

| 方法/属性                                       | 作用                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ |
| re.match(pattern, string, flags=0)              | **一次匹配的结果**。从字符串的起始位置匹配，如果起始位置匹配不成功的话，match()就返回none |
| re.search(pattern, string, flags=0)             | 扫描整个字符串并返回第一个成功的匹配                         |
| re.findall(pattern, string, flags=0)            | 找到RE匹配的所有字符串，并把他们作为一个列表返回             |
| re.finditer(pattern, string, flags=0)           | 找到RE匹配的所有字符串，并把他们作为一个迭代器返回           |
| re.sub(pattern, repl, string, count=0, flags=0) | 替换匹配到的字符串                                           |

函数参数说明：

pattern:匹配的正则表达式

string：要匹配的字符串

flags：标记为，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

repl：替换的字符串，也可作为一个函数

count：模式匹配后替换的最大次数，默认0表示替换所有匹配

**常用的正则表达式**

![pyre](https://images.cnblogs.com/cnblogs_com/huxi/Windows-Live-Writer/Python_10A67/pyre_ebb9ce1c-e5e8-4219-a8ae-7ee620d5f9f1.png)

**获取匹配的函数**：

| 方法/属性    | 作用                                                         |
| ------------ | ------------------------------------------------------------ |
| group(num=0) | 匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。 |
| groups()     | 返回包含所有小组字符串的元组，从1到所含的小组                |
| groupdict()  | 返回以有别名的组的别名为键、以该组截获的子串为值的字典       |
| start()      | 返回匹配开始的位置                                           |
| end()        | 返回匹配结束的位置                                           |
| span()       | 返回一个元组包含匹配（开始，结束）的位置                     |

* Python中数量词默认是贪婪的。 总是尝试匹配尽可能多的字符；非贪婪的则相反，总是尝试匹配尽可能少的字符。例如：正则表达式"ab*"如果用于查找"abbbc"，将找到"abbb"。而如果使用非贪婪的数量词"ab*?"，将找到"a"。 

### Pattern

Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。

Pattern不能直接实例化，必须使用re.compile()进行构造。

Pattern提供了几个可读属性用于获取表达式的相关信息：

1. pattern: 编译时用的表达式字符串。 
2. flags: 编译时用的匹配模式。数字形式。 
3. groups: 表达式中分组的数量。 
4. groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。

![img](https://images2015.cnblogs.com/blog/1036857/201705/1036857-20170529203214461-666088398.png)

> ```python
> 
> print(re.findall('a\\c','a\c')) #对于正则来说a\\c确实可以匹配到a\c,但是在python解释器读取a\\c时，会发生转义，然后交给re去执行，所以抛出异常
> print(re.findall(r'a\\c','a\c')) #r代表告诉解释器使用rawstring，即原生字符串，把我们正则内的所有符号都当普通字符处理，不要转义
> print(re.findall('a\\\\c','a\c')) #同上面的意思一样，和上面的结果一样都是['a\\c']
> ```

**总结:  尽量使用泛匹配模式.*  尽量使用非贪婪模式:.*?  使用括号得到匹配目标:用group(n)去取得结果  有换行符就用re.S:修改模式**

