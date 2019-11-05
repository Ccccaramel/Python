# 日期(calendar)+时间(time)+datetime
"""
python 提供了一个 time 和 calendar 模块可以用于格式化日期和时间
时间间隔是以秒为单位的浮点小数
每个时间戳都以自从 1970 年 1 月 1 日午夜(历元)经历了多长时间来表示

datetime 提供用于操作日期和时间的类,重点是针对输出格式和操作的有效属性提取,具体使用略
"""

# 获取时间戳
"""
时间戳单位最适用于做日期运算
UNIX 和 Windows 只支持 1970 年至 2038 年
"""
import time
# while 1:
#     ticks = time.time()
#     print("当前时间戳: {}".format(ticks))
#     time.sleep(1)

# 时间元组
"""
很多 python 函数用一个包含 9 组数字的元组处理时间
下标--字段--值
0   tm_year   年( 4 位数)      例如: 2019
1   tm_mon    月               1 到 12
2   tm_mday   日               1 到 31
3   tm_hour   小时             0 到 23
4   tm_min    分钟             0 到 59
5   tm_sec    秒               0 到 61(60或61是闰秒)
6   tm_wday   一周的第几日     0 到 6(0是周一) 
7   tm_yday   一年的第几日     1 到 366(儒略历)  
8   tm_isdst  夏令时           -1(未知,默认),0(不是夏令时),1(有夏令时)
"""

# 获取当前时间
"""
从返回浮点数的时间戳方式向时间元组转换,只要将浮点数传递給如 localtime 之类的函数
"""
import time
localtime1 = time.localtime(time.time())
print("本地时间: {}".format(localtime1))

# 获取格式化的时间
"""
最简单的获取可读的时间模式的函数是 asctime()
"""
import time
localtime2 = time.asctime(time.localtime(time.time()))
print("本地时间(格式化): {}".format(localtime2))

# 格式化日期
"""
可以使用 time 模块的 strftime 方法来格式化日期
time.strftime(format[,t])
"""
import time
# 格式化成 2016-03-20 11:45:39 形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成 Fra October 28 11:45:39 2019 形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 格式化字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
# 字符串格式化成自定义使时间格式
a = "Fri Oct 25 11:00:39 2019"
print(time.strftime("%Y/%m/%d %H:%M:%S", time.strptime(a, "%a %b %d %H:%M:%S %Y")))
"""
代码敲着敲着就学起了英语...
Mon    Monday      |   JAN Jan    January           AUG Aug    August
Tues   Tuesday     |   FEB Feb    February          SEP Sept   September
Wed    Wednesday   |   MAR Mar    March             OCT Oct    October
Thur   Thursday    |   APR Apr    April             NOV Nov    November
Fri    Friday      |   MAY May    May               DEC Dec    December
Sat    Saturday    |   JUN Jun    June              
Sun    Sunday      |   JUL Jul    July      

python 中时间日期格式化符号        
%y | %Y   两位数|四位数 的年份表示 (00-99)|(000-9999)
%m        月份(01-12)
%d        月内中的一天(0-31)
%H | %I   24|12 小时制小时数 (0-23)|(01-12)
%M        分钟数(00-59)
%S        秒(00-59)
%a | %A   本地 简化|完整 星期名称
%b | %B   本地 简化|完整 月份名称
%c        本地相应的日期表示和时间表示
%p        本地 A.M. 或 P.M. 等价符
%U        一年中的星期数(00-53)星期天为星期的开始
%w | %W   星期(0-6),星期天为星期的开始|一年中的星期数(00-53)星期一为星期的开始
%x | %X   本地相应的 日期|时间 表示
%Z        当前时区的名称
%%        % 号本身
室女座超星系团本星系群银河系太阳系盖亚中华人民共和国
"""

# 获取某月日历
import calendar
cal = calendar.month(2019, 10)
print("2019年10月:\n{}".format(cal))

# Time 模块
"""
---------内置函数----------
time.altzone                           返回格林威治西部的夏令时地区的偏移秒数,如果该地区在格林威治东部会返回负值(如西欧,英国),对夏令时启用地区才能使用
time.asctime([tupletime])              接收时间元组并返回一个可读的形式为"Tue Dec 11 18:12:11 1996"(1996年12月11日 周二18时12分11秒)的24个字符串
*time.clock()                <弃用!>   用浮点数计算的秒数返回当前的 CPU 时间,用来衡量不同程序的耗时,比 time.time() 更有用,依赖操作系统
time.ctime([secs])                     等同于 asctime(localtime(secs)) ,未给参数相当于asctime()
time.gmtime([secs])                    接收时间戳(1970纪元后经过的浮点秒数)并返回格林威治天文时间下的时间元组 t , t.tm_isdst 始终为 0
time.localtime([secs])                 接收时间戳(1970纪元后经过的浮点秒数)并返回当地时间下的时间元组 t(t.tm_isdst 可取 0 或 1 ,取决于当地是否启用夏令时 )
time.mktime(tupletime)                 接收时间戳(1970纪元后经过的浮点秒数)
time.sleep(secs)                       推迟调用线程的运行, secs 指秒数
time.strftime(fmt[,tupletime])         接收以时间元组,并返回以可读字符串表示的当地时间,格式由 fmt 决定
time.strptime(str,ftm='格式化符号')     根据 fmt 的格式把一个时间字符串解析为时间元组
time.time()                            返回当前的时间戳(1970纪元后经过的浮点秒数)
time.tzset()                           根据环境变量 TZ 重新初始化相关设置
time.perf_counter()                    返回计算器的精准时间(系统的运行时间),包括整个系统的睡眠时间,由于返回值的基准点是未定义的,故只有连续调用的结果之间的差才有效
time.process_time()                    (同上)
----------属性----------
time.timezone    当地时区(未启动夏令时)距离格林威治的偏移数(>0,美洲;<=0,大部分欧洲,亚洲,非洲)
time.tzname      包含了一对根据情况的不同而不同的字符串,分别是带夏令时的本地时区名称和不带的
"""

