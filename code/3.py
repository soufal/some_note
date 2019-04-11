import sys
n = int(input())
strList = []
for line in sys.stdin:  
    tempStr = line.split()
    strList.extend(tempStr)
