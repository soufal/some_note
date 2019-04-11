
# 运算符优先
ops_rule = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}
 
def middle_to_after(s):
    """中缀表达式变为后缀表达式"""
    expression = []
    ops = []
    for item in s:
        # 当遇到运算符
        if item in ['+', '-', '*', '/',"^"]:
            while len(ops) >= 0:
                # 如果栈中没有运算符，直接将运算符添加到后缀表达式
                if len(ops) == 0:
                    ops.append(item)
                    break
                # 如果栈中有运算符
                op = ops.pop()
                # 如果栈顶的运算符比当前运算符级别低，当前运算符入栈
                if op == '(' or ops_rule[item] > ops_rule[op]:
                    ops.append(op)
                    ops.append(item)
                    break
                else:
                    # 如果栈顶的运算符比当前运算符级别高，将栈顶运算符加入到表达式
                    # 当前运算符与栈中后面的运算符比较
                    expression.append(op)
        # 遇到左括号入栈
        elif item == '(':
            ops.append(item)
        # 遇到右括号，将栈中运算符加入到表达式直到遇到左括号
        elif item == ')':
            while len(ops) > 0:
                op = ops.pop()
                if op == '(':
                    break
                else:
                    expression.append(op)
        # 遇到运算数，添加到表达式
        else:
            expression.append(item)
    # 最好将栈中全部运算符加到后缀表达式中
    while len(ops) > 0:
        expression.append(ops.pop())
 
    return expression
 
 
def expression_to_value(expression):
    """后缀表达式计算"""
    stack_value = []
    for item in expression:
        if item in ['+', '-', '*', '/','^']:
            n2 = stack_value.pop()
            n1 = stack_value.pop()
            result = cal(n1, n2, item)
            stack_value.append(result)
        else:
            stack_value.append(int(item))
    return stack_value[0]
 
 
# 计算函数
def cal(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        return n1 // n2
    if op == '^':
        return n1**n2
 
 
if __name__ == '__main__':
    exp = input().split()
    expression = middle_to_after(exp)
    value = expression_to_value(expression)
    print(value)

