# 模块(__name__+dir+包)
"""
将定义的方法和变量存放在文件中,为一些脚本或者交互式的解释器实例使用,此文件即为模块
"""
# sys.path.append("package190904")
import sys
print("命令行参数如下:")
for i in sys.argv:
    print(i)
print("\nPython 路径:",sys.path)

import moudle17
print("使用模块名称来访问函数进行求和:",moudle17.adding(2,7))
ad=moudle17.adding  #取别名
print("使用别名进行求和:",ad(6,7))

from moudle17 import *  #简单,但不推荐
print("把整个模块导入到当前命名空间,直接使用方法进行求和:",adding(8,9))

from moudle17 import adding
print("从模块中导入指定方法(或变量)到当前命名空间,使用该方法进行求和:",adding(9,9))

from moudle17 import dividing,multiplying  #导入多个方法或变量

print("-----__name__-----")
"""
每一个模块都有一个__name__属性,当其值是'__main__'时,表示该模块自身在运行,否则是被引入
"""
if __name__=='__main__':
    print("test17.py:程序自身在运行")
else:
    print("test17.py:我来自另一个模块")
    
print("-----dir-----") 
print("sys模块内定义的所有名称:",dir(sys))
print("当前定义的所有名称:",dir())

print("-----标准模块-----")
"""
python自带的一些标准的模块库,详见库参考文档
有些模块直接被构建在解析器里,虽然不是一些语言内置的功能,但它却能很高效的使用,即使系统调用
这些组件会根据不同的操作系统进行不同形式的配置
模块sys内置在每个python解析器中
"""
'''
46,47无法执行,
sys.ps1 is only defined for the python interactive interpreter, so it's undefined in IDLE until set。
通过IDE编写无法执行,可以在cmd中执行,
'''
# print("sys.ps1:",sys.ps1)
# print("sys.ps2:",sys.ps2)

print("-----包-----")
"""
包是一种管理python模块命名空间的形式,采用"点模块名称"
在导入一个包的时候,python会根据sys.path中的目录来寻找这个包中包含的子目录
目录只有包含一个叫做__init__.py的文件才会被认作是一个包
主要是为了避免一些滥俗的名字(比如string)不小心的影响搜索路径中的有效模块
最简单的做法,放一个空的__init__.py就可以了,当然也可以包含一些初始代码或为__all__变量赋值(见下文)
sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

用户可以每次只导入一个包里面的特定模块:
ipmort sound.effects.echo

使用全名去访问:
sound.effects.echo.echofilter(input,output,delay=0.7,atten=4)

另一种导入子模块的方法:
from sound.effects import echo
echo.echofilter(input,output,delay=0.7,atten=4)

直接导入一个函数或者变量,并且可以直接使用它的echofilter()函数:
from sound.effects.echo import echofilter
echofilter(input,output,delay=0.7,atten=4)

当使用 from package import item 这种形式的时候
对应的item既可以是包里面的子模块(子包),或者包里面定义的其它名称,比如函数,类或者变量
import语法会首先把item当作一个包定义的名称
若未找到,再试图按照一个模块去导入,若还未找到,则将抛出一个exc:ImportError异常

当使用 import item.subitem.subsubitem 这种导入形式,除了最后一项,都必须是包
而最后一项则可以是模块或者是包,但不可以是类,函数或者变量的名字

Windows是一个大小写不区分的系统,很容易误导,而且DOS的8+3命名规则对长模块名称的处理问题会把问题搞得更纠结,故只能提供精确的包的索引了

导入语句遵循如下规则:
如果包定义文件__init__.py存在一个叫做__all__的列表变量
那么使用from package import *的时候就把这个列表中的所有名字作为包内容导入,作为包的作者记得在更新包后也更新__all__
__init__.py:
    __all__=["echo","surround","reverse"]
这表示当你使用 from sound.effects import * 这种方法时,你只会导入包里面这三个子模块
如果__all__真的没有定义,那么使用 from sound.effects import * 这种语法的时候,就不会导入包sound.effects里的任何子模块
它只是把包sound.effects和它里面定义的所有内容导入进来(可能运行__init__.py里定义的初始化代码)
这会把__init__.py里面定义的所有名字导入进来,并且它不会破坏掉我们在这句话之前导入的所有明确指定的模块
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
这个例子中,在执行from...import前,包sound.effects中的echo和surround模块都被导入到当前的命名空间中了(如果定义了__all__就更没问题了)
通常我们并不主张使用*这种方法来导入模块,因为这种方法经常会导致代码的可读性降低,不过这样倒是省时间,而且一些模块都设计成了只能通过特定的方法导入
推荐使用from Package import specigic_submodule,除非要导入的子模块有可能和其它包的子模块重名

如果在结构中包是一个子包(比如这个例子中对于包sound来说),而你又想导入兄弟包(同级别的包)你就得用导入绝对路径来导入
例如模块sound.filters.vocoder要使用sound.effects中的模块echo,你就要写成from sound.effects import echo
from . import echo
from .. import formats
from ..filters import equalizer
无论是隐式的还是显式的相对导入都是从当前模块开始的,主模块的名字永远是"__main__"
一个python应用程序的主模块,应当总是使用绝对路径引用
包还提供一个额外的属性__path__,这是一个目录列表,里面每一个包含的目录都有为这个包服务的__init__.py
你得在其它__init__.py被执行前定义,可以修改这个变量,用来影响包含在包里面的模块和子包
这个功能宾补常用,一般用来扩展包里面的模块
"""