# 网络编程(服务端)
"""
python 提供了两个级别访问的网络服务
    <1>低级别的网络服务支持基本的 Socket 
        它提供了标准的 BSD Socket API
        可以访问底层操作系统 Socket 接口的全部方法
    <2>高级别的网络服务模块 SocketServer
        它提供了服务器中心类
        可以简化网络服务器的开发

什么是 Socket?
    Socket 又称"套接字"
    应用程序通常通过"套接字"向网络发出请求或者应答网络请求
    使主机间或这一台计算机上的进程间可以通讯
    
Socket() 函数
    用来创建套接字
    socket.socket([family[,type[,proto]]])
    family   套接字家族可以是 AF_UNIX 或 AF_INET
    type     套接字类型可以根据是面向连接或非连接分为 SOCK_STREAM 或 SOCK_DGRAM
    proto    一般不填,默认为0
    
**********Socket 对象(内建)方法**********

          -----服务器端套接字-----
s.bind()                            	绑定地址( host , port )到套接字, 在 AF_INET 下,以元组( host , port )的形式表示地址
s.listen()	                            开始 TCP 监听。 backlog 指定在拒绝连接之前,操作系统可以挂起的最大连接数量。该值至少为1,大部分应用程序设为5就可以了
s.accept()                           	被动接受TCP客户端连接,(阻塞式)等待连接的到来

          -----客户端套接字-----
s.connect()	                            主动初始化 TCP 服务器连接,。一般 address 的格式为元组( hostname , port ),如果连接出错,返回 socket.error 错误
s.connect_ex()                      	connect() 函数的扩展版本,出错时返回出错码,而不是抛出异常

          -----公共用途的套接字函数-----
s.recv()                            	接收 TCP 数据,数据以字符串形式返回,bufsize指定要接收的最大数据量。 flag 提供有关消息的其他信息,通常可以忽略
s.send()                              	发送 TCP 数据,将 string 中的数据发送到连接的套接字。返回值是要发送的字节数量,该数量可能小于 string 的字节大小
s.sendall()                          	完整发送 TCP 数据,完整发送 TCP 数据。将 string 中的数据发送到连接的套接字,但在返回之前会尝试发送所有数据。成功返回 None ,失败则抛出异常
s.recvfrom()                          	接收 UDP 数据,与 recv() 类似,但返回值是( data , address )。其中 data 是包含接收数据的字符串, address 是发送数据的套接字地址
s.sendto()	                            发送 UDP 数据,将数据发送到套接字,address是形式为(ipaddr , port )的元组,指定远程地址。返回值是发送的字节数
s.close()                           	关闭套接字
s.getpeername()	                        返回连接套接字的远程地址。返回值通常是元组( ipaddr , port )
s.getsockname()                     	返回套接字自己的地址。通常是一个元组( ipaddr , port )
s.setsockopt(level,optname,value)   	设置给定套接字选项的值
s.getsockopt(level,optname[.buflen])	返回套接字选项的值
s.settimeout(timeout)               	设置套接字操作的超时期, timeout 是一个浮点数,单位是秒。值为 None 表示没有超时期。一般,超时期应该在刚创建套接字时设置,因为它们可能用于连接的操作(如 connect() )
s.gettimeout()                      	返回当前超时期的值,单位是秒,如果没有设置超时期,则返回 None 
s.fileno()                          	返回套接字的文件描述符
s.setblocking(flag)                 	如果 flag 为0,则将套接字设为非阻塞模式,否则将套接字设为阻塞模式(默认值)。非阻塞模式下,如果调用 recv() 没有发现任何数据,或 send() 调用无法立即发送数据,那么将引起 socket.error 异常
s.makefile()                          	创建一个与该套接字相关连的文件
"""
# 服务端代码
import socket,sys

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #创建 socket 对象
host=socket.gethostname()  #获取本地主机名
port=9999
serversocket.bind((host,port))  #绑定端口号
serversocket.listen(5)  #设置最大连接数，超过后排队

while True:
    clientsocket,addr=serversocket.accept()  #建立客户端连接
    print("连接地址:{}".format(str(addr)))  #
    msg="this is test6,i see you!"+"\r\n"
    clientsocket.send(msg.encode("utf-8"))  #编码
    clientsocket.close()
    
"""
一些重要模块
--协议--------------功能用处--------------端口号--------Python 模块----------
HTTP     网页访问                         80    httplib, urllib, xmlrpclib
NNTP     阅读和张贴新闻文章，俗称为"帖子"   119   nntplib
FTP      文件传输                         20    ftplib, urllib
SMTP     发送邮件                         25    smtplib
POP3     接收邮件                         110   poplib
IMAP4    获取邮件                         143   imaplib
Telnet   命令行                           23    telnetlib
Gopher   信息查找                         70    gopherlib, urllib
"""