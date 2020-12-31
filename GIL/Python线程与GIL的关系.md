# Python进程与GIL的关系

本人的电脑：win7，4核，python3.7

## 一、python与GIL

首先，我们想一下，如果有一个死循环在程序中进行，此时占用多少cpu资源呢？我们运行一下代码，查看其CPU使用率为多少？

```python
# -*- coding: utf-8 -*-

while True:
    pass

```

运行以上程序代码之后，他的cpu占用率大约在24%左右。并且cpu0是跑满的状态

![image-20201230155516004](imgs\image-20201230155516004.png)

那么，如果我们使用多线程，用三个线程一起跑这个代码，他的cpu占用率是否能达到60%呢？

```python
# -*- coding: utf-8 -*-
import threading


def diethre():
    while True:
        pass


t1 = threading.Thread(target=diethre)
t2 = threading.Thread(target=diethre)
t1.start()
t2.start()
while True:
    pass

```

我们可以看到，当前的线程数为3，但是他的cpu占用率始终在24%左右，并不是我们所预想的60%，并且cpu0和cpu2都处在50%的使用率（因为截图比较早，cpu1并没有上升到50%，可以看下一张图的前半部分就可以知道也是处在50%的）。那为什么会这样呢？这里就是GIL在作祟

![image-20201230155615569](imgs\image-20201230155615569.png)

在讲GIL之前我们先来看看多进程实现死循环的cpu占用率，来做个简单比较。

```python
# -*- coding: utf-8 -*-
import multiprocessing


def diemul():
    while True:
        pass


if __name__ == '__main__':
    m1 = multiprocessing.Process(target=diemul)
    m1.start()
    while True:
        pass

```

可以看出，当使用多进程之后，创建出一个新的进程，这两个进程基本上都是23%左右的cpu占用率，而且cpu的总占用率也来到了61%与之前大约是两倍左右，同时cpu0已经在跑满状态，cpu1也是快要跑满的情况。

![image-20201230155705155](imgs\image-20201230155705155.png)

## 二、GIL

我们先看一下官方对GIL的解释

```
In CPython, the global interpreter lock, or GIL, is a mutex that prevents multiple native threads from executing Python bytecodes at once. This lock is necessary mainly because CPython’s memory management is not thread-safe. (However, since the GIL exists, other features have grown to depend on the guarantees that it enforces.)
```

简单的一句话包含了很多信息；

a）在Python众多解释器中，只**有Cpython才有GIL**，JPython就没有；因为CPython是大部分环境下默认的Python执行环境。所以在很多人的概念里CPython就是Python，也就想当然的把`GIL`归结为Python语言的缺陷。**明确一点，GIL并不是Python的特性，它是在实现Python解析器(CPython)时所引入的一个概念，Python完全可以不依赖于GIL;**

**看一下CPython的源代码**

`static PyThread_type_lock interpreter_lock = 0; /* This is the GIL */`

这一行代码摘自 [ceval.c](https://github.com/python/cpython/blob/e62a694fee53ba7fc16d6afbaa53b373c878f300/Python/ceval.c#L238) —— CPython 2.7 解释器的源代码，Guido van Rossum 的注释”This is the GIL“ 添加于2003 年，但这个锁本身可以追溯到1997年他的第一个多线程 Python 解释器。在 Unix系统中，PyThread_type_lock 是标准 C  mutex_t 锁的别名。当 Python 解释器启动时它初始化：

```c
void PyEval_InitThreads(void)
{
    interpreter_lock = PyThread_allocate_lock();
    PyThread_acquire_lock(interpreter_lock);
}
```

**解释器中的所有 C 代码在执行 Python 时必须保持这个锁。**

**b）**GIL是一把互斥锁

Python代码的执行由Python虚拟机（也叫解释器主循环）来控制，而对Python虚拟机的访问由GIL（全局解释器锁）控制，**GIL保证了在任意时刻，只有一个线程在解释器中运行，就像单CPU系统运行多线程一样，内存中可以存放多个程序，但在任意时刻，只有一个线程在解释器中运行；**

**c）GIL是历史遗留问题，为了解决线程安全的简单粗暴做法**

多线程编程可以更有效地利用多核处理器，但是随之带来的就是线程间数据一致性和状态同步的困难（线程安全）；多核 CPU 在 1990 年代还属于类科幻，Guido van Rossum 在创造 python 的时候，也想不到他的语言有一天会被用到很可能 1000＋ 个核的 CPU 上面，**一个全局锁搞定多线程安全在那个时代应该是最简单经济的设计了**。简单而又能满足需求，那就是合适的设计（对设计来说，应该只有合适与否，而没有好与不好）。

**线程安全就是多线程访问时，采用了加锁机制，当一个线程访问该类的某个数据时，进行保护，其他线程不能进行访问直到该线程读取完，其他线程才可使用。不会出现数据不一致或者数据污染。 线程不安全就是不提供数据访问保护，有可能出现多个线程先后更改数据造成所得到的数据是脏数据。**

**d）GIL的执行机理**

**记住一个原则：“一个线程运行 Python ，而其他 N 个睡眠或者等待 I/O.”（One thread runs Python, while others sleep or await I/O）**

多线程环境中，python虚拟机按以下方式执行：

1. 设置GIL
2. 切换到一个线程去执行
3. 运行
   - 指定数量的字节码指令(python2为1000字节指令)或运行了执行时间（python3为15ms）---抢占式多任务处理
   - 线程主动让出控制（可以调用time.sleep(0)) -------协同式多任务处理
