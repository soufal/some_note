num = list(input())
if num[0] != '-':
    num = num[::-1]
else:
    num = num[::-1]
    temp = num.pop()
    num.insert(0,temp)

if num == []:
    print('0')
else:
    print(int(''.join(num)))