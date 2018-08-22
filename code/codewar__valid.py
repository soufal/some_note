def valid_parentheses(string):
    #your code here
    result = []
    for i in string:
        if i == '(':
            result.append(i)
        elif i == ')' and len(result) == 0:
            return False
        elif i == ')':
            result.pop()
            
    if len(result) == 0:
        return True
    else:
        return False

print(valid_parentheses(")test"))