4. 把线程设置完睡眠状态
5. 解锁GIL
6. 再次重复以上步骤

对所有面向 I/O 的(会调用内建的操作系统 C 代码的)程序来说，**GIL 会在这个 I/O 调用之前被释放， 以允许其它的线程在这个线程等待 I/O 的时候运行**。 如果某线程并未使用很多 I/O 操作，它会在自己的时间片内一直占用处理器（和 GIL）。也就是说，**I/O 密集型（程序大量时间花费在等待I/O操作，CPU总是闲置，在10%左右（如：网络请求socket））的 Python 程序比计算密集型（程序线性执行，大量占用CPU，总是接近100%（如：正则匹配替换大量文本））的程序更能充分利用多线程环境的好处。**

**线程何时切换**？一个线程无论何时开始睡眠或等待网络 I/O，其他线程总有机会获取 GIL 执行 Python 代码。这是协同式多任务处理。CPython 也还有抢占式多任务处理。如果一个线程不间断地在 Python 2 中运行 1000 字节码指令，或者不间断地在 Python 3 运行15 毫秒，那么它便会放弃 GIL，而其他线程可以运行。把这想象成旧日有多个线程但只有一个 CPU 时的时间片。现在，将具体讨论这两种多任务处理。

## 三、协同式多任务处理

**当一项任务比如网络 I/O启动，而在长的或不确定的时间，没有运行任何 Python 代码的需要，一个线程便会让出GIL，从而其他线程可以获取 GIL 而运行 Python。这种礼貌行为称为协同式多任务处理**，它允许并发；多个线程同时等待不同事件。

也就是说两个线程各自分别连接一个套接字：

```python
def do_connect():
    s = socket.socket()
    s.connect(('python.org', 80))  # drop the GIL
 
for i in range(2):
    t = threading.Thread(target=do_connect)
    t.start()
```

两个线程在同一时刻只能有一个执行 Python ，但一旦线程开始连接，它就会放弃 GIL ，这样其他线程就可以运行。这意味着两个线程可以并发等待套接字连接，这是一件好事。在同样的时间内它们可以做更多的工作。

让我们打开盒子，看看一个线程在连接建立时实际是如何放弃 GIL 的，在 socketmodule.c 中:

```c
/* s.connect((host, port)) method */
static PyObject *
sock_connect(PySocketSockObject *s, PyObject *addro)
{
    sock_addr_t addrbuf;
    int addrlen;
    int res;
 
    /* convert (host, port) tuple to C address */
    getsockaddrarg(s, addro, SAS2SA(&addrbuf), &addrlen);
 
    Py_BEGIN_ALLOW_THREADS
    res = connect(s->sock_fd, addr, addrlen);
    Py_END_ALLOW_THREADS
 
    /* error handling and so on .... */
}
```

线程正是在Py_BEGIN_ALLOW_THREADS 宏处放弃 GIL；它被简单定义为：

```
PyThread_release_lock(interpreter_lock);
```

当然 Py_END_ALLOW_THREADS 重新获取锁。一个线程可能会在这个位置堵塞，等待另一个线程释放锁；一旦这种情况发生，等待的线程会抢夺回锁，并恢复执行你的Python代码。简而言之：当**N个线程在网络 I/O 堵塞，或等待重新获取GIL，而一个线程运行Python。**

## 四、抢占式多任务处理

Python线程可以主动释放 GIL，也可以先发制人抓取 GIL 。

让我们回顾下 Python 是如何运行的。你的程序分两个阶段运行。首先，Python文本被编译成一个名为字节码的简单二进制格式。第二，Python解释器的主回路，一个名叫 pyeval_evalframeex() 的函数，流畅地读取字节码，逐个执行其中的指令。

