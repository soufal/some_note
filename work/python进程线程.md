
小姐姐。进程和线程是什么啊



进程是程序执行的最小单元，每个进程**都有自己独立的内存空间**，而线程是进程的一个实体，是系统调用调用的一个基本单位。

举个栗子吧：

我们启动一个app 这就创建了一个进程，这个app里可能有语音播放、搜索等功能，这些是进程里不同的线程。

注意：线程是轻量级的，他没有独立的空间地址(内存空间)，因为他是由进程创建的，寄存在进程的内存地址中。**一个进程会包含多个线程**(这就是我们今天说的多线程)



![img](https://mmbiz.qpic.cn/mmbiz_png/Kg0ClEKGI5kbLH158qD5s2qXerXwXXpJ25t4O9PuP8VGSTJiaMNe72ibojiaGAUKeQhibHfLia6UQBQyyjiau0DSjnicw/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![img](https://mmbiz.qpic.cn/mmbiz_jpg/Kg0ClEKGI5kbLH158qD5s2qXerXwXXpJxluxqqSo4Um0sicV5co4HiapUNZu6vKJsjDUX9shibq87icNDt9qmLyG5w/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



我们先了解一下线程的5种状态：

**1、新建状态：**

    当一个线程被创建时就开始了它的生命周期，在启动线程之前他一直处于新建状态。

**2、就绪状态：**

    当线程被启动时，由于还没有分配到cpu资源，该线程进入等待队列在等待另一个线程执行完(等待cpu服务)，此时线程被称为就绪状态。

**3、运行状态：**

    当处于就绪状态的线程被调用并获得cpu资源时，此时为运行状态。

**4、阻塞状态：**

    一个正在执行的线程在某些情况下不得已让出cpu资源时，会中止自己的执行过程，这是被称为阻塞状态。值得注意的是：阻塞被消除后是回到就绪状态，不是运行状态。

**5、死亡状态：**

    线程被终止、销毁、或执行完毕则进入死亡状态。不可再重新启动







**阻塞状态的分类**

阻塞状态又分为三种情况：等待阻塞、同步阻塞、其他阻塞

说到阻塞不得不提到一个‘锁’的概念





多线程可以运行多个任务，很大程度上提高了我们程序的工作效率，但是面临一个非常致命的问题。如果有多个线程去操作同一个列表(这个列表被称为：共享数据)，比如线程a要列表第一个元素的值加1，这个过程可以细分为3步：1.取出元素；2：元素加1；3：将最终的结果放入列表。那如果在a线程执行到第二步加1的时候线程b突然要读取列表 那么他读取到的列表仍然是没修改之前的内容。这并不是我们想要的

所以引进了锁的概念。当某个线程需要独占共享资源时，必须先上锁，这样别的线程就无法再操作。当操作完之后一定要将锁打开，别的线程才可以操作数据。

在I/O密集型操作中，需要保持数据同步的时候需要加锁 保证资源同步。但同时因为其他线程面临阻塞，性能不可避免的会下降。

同步阻塞：线程请求锁定的时候进入同步阻塞，一旦获得锁又变成运行状态。



等待阻塞：是指等待其他线程通知的状态，线程获得条件锁定后，调用“等待”将进入这个状态，一旦其他线程发出通知，线程将进入同步状态，再次竞争条件锁定。



其他阻塞：指线程sleep 、join或等待io时的阻塞。







下面我们创建一个简单的多线程

 python3.x中提供了两种创建线程的方式：

 _thread.start_new_thread()

 threading.Thread()

```
import _thread
import threading
import time

def my_thread(threadName):
   for i in range(10):
       print(' 线程 :' + threadName + '正在执行')

# 启动线程
# 方法名  方法参数，无参时空tuple
# _thread.start_new_thread()
t1 = threading.Thread(target=my_thread, args=('name1',))
t2 = threading.Thread(target=my_thread, args=('name2',))

## t1 = _thread.start_new_thread(my_thread, ('name1',))
# t2 = _thread.start_new_thread(my_thread, ('name2',))

# 通过start方法 启动线程
t1.start()
t2.start()
```



从控制台打印的结果来看 t1线程和t2线程无规律的交错打印。这正是两个线程之间抢占cpu资源的结果。



下面我们模拟多窗口出售电影票的场景来理解阻塞和锁

```
import threading
# 库存电影票数量,为了使结果更加准确设置成10w
num = 100000
def thread(name):
   global num
   while num > 0:
       num -= 1
       print('%s出售 1 张电影票 === 剩余 %d 张电影票' % (name, num))

# 三种售票途径
businesses = ['美团', '淘票', '糯米']
for i in businesses:
   # 创建线程
   t = threading.Thread(target=thread, args=(i,))
   # 启动线程
   t.start()
```



通过多次运行代码、发现控制台打印的结果有时候明明两个窗口都售出去一张票了，但余票数量相等。更明显的是明明美团窗口显示余票已经为0了，但是另外两个窗口还是有很多剩余电影票 如下图：

![img](https://mmbiz.qpic.cn/mmbiz_png/Kg0ClEKGI5kbLH158qD5s2qXerXwXXpJANQDPZf0CPBYF6LWQSWiaKxqdvBPWwsy55vDXtU6zNq2LLb45tqBREQ/640?tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

通过分析控制台记录我们会发现，美团售票窗口一次性卖了好几百张票，糯米和淘票窗口的数据一直没有更新成最新的库存，导致明明没票了，缺还显示剩余很多。

不仅仅是售票，生活中有很多这样的例子，比如抢购火车票，银行取钱等...都会有这种数据不同步的问题。解决这一问题的办法就是前面提到的‘锁’。

简单的讲美团在卖票的过程中，将库存进行锁定，在这期间糯米和淘票票不可以在操作，只能等待美团操作完将数据更新后，然后释放锁才可以继续操作。

在threading模块中提供了一个获得线程锁的方法:

threading.Lock()



SHOW CODING!!!

```
import threading
# 库存电影票数量,为了使结果更加准确设置成10w
num = 100000
lock = threading.Lock()
def thread(name):
   global num
   while num > 0:
       # 加锁  这里一定要放在判断总量之前，
       # 不然会导致另外两个窗口最后会出现负数票的情况
       # 如果没有加锁就释放锁会导致报错，所以在while循环里又加了一层if判断
       lock.acquire()
       if num > 0:
           num -= 1
           print('%s出售 1 张电影票 === 剩余 %d 张电影票' % (name, num))
           # 释放锁
           lock.release()
       else:
           lock.release()

# 三种售票途径
businesses = ['美团', '淘票', '糯米']
for i in businesses:
   # 创建线程
   t = threading.Thread(target=thread, args=(i,))
   # 启动线程
   t.start()
```

在运行时我们发现，无论执行代码多少次，最终票数为0时，所有窗口都停止售票了。这个例子很完美的阐述了阻塞和锁在多线程中的重要性！！！

大家在开发过程中，使用多线程也要多加注意，避免不必要的错误发生







其他常用方法



▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼

**1、threading.Rlock()**

        RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，必须调用n次的release才能真正释放所占用的琐。



2、threading.Condition()

        可以把Condiftion理解为一把高级的琐，它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题。threadiong.Condition在内部维护一个琐对象（默认是RLock），可以在创建Condigtion对象的时候把琐对象作为参数传入。Condition也提供了acquire, release方法，其含义与琐的acquire, release方法一致，其实它只是简单的调用内部琐对象的对应的方法而已。Condition还提供wait方法、notify方法、notifyAll方法(特别要注意：这些方法只有在占用琐(acquire)之后才能调用，否则将会报RuntimeError异常)





**3、threading.Semaphore和BoundedSemaphore**



        Semaphore：Semaphore 在内部管理着一个计数器。调用 acquire() 会使这个计数器 -1，release() 则是+1(可以多次release()，所以计数器的值理论上可以无限).计数器的值永远不会小于 0，当计数器到 0 时，再调用 acquire() 就会阻塞，直到其他线程来调用release()



4、join()

       

 如果一个线程在执行过程中要调用另外一个线程，并且等到其完成以后才能接着执行



```
def my_thread(threadName):
  for i in range(10):
      print(' 线程 :' + threadName + '正在执行')

# 启动线程
# 方法名  方法参数，无参时空tuple
# _thread.start_new_thread()
t1 = threading.Thread(target=my_thread, args=('name1',))
t2 = threading.Thread(target=my_thread, args=('name2',))

## t1 = _thread.start_new_thread(my_thread, ('name1',))
# t2 = _thread.start_new_thread(my_thread, ('name2',))

# 通过start方法 启动线程
t1.start()
t2.start()
# 如果不加join 则Ending会在t1和t2没有执行完就会打印
# 加了join之后 Ending会等待线程执行完毕之后才会打印
t1.join()
t2.join()
print("Ending 。。。。。")
```





**5、isAlive**

        isAlive 等价于 is_alive(self)，用于判断线程是否运行。当线程没有调用start时，或者线程执行完毕处于死亡状态，isAlive()返回false。

```
# False
print(t1.isAlive())
t1.start()
# True
print(t1.is_alive())
```





**6、Daemon**

        Python主程序当且仅当不存在非Daemon线程存活时退出。即:主程序等待所有非Daemon线程结束后才退出，且退出时会自动结束（很粗鲁的结束）所有Daemon线程。

```
t1 = threading.Thread(target=thread_run, args=('jone', ), daemon= True)
t1.setDaemon(True)
```



**7、name**



```
t1.setName('i am a thread')
# i am a thread
print(t1.getName())
```