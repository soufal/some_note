import time
def wrapper(func):
        def inner():
                start=time.time()
                func()
                end=time.time()
                print(end-start)
        return inner
@wrapper
def kkk():#相当于kkk=wrapper(kkk)
    print('aaaaa')
kkk()          
