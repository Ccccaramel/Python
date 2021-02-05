# 输出"Hello World"
import time
from splinter.browser import Browser
from time import sleep
import traceback  # traceback 模块被用来跟踪异常返回信息
username = u"15971366760"
passwd = u"20051109nl"  # bie wang le o
"""
起始点和乘车时间的 cookies 值在 Application 选项里找
表格中 cookie 的值:
 _jc_save_fromeStation      出发地
 _jc_save_toStatation       目的地
 _jc_save_fromDate          出发日期
 _jc_save_toDate            返程日期
 %u6DF1%u5733%2CSZQ 深渊
 %u8572%u6625%2CQRN 蕲春
 %u6B66%u6C49%2CWHN 武汉
 %u5317%u4EAC%2CBJP 北京
 
 可预订的【预订按钮】的标签中 class="btn72"
 否则均不可正常预订(已售完、暂停发售:、时间未到) class="no-br"
"""
from_station = u"%u6DF1%u5733%2CSZQ"
to_station = u"%u8572%u6625%2CQRN"
from_date = u"2019-12-05"  # 时间格式 1996-05-08
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
selling_time = u"Tue Nov 05 14:00:00 2019"  # 参考上面打印的格式
order = 0  # 车次,选择第几趟, 0 则从上至下依次点击
ticketer = u"丁坦华"  # 设置乘车人姓名
check = u"normalPassenger_0"
# 设定网址
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"  # 选票界面
login_url = "https://kyfw.12306.cn/otn/login/init"  # 登录界面
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"  # 登录界面
url = "https://kyfw.12306.cn/otn/resources/login.html"

def login():
    """
    之前是通过 sleep 等待固定且充裕的时间让浏览器加载
    然后接着触发按钮
    这样做太慢了
    通过死循环判断指定信息是否存在的方式更优
    """
    while 1:
        print("1")
        if bwr.is_text_present(u"登录"):  # 登录按钮是否存在,本质是在网页源代码中搜索相关内容,似乎有点耗时间
            print("2")
            bwr.find_by_text(u"登录").click()  # 点击"登录"按钮
            print("3")
            break
    # sleep(0.02)
    while 1:
        print("4")
        if bwr.is_text_present(u"账号登录"):
            print("5")
            bwr.find_by_text(u"账号登录").click()  # 点击"账号登录"按钮
            print("6")
            break
    # print("3")
    while 1:
        if bwr.is_text_present(u"立即登录"):
            break
    # bwr.fill("J-userName", username)  # fill 填充搜索框的内容,账号和密码的 id 有可能更改,而且还有可能把 name 换成了 id 鸥
    bwr.find_by_id("J-userName").fill(username)
    # bwr.fill("J-password", passwd)
    bwr.find_by_id("J-password").fill(passwd)
    # bwr.find_by_text(u"账号登录").click()  # 点击"账号登录"按钮
    print(u"等待验证码,请手动输入...")
    print("bwr.url:", bwr.url)
    while 1:
        if bwr.url == url:  # 判断当前的 url 是否已经进入系统
            # print("bwr.url-1:", bwr.url)
            # print("initmy_url:", url)
            sleep(0.001)
        else:
            break


