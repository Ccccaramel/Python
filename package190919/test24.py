# 简单的爬虫(获取评分排名前茅的电影名以及评分+zip_longest:将多个序列转换成元组)
import urllib.request
import re
import itertools

page = urllib.request.urlopen('https://movie.douban.com/top250')  # 回一个类文件对象
htmlCode = page.read()  # 换成byte
data = htmlCode.decode('utf-8')  # 解码
# print(data)
reg = r'property="v:average">(\d.\d)</span>'
name = r'<span class="title">([\u4e00-\u9fa5]*)</span>'
reg_num = re.compile(reg)
cname = re.compile(name)
mark_list = reg_num.findall(data)
name_list = cname.findall(data)
for n, m in itertools.zip_longest(name_list, mark_list, fillvalue=-1):
    print(n, ":", m)
