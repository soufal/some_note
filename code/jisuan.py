#!/usr/bin/env python3
#coding=utf-8
import os 
while True: 
    dynamic = input('输入计算表达式：') 
    if dynamic != 'cls': 
        try: 
            result = eval(dynamic.lstrip().rstrip("=")) 
            print('计算结果：'+str(result)) 
        except: 
            print('计算表达式输入有误！') 
    else: 
        command = 'cls' 
        os.system(command)
