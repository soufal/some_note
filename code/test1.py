def validBraces(string):
  result = []
  for i in string:
      if i in "({[":
          result.append(i)
      elif len(result) != 0:
          if (i == ')') & (result[-1] == '('):
              result.pop()
          elif (i == '}') & (result[-1] == '{'):
              result.pop()
          elif result[-1] == '[':
              result.pop()
      elif i not in "(){}[]":
          continue
      else:
          return False
      
  if len(result) == 0:
      return True
  else:
      return False

print(validBraces("ttt(test()"))