# time.perf_counter() 实例
import time

scale = 50
print("执行开始".center(scale//2, "-"))  # .center() 控制输出的样式，宽度为 25//2，即 22，汉字居中，两侧填充 -

# 调用一次 perf_counter(),从计算机系统里随机选一个时间点A,计算其距离当前时间点B1有多少秒
# 当第二次调用该函数时,默认从第一次调用的时间点A算起,距离当前时间点B2有多少秒
# 两个函数取差，即实现从时间点B1到B2的计时功能。
start = time.perf_counter()

for i in range(scale+1):
    a = '>' * i             # i 个长度的 * 符号
    b = ' ' * (scale-i)  # scale-i 个长度的 . 符号 . 符号 * 和 . 总长度为50
    c = (i/scale)*100  # 显示当前进度，百分之多少
    dur = time.perf_counter() - start    # 计时,计算进度条走到某一百分比的用时
    # ^:居中 \r:用来在每次输出完成后,将光标移至行首,这样保证进度条始终在同一行输出,即在一行不断刷新的效果
    print("\r{:^3.0f}%[{}{}]{:.2f}s".format(c, a, b, dur), end='')
    time.sleep(0.1)     # 在输出下一个百分之几的进度前,停止0.1秒

print("\n"+"执行结果".center(scale//2, '-'))

# time.tzset() 实例
"""
根据环境变量 TZ 重新初始化时间相关设置
标准 TZ 环境变量格式:
std , offset               [dst [offset [,start[/time], end[]/time]]]
std , dst                  三个或者多个时间的缩写字母,传递给 time.tzname
offset                     距离 UTC 的偏移,格式:[+|-]hh[:mm[:ss]]{h=0-23,m/s=0-59}
start[/time] end[/time]    DST 开始生效时的日期,格式为 m.w.d ,代表日期的月份,周数和日期, w=1 指月份中的第一周,而 w=5 指月份的最后一周, start 和 end 可以是以下格式之一:
                               Jn:        儒略日n(1<=n<=365),闰年日(2月29)不计算在内
                               n:         儒略日n(1<=n<=365),闰年日(2月29)计算在内
                               Mm.n.d:    日期的月份,周数和日期,w=1 指月份中的第一周,而 w=5 指月份的最后一周     
                               Jn:        (可选) DST 开始生效时的时间(24小时制),默认为02:00(指定时区的本地时间)

该函数无返回值

import time
import os

os.environ['TZ'] = 'EST+05EDT,M4.1.0,M10.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))

os.environ['TZ'] = 'AEST-10AEDT-11,M10.5.0,M3.5.0'
time.tzset()
print(time.strftime('%X %x %Z'))
"""

# 日历(Calendar)模块
"""
每周第一天默认是星期一,星期天是默认的最后一天
----------内置函数----------
calendar.calendar(year,w=2,l=1,c=6)        返回一个多行字符串格式的 year 年年历, 3 个月一行,间隔距离为 c ,每日宽度间隔为 w 字符,每行宽度 21*W+18+2*C, l 是每星期行数
calendar.firstweekday()                    返回当前每周起始日期的设置,默认情况下,首次载入 caendar 模块时返回 0 ,即星期一
calendar.isleap(year)                      是闰年返回 True ,否则为 False
calendar.leapdays(y1,y2)                   返回 y1 与 y2 两年之间的闰年总数
calendar.month(year,month,w=2,l=1)         返回一个多行字符串格式的 year 年 month 月日历,两行标题,一周一行,每日宽度间隔为 w 字符,每行的长度为7*w+6,l是每星期的行数
calendar.monthcalendar(year,month)         返回一个整数的单层嵌套列表,每个子列表装载代表一个星期的整数, year 年 month 月外的日期都设为 0 ,范围内的日子都由该月第几日表示,从 1 开始
calendar.monthrange(year,month)            返回两个整数,第一个是该月的星期几,第二个是该月有几天,星期几是从 0(星期一) 到 6(星期日)
calendar.prcal(year=1,w=2,l=1,c=6)         相当于 print calendar.calendar(year,w,l,c)
calendar.prmonth(year,month,w=2,l=1)       相当于 print calendar.calendar(year,w,l,c)
calendar.setfirstweekday(weekday)          设置每周的起始日期码, 0(星期一) 到 6(星期日)
calendar.timegm(tupletime)                 和 time.gmtime 相反,接受一个时间元组形式,返回该时刻的时间戳(1970纪元后经过的浮点秒数)
calendar.weekday(year,month,day)           返回给定日期的日期码, 0(星期一) 到 6(星期日),月份为 1(一月) 到12(十二月)
"""