def getTickt():  # 购票
    global bwr
    global bwr
    bwr = Browser(driver_name="chrome")  # 使用 splinter 打开 chrome 浏览器
    bwr.visit(ticket_url)  # splinter 打开浏览器(返回购票页面)
    while bwr.is_text_present(u"登录"):
        sleep(0.001)
        login()
        if bwr.url != url:  # 判断是否已经进入系统
            break
    try:
        print(u"购票页面...")
        bwr.visit(ticket_url)  # splinter 打开浏览器(跳回购票页面)
        # bwr.find_by_text(u"首页").click()  # 点击"首页"按钮
        while 1:
            if bwr.is_text_present(u"查询"):  # 登录按钮是否存在
                break
        bwr.cookies.add({"_jc_save_fromStation": from_station})  # 填入起始站
        bwr.cookies.add({"_jc_save_toStation": to_station})  # 填入终点站
        bwr.cookies.add({"_jc_save_fromDate": from_date})  # 选定时间
        wait_time()  # 此步执行完就意味着马上将要开始抢票了
        bwr.reload()  # 刷新页面
        sleep(0.001)
        count = 0  # 查询次数
        if order != 0:  # 车次
            while bwr.url == ticket_url:  # 判断页面是否跳转,若为 False 则表明已跳转至【提交订单】界面
                bwr.find_by_text(u"查询").click()  # 点击查询
                count += 1
                print(u"循环点击查询...第 %s 次"%count)
                sleep(1.001)
                try:
                    bwr.find_by_text(u"预订")[order-1].click()  #点击预订
                except:
                    print(u"还没开始预订")
                    continue
        else:
            while bwr.url == ticket_url:  # 判断页面是否跳转

                """
                每刷新几次就会有弹窗弹出 "该车次暂不办理业务!"
                此时只能点确定
                """
                if bwr.is_text_present(u"确定"):  # 登录按钮是否存在
                    bwr.find_by_text(u"确定").click()  # 点击"登录"按钮

                bwr.find_by_text(u"查询").click()  # 点击查询
                count += 1
                print(u"循环点击查询...第 %s 次!"%count)
                sleep(1.001)
                try:
                    for i in bwr.find_by_text(u"预订"):
                        i.click()
                        print("点击预订的时间戳: {}".format(get_time_stamp()))
                        sleep(0.001)
                except:
                    print(u"还没开始预订!")
                    continue
        sleep(1)  # 等待加载页面,包括此行在内以及之后的 sleep 都不用在意了,你的票已经"拿"到了,但需要赶快支付
        print("ok")
        # bwr.find_by_text(ticketer).click()
        bwr.find_by_id(check).click()
        sleep(1)
        bwr.find_by_text(u"提交订单").click()
        sleep(1)

        #
        # 以 D 开头的动车可以选座
        # 窗   A   B   C   过道   D   F   窗
        # id: 1A  1B  1C         1D  1F
        # bwr.find_by_id(u"1F").click()
        # sleep(1)
        #

        # bwr.find_by_id(u"qr_submit_id").click()  # 确认(测试的时候把此行注销掉,否则会进入支付界面,每天只有三次取消订单的机会,之后将无法购票)
        print(u"成功抢到一张票")
    except Exception as e:
        print(traceback.print_exc())


"""
仅仅用脚本抢一张已经开始出售的而且余票充足的票是没有用的
你最初的目的是想通过它来抢到回家的票!

即使你用脚本还是没黄牛快
百兆级网络   公司网还行
独立服务器   不知道公司服务器怎么样(高危)
高配置路由   人生本来就短你还要走捷径
七类万兆网线   听着就感觉很厉害
独立抢票软件   至少比我脚本好:(
多台机器同时启动   多线程可以媲美吗?不可以线程切换需要大量 CPU 资源,，还不如单线程

但机器至少比你快
为了更快你得计算好时间点
python 的时间戳的精确度为 1/10^7 秒
"""


def get_time_stamp():  # 获取当前时间戳
    return time.time()


def time_conversion(stime:str):  # 时间转换,将字符串转换成时间戳
    return time.mktime(time.strptime(stime, "%a %b %d %H:%M:%S %Y"))

def wait_time():
    t0 = get_time_stamp()  # 当前时间
    s = "Tue Nov 05 16:31:00 2019"  # 目标时间 书写格式?见test13.py
    """
    为什么要 -0.001 ?
    如果你在目标时间那一瞬间才点击刷新,那么你已经慢了一步
    提前点击刷新,等到你的请求到达服务器大概率已经开始售票
    但也不可以提前过早
    """
    t1 = time_conversion(s)-0.001  # 目标时间的时间戳
    while 1:
        t0 = get_time_stamp()
        if t0 <= t1:
            # print("时间未到! {}".format(t0))
            continue
        else:
            break
    t0 = get_time_stamp()
    print("提前刷新! {}".format(t0))


def sleep_time():
    while 1:
        print("1",get_time_stamp())
        sleep(0.001)
        print("2",get_time_stamp())


if __name__ == "__main__":
    # wait_time()
    # sleep_time()
    getTickt()
