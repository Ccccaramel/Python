# 字典连接
dict1 = {'name': 'Jim', 'age': 12, 'tel': 888888, 'add': 'WuHan'}
dict2 = {'name1': 'Tom', 'age1': 15, 'tel1': 666666, 'add1': 'WuChang'}
dict2 = {0: 'Tom', 2: 15, 3: 666666, 4: 'WuChang'}
dict1.update(dict2)
for k, v in dict1.items():
    print(k, v)
