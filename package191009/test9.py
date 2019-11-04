# 多线程

"""
线程可分为:
  <1>内核线程:由操作系统内核创建和撤销
  <2>用户线程:不需要内核支持而在用户程序中实现的线程

python3 线程中常用的两个模块为: _thread , threading(推荐使用)
注: thread 模块已被抛弃，用户可以使用 threading 模块代替，为了兼容性 thread 被重名为 _thread

python 中使用线程有两种方式:函数或者用类来包装线程对象

函数式:调用 thread 模块中的 start_new_thread() 函数来产生新线程
start_new_thread(function,args[,kwargs])
function()   线程函数
args         传递给线程函数的参数，它必须是 tuple 类型
kwargs       可选参数
"""
print("*****开始学习Python线程*****")
import _thread
import time


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("{}:{}".format(thread_name, time.ctime(time.time())))


# try:
#     _thread.start_new_thread(print_time, ("Thread-1", 1))
#     _thread.start_new_thread(print_time, ("Thread-2", 2))
# except():
#     print("Error: unable to start thread")
#
# time.sleep(14)
"""
_thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的
threading 提供的除包含 _thread 模块中的所有方法外的其它方法:
threading.currentThread() :返回当前的线程变量
threading.enumerate() :返回一个包含正在运行的线程的 list ，正在运行指线程启动后、结束前，不包括启动前和终止后的线程
threading.activeCount() :返回正在运行的线程数量，与 len(threading.enumerate()) 有相同的结果
除使用方法外，线程模块同样提供了 Thread 类来处理线程， Thread 类提供了以下方法:
run()          
start()        
join([time])   等待至线程终止。这阻塞调用线程直至线程的 join() 方法被调用中止-正常退出或者抛出
isAlive()      返回线程是否活动
getName()      返回线程名
setName()      设置线程名
"""
# 使用 threading 模块创建线程
# 通过直接从 threading.Thread 继承创建一个新的子类,并实例化后调用 start() 方法启动新线程,即调用了线程的 run() 方法
print("*****使用 threading 模块创建线程*****")
import threading
exitFlag = 0


class my_Thread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程:" + self.name)
        print_time(self.name, self.counter, 5)
        print("退出线程:" + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s:%s" % (threadName, time.ctime(time.time())))
        counter -= 1


# # 创建新线程
# thread3 = my_Thread(1, "Thread-3", 1)
# thread4 = my_Thread(2, "Thread-4", 2)
# # 开启新线程
# thread3.start()
# thread4.start()
# thread3.join()
# thread4.join()
# print("退出主线程")
# time.sleep(8)
"""
线程同步
如果多个线程共同对某一个数据修改,则可能出现不可预料的结果,为保证数据的正确性,需要多个线程进行同步
使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步,这两个对象都有 acquire 方法和 release 方法
对于那些需要每次只允许一个线程操作的数据,可以将其操作放到 acquire 和 release 方法之间
多线程的优势在于可以同时运行多个任务,但是当线程需要共享数据时,可能存在数据不同步的问题
考虑这一情况:一个列表里所有元素都是 0 ,线程"set"从后向前把所有元素改成 1 ,而线程"print"负责从前往后读取列表并打印
那么,可能线程"set"开始改的时候,线程"print"便来打印列表了,输出成了一半 0 一般 1 ,这就是数据的不同步
为了避免这种情况,引入了锁的概念
锁有两种状态---锁定和未锁定
每当一个线程比如"set"要访问共享数据时,必须先获得锁定
如果已经有别的线程比如"print"获得锁定了,那么就让线程"set"暂停,也就是同步阻塞
等到线程"print"访问完毕,释放锁以后,再让线程"set"继续
经过这样的处理,打印列表时要么全部输出 0 ,要么全部输出 1 ,不会出现一半 0 一半 1 的情况,
,,
"""
print("*****线程同步*****")
import threading
import time


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开启线程: " + self.name)
        # 获取锁,用于线程同步
        threadLock.acquire()
        print_time(self.name, self.counter, 3)  # 只允许一个线程访问
        # 释放锁,开启下一个线程
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# threadLock = threading.Lock()
# threads = []
#
# # 创建新线程
# thread5 = myThread(1, "Thread-5", 1)
# thread6 = myThread(2, "Thread-6", 2)
#
# # 开启新线程
# thread5.start()
# thread6.start()
# thread5.join()
# thread6.join()
# print("退出主线程")
# time.sleep(10)
"""
线程优先级排列
python 的 Queue 模块提供了同步的、线程安全的队列类,包括 FIFO(先入先出) 队列 Queue , LIFO(后入先出) 对列
和优先级队列 PriorityQueue
这些队列都实现了锁原理,能够在多线程中直接使用,可以使用队列来实现线程间的同步
Queue 模块中的常用方法
qsize()                 返回列的大小
empty()                 如果队列为空,返回 true ,否则返回 false
full()                  如果队列满了,返回 true ,否则返回 false
maxsize()               其大小与 full() 对应
get([block[,timeout])   获取队列, timeout 等待时间
get_nowait()            相当于 Queue.get(false)
put(item)               写入队列, timeout 等待时间 
put_nowait(item)        相当于Queue.put(item, false)
task_done()             在完成一项工作之后, Queue.task_done() 函数向任务已经完成的队列发送一个信号 
join()                  实际上意味着等到队列为空,再执行别的操作
"""
print("*****线程优先级排列*****")
import queue
import threading
import time

exitFlag = 0


class my_thread(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("开启线程:" + self.name)
        process_data(self.name, self.q)
        print("退出线程:" + self.name)


def process_data(threadName, q):
    while not exitFlag:  # 0 -> 1
        queueLock.acquire()
        if not workQueue.empty():  # 对列为空时返回 True ,否则返回 False , 215 行开始存入"资源"
            data = q.get()
            queueLock.release()
            print("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            pass
        time.sleep(1)


threadList = ["Thread-7", "Thread-8", "Thread-9"]  # 线程名
nameList = ["One", "Two", "Three", "Four", "Five"]  # 待提取"资源"
queueLock = threading.Lock()  # 实例化,加锁或解锁
workQueue = queue.Queue()  # 实例化,将"资源"存入对列或取出
threads = []  # 将多个线程存在列表中以便等待运行完成
threadID = 1  # 未使用,仅用于标记?

# 创建新线程
for tName in threadList:
    thread = my_thread(threadID, tName, workQueue)  # 为每个线程名创建一个线程
    thread.start()  # 运行线程
    threads.append(thread)  # 将线程存入列表中
    threadID += 1  # 标记

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print("退出主线程")
# 懵
