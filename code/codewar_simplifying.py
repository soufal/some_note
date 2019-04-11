import re
def simplify(poly):
    terms = {}
    ``` 将输入的多项式按照符号、数字、字母使用正则表达式将他们分割开来
	并对他们使用不同的方法进行处理：
	符号：如果符号为‘-’，则将其变为‘-1’，如果为‘+’，则赋值为‘1’	   数字：如果数字存在，则直接同符号相乘，如果不存在则使用1同符号相乘。
	字母：对每一组字符串进行排序。这里使用join，是因为排序后的结果是一个列表，而我们需要的是一个字符串。需要使用join将他们链接为一个字符串。
        构建一个字典terms，将字母作为keys，coef作为values想对应添加到字典中。这里在添加的同时使用了terms.get（）来判断某一个key，也就是某一个单项式字母是否已经存在于字典中了。如果存在就将他们相加。不存在则添加该值。
	最后对字典中的元素进行排序。使用两个key来进行排序：第一个是keys的长度从小到大排序，如果长度相同，则使用values进行排序，同样的按照从小到大的方式。
	这一系列操作过后，我们的字典中已经有了计算好的多项式的结果，现在需要将他们链接起来返回简化后的多项式。使用format_term函数来对每一个item进行映射。
        format_term()函数：对字典中的每一个item进行判断，如果item的values为0，则返回‘’也就是空，如果为1，则返回‘+’+ key。如果为-1，则返回‘-’+key，其他情况，则返回‘+’+ values + key。将每一个结果使用join链接起来就得到了最后的结果。并且需要移除头尾多出来的‘+’。

    ```
    for sign, coef, vars in re.findall(r'([\-+]?)(\d*)([a-z]*)', poly):
        sign = (-1 if sign == '-' else 1)
        coef = sign * int(coef or 1)
        vars = ''.join(sorted(vars))
        terms[vars] = terms.get(vars, 0) + coef
    # sort by no. of variables
    terms = sorted(terms.items(), key=lambda (v, c): (len(v), v))
    return ''.join(map(format_term, terms)).strip('+')

def format_term((vars, coef)):
    if coef == 0:
        return ''
    if coef == 1:
        return '+' + vars
    if coef == -1:
        return '-' + vars
    return '%+i%s' % (coef, vars)
