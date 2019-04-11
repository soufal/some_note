#!/usr/bin/env python3
a=['a','b','a','c','a','c','b','d','e','c','a','c']
duixiang = set(a)
print(duixiang)
dict = {}
for i in duixiang:
    dict[i]=a.count(i)
a=sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(a)
