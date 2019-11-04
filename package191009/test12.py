# XML 解析
"""
XML(eXtensible Markup Language) 指可扩展标记语言,标准通用标记语言的子集,是一种用于标记电子文件使其具有结构性的标记语言
XML 被设计用来传输和存储数据
XML 是一套定义语义标记的规则,这些标记将文档分成许多部件并对这些部件加以标识
XML 也是标记语言,即定义了用于定义其它与特定领域有关的 语义的 结构化的 标记语言的句法语言

python 对 XML 的解析
常见的 XML 编程接口有 DOM 和 SAX ,这两种接口处理 XML 文件的方式不同,当然使用场合也不同
python 有三种方法解析 XML : SAX , DOM , ElementTree
"""

"""
<1>SAX(simple API for XML)
   python 标准库包含 SAX 解析器, SAX 用事件驱动模型,通过解析 XML 的过程中触发一个个的事件并调用用户定义的回调函数来处理 XML 文件
SAX 是一种基于事件驱动的 API
利用 SAX 解析 XML 文档牵涉到两个部分:解析器和事件处理器
解析器负责读取 XML 文档,并向事件处理器发送事件,如元素开始跟元素结束事件
而事件处理器则负责对事件做出响应,对传递的 XML 数据进行处理
1.对大型文件处理
2.只需要文件的部分内容,或者只需从文件中得到特定信息
3.想建立自己的对象模型的时候
在 python 中使用 SAX 方式处理 XML 要先引入 xml.sax 中的 parse 函数,还有 xml.sax.handler 中的 ContentHandler

ContentHandler 类方法介绍
characters(content)方法
调用时机:
从行开始,遇到标签之前,存在字符, content 的值为这些字符串
从一个标签,遇到下一个标签之前,存在字符, content 的值为这些字符串
标签可以是开始标签,也可以是结束标签
startDocument() 方法
文档启动时的时候调用ma'ke
endDocument() 方法
解析器到达文档结尾时调用
startElement(name,attrs) 方法
遇到 XML 开始标签时调用,name是标签的名字,attrs是标签的属性值字典
endElement(name) 方法
遇到 XML 结束标签是调用

"""

"""
<2>DOM(Document Object Model)
   将 XML 数据在内存中解析成一个树,通过对树的操作来操作 XML
"""