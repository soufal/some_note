#coding=utf-8
#!/usr/bin/python3 
import os,sys 
def check_ip(ipAddr): 
       import sys 
       addr=ipAddr.strip().split('.')  #切割IP地址为一个列表 
       #print addr 
       if len(addr) != 4:  #切割后列表必须有4个参数 
               print "check ip address failed!"
               sys.exit() 
       for i in range(4): 
               try: 
                       addr[i]=int(addr[i])  #每个参数必须为数字，否则校验失败 
               except: 
                       print "check ip address failed!"
                       sys.exit() 
               if addr[i]<=255 and addr[i]>=0:    #每个参数值必须在0-255之间 
                       pass
               else: 
                       print "check ip address failed!"
                       sys.exit() 
               i+=1
       else: 
               print "check ip address success!"
if  len(sys.argv)!=2:  #传参加本身长度必须为2 
       print "Example: %s 10.0.0.1 "%sys.argv[0] 
       sys.exit() 
else: 
       check_ip(sys.argv[1])  #满足条件调用校验IP函数