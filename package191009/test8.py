# encode + decode
"""
python3 默认编码为unicode
而 python2 是ASCII码
Windows 环境默认是 gbk 编码

编码种类
ASCII   占1个字节，只支持英文
GB2312   占2个字节，支持6700+汉字
GBK   GB2312的升级版，支持21000+汉字，中文2个字节
Unicode    2-4字节，已经收录136690个字符
UTF-8    使用1-4个字节表示所有字符，优先使用1个字节，无法满足则增加1个字节，最多4个，英文占1个，欧语体系占2个，东亚占3个，其它及特殊字符占4个，中文占3个
UTF-16   使用2或4个字节表示所有字符，优先使用2个字节，否则使用4个字节

python3 的执行过程
解释器找到代码文件，把代码字符串按文件头定义的编码加载到内存，转成 unicode  ---> 把代码字符串按照语法规则进行解释 ---> 所有的变量字符都会以 unicode 编码声明
python3 自动把文件编码转为 unicode ， python2 并不会自动而需要手动转码

手动转码规则
UTF-8 --> decode 编码 --> Unicode
Unicode --> encode 编码 --> GBK/UTF-8 等
使用 type 可以查看编码形式， unicode 是 'unicode', GBK 和 UTF-8 是 'str' 或 'bytes'
python2
----------
#coding=utf-8
a='编码'  # utf-8
b=a.decode('utf-8')  # unicode
c=b.encode('gbk')  # gbk/utf-8
d=c.decode('gbk').encode('utf-8')  #先解码成 unicode ，后又编码成 gbk/utf-8
print a,b,c,d
print type(a),type(b),type(c),type(d)
打印结果:
编码编码【此处乱码】编码
<type 'str'><type 'unicode'><type 'str'><type 'str'>
----------
"""
a='编码'  # unicode
b=a.encode('utf-8')  # utf-8
c=a.encode('gbk')  # gbk
print(a,b,c)
print(type(a),type(b),type(c))