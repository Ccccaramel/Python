# 输出"Hello World"1
from splinter.browser import Browser
from time import sleep
import traceback  # traceback 模块被用来跟踪异常返回信息
username = u""
passwd = u""  # bie wang le o
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
"""
from_station = u"%u6DF1%u5733%2CSZQ"
to_station = u"%u8572%u6625%2CQRN"
from_date = u"2019-11-01"  # 时间格式 1996-05-08
order = 0  # 车次,选择第几趟, 0 则从上至下依次点击
ticketer = u""  # 设置乘车人姓名

# 设定网址
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"  # 选票界面
login_url = "https://kyfw.12306.cn/otn/login/init"  # 登录界面
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"  # 登录界面
url = "https://kyfw.12306.cn/otn/resources/login.html"

def login():
    bwr.find_by_text(u"登录").click()  # 点击"登录"按钮
    sleep(3)
    bwr.find_by_text(u"账号登录").click()  # 点击"登录"按钮
    sleep(3)
    # bwr.fill("J-userName", username)  # fill 填充搜索框的内容,账号和密码的 id 有可能更改,而且还有可能把 name 换成了 id 鸥
    bwr.find_by_id("J-userName").fill(username)
    sleep(1)
    # bwr.fill("J-password", passwd)
    bwr.find_by_id("J-password").fill(passwd)
    sleep(1)
    print(u"等待验证码,请手动输入...")

    # old_bwrurl = bwr.url
    print("bwr.url:", bwr.url)
    # while True:
    #
    #     if bwr.url == url:  # 判断当前的 url 是否已经进入系统
    #         print("bwr.url:", bwr.url)
    #         # print("initmy_url:", url)
    #         sleep(3)
    #     else:
    #         break


def getTickt():  # 购票
    global bwr
    bwr = Browser(driver_name="chrome")  # 使用 splinter 打开 chrome 浏览器
    bwr.visit(ticket_url)  # splinter 打开浏览器(返回购票页面)
    while bwr.is_text_present(u"登录"):
        sleep(3)
        login()
        if bwr.url != url:  # 判断是否已经进入系统
            break
    try:
        print(u"购票页面...")
        bwr.visit(ticket_url)  # splinter 打开浏览器(跳回购票页面)
        bwr.cookies.add({"_jc_save_fromStation": from_station})  # 加载查询信息
        bwr.cookies.add({"_jc_save_toStation": to_station})
        bwr.cookies.add({"_jc_save_fromDate": from_date})
        bwr.reload()
        sleep(2)
        count = 0
        if order != 0:
            while bwr.url == ticket_url:
                bwr.find_by_text(u"查询").click()
                count += 1
                print(u"循环点击查询...第 %s 次"%count)
                sleep(1)
                try:
                    bwr.find_by_text(u"预订")[order-1].click()()
                except:
                    print(u"还没开始预订")
                    continue
        else:
            while bwr.url == ticket_url:
                bwr.find_by_text(u"查询").click()
                count += 1
                print(u"循环点击查询...第 %s 次"%count)
                sleep(1)
                try:
                    for i in bwr.find_by_text(u"预订"):
                        i.click()
                        sleep(1)
                except:
                    print(u"还没开始预订")
                    continue
        sleep(1)
        bwr.find_by_text(ticketer)[0].click()
        sleep(1)
        bwr.find_by_text(u"提交订单").click()
        sleep(1)
        print(u"成功抢到一张票")
    except Exception as e:
        print(traceback.print_exc())


if __name__ == "__main__":
    getTickt()
