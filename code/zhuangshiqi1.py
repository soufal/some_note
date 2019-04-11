def outer(flag):
    def timer(func):
        def inner(*args,**kwargs):
            if flag:
                print('''执行函数之前要做的''')
            re = func(*args,**kwargs)
            if flag:
                print('''执行函数之后要做的''')
            return re
        return inner
    return timer

@outer
def func(False):
    print(111)

func()
