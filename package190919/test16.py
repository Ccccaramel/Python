# 二维字典与key的调用以及value的判断
config = {
    "log" : {"console" : "True","file" : "False"},
    "warn" : {"console" : "True","file" : "True"},
    "error" : {"console" : "True","file" : "True"},
    "runtime" : {"console" : "True","file" : "True"},
}

def recursion(dic):
    for k in dic :
        if isinstance(k,dict) :
            recursion(k)
        else :
            print("k:",k,",v:",dic[k])
recursion(config)

c=config["log"]
# print("type(c):",type(c))
# for k,v in c.items():
#     print(k,v)
if c['console']=="True" :
    print("ok")

# key可以是变量吗?
ln='log'
c1=config[ln]
logname='file'
if c1[logname]=="True" :
    print("Yes")
if c1[logname]=="False" :
    print("No")
if c1[str(logname)]=="True" :
    print("yes")
if c1[str(logname)]=="False" :
    print("no")