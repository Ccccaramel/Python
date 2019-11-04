# 仿写Lua的select内置方法
# 在python中，不定参数是一个集合
def select_v(index,*vartuple):
    if index == '#' :
        l=_vartuple_len(*vartuple)
        if l==1 :
            l=select_vlen(0,*vartuple)
        return l
    elif isinstance(index,int) or isinstance(index,float) :
        if index >= 0 :
            return _vartuple_value(index,*vartuple)
        else :
            pass
    else:
        pass

# 获取不定参数中指定参数的长度（假设指定的参数是字典）
def select_vlen(index,*vartuple):
    var=select_v(index,*vartuple)
    return len(var)

# 返回不定参数的长度
def _vartuple_len(*vartuple):
    sgin=0
    for var in vartuple:
        sgin+=1
    return sgin

# 获取不定参数中指定索引的参数
def _vartuple_value(index,*vartuple):
    sgin=0
    for var in vartuple:
        if sgin==index :
            return var
        sgin+=1
    return sgin

dict1={'name':'Jim','age':12,'tel':888888,'add':'WuHan'}
dict2={'name':'Tom','age':15,'tel':666666,'add':'WuChang'}
dict3={'name':'Tony','age':13,'tel':444444,'birth':'BeiJing','add':'NanChang'}
vlen=select_v("#",dict1,dict2,dict3)
vlen1=select_v("#",dict1)
print("len:",vlen)
print("len:",vlen1)
print("select_v(2,dict1,dict2,dict3):",select_v(2,dict1,dict2,dict3))
print("select_vlen(2,dict1,dict2,dict3):",select_vlen(2,dict1,dict2,dict3))