当解释器通过字节码时，它会定期放弃GIL，而不需要经过正在执行代码的线程允许，这样其他线程便能运行：默认情况下，检测间隔是1000 字节码。所有线程都运行相同的代码，并以相同的方式定期从他们的锁中抽出。在 Python 3 GIL 的实施更加复杂，检测间隔不是一个固定数目的字节码，而是15 毫秒。然而，对于你的代码，这些差异并不显著。

**e）应对GIL**

在多核时代，编程的免费午餐没有了。如果程序不能用并发挤干每个核的运算性能，那就意谓着会被淘汰。对软件如此，对语言也是一样。那 Python 的对策呢？

Python 的应对很简单，以不变应万变。在 python 3 中依然有 GIL。之所以不去掉，原因嘛，不外以下几点：

**欲练神功，挥刀自宫**

CPython 的 GIL 本意是用来保护所有全局的解释器和环境状态变量的。如果去掉 GIL，就需要多个更细粒度的锁对解释器的众多全局状态进行保护。或者采用 Lock-Free 算法。无论哪一种，要做到多线程安全都会比单使用 GIL 一个锁要难的多。而且**改动的对象还是有 20 年历史的 CPython 代码树，更不论有这么多第三方的扩展也在依赖 GIL。对 Python 社区来说，这不异于挥刀自宫，重新来过。**这是Guido的声明：http://www.artima.com/forums/flat.jsp?forum=106&thread=214235

**就算自宫，也未必成功**

有位牛人曾经做了一个验证用的 CPython，将 GIL 去掉，加入了更多的细粒度锁。但是经过实际的测试，**对单线程程序来说，这个版本有很大的性能下降，只有在利用的物理 CPU 超过一定数目后，才会比 GIL 版本的性能**好。这也难怪。单线程本来就不需要什么锁。单就锁管理本身来说，锁 GIL 这个粗粒度的锁肯定比管理众多细粒度的锁要快的多。而现在绝大部分的 python 程序都是单线程的。再者，从需求来说，使用 python 绝不是因为看中它的运算性能。就算能利用多核，它的性能也不可能和 C/C++ 比肩。费了大力气把 GIL 拿掉，反而让大部分的程序都变慢了，这不是南辕北辙吗。

最后总结一下：

- **因为GIL的存在，只有IO Bound场景下得多线程会得到较好的性能**
- **如果对并行计算性能较高的程序可以考虑把核心部分也成C模块，或者索性用其他语言实现**
- **GIL在较长一段时间内将会继续存在，但是会不断对其进行改进**

## 五、利用c取代python程序中的核心代码

我们知道，Python是解释型语言，并不像c一样需要先编译然后执行，更何况Python具有很高的兼容性，如果你是c的或者java的都可以加入到Python代码中。加下来我们利用python来执行c的死循环。

1.先写一个c的死循环代码

```c
void test()
{
    while(1)
    {
        ;
    }
}
```

2.生成该代码的动态库

在linux中输入`gcc loop.c -shared -o loop.so`，当代码执行完成之后，就会在当前行下出现一个loop.so的文件，这个文件就是一个动态库。

3.创建python代码

```python
from ctypes import *
from threading import Thread

# 加载动态库
lib = cdll.LoadLibrary("./loop.so")

# 创建一个子线程，让其执行c语言编写的函数，此函数是一个死循环
t = Thread(target=lib.test)
t.start()

# 主线程
while True:
    pass
```

4.运行代码

当上面的代码运行之后，就会发现原本么有跑满的两个线程现在都已经跑满了。win貌似不行必须linux，我的是一核的，所以看不出来。

## 六、简单的面试题

**描述Python GIL的概念， 以及它对python多线程的影响？编写一个多线程抓取网页的程序，并阐明多线程抓取程序是否可比单线程性能有提升，并解释原因。**

参考答案：

1. Python语言和GIL没有半毛钱关系。仅仅是由于历史原因在Cpython虚拟机(解释器)，难以移除GIL。
2. GIL：全局解释器锁。每个线程在执行的过程都需要先获取GIL，保证同一时刻只有一个线程可以执行代码。
3. 线程释放GIL锁的情况： 在IO操作等可能会引起阻塞的system call之前,可以暂时释放GIL,但在执行完毕后,必须重新获取GIL Python 3.x使用计时器（执行时间达到阈值后，当前线程释放GIL）或Python 2.x，tickets计数达到100
4. Python使用多进程是可以利用多核的CPU资源的。
5. 多线程爬取比单线程性能有提升，因为遇到IO阻塞会自动释放GIL锁

参考文献：https://www.cnblogs.com/deeper/p/7730203.html