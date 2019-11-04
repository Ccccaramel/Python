# <new> 代替lua中的 # 
def _len(dic):
	n1 = 0  #计数器，记录当前循环次数，当遇到元素为None时仍然计数
	count=0  #计数器，当遇到元素为None时不计数
	sgin=0
	state=True  #索引状态，
				#True时表示遍历至此索引一直是连续状态
				#False时表示索引因为字符而断开，需要到达写一个数字索引并判断是否连续，若连续置为True，否则直接return Ret
	l=len(dic)  #真实长度
	# print("l:",l)
	if dic!={} :
		for k in dic :
			# print("k:",k,",v:",dic[k])
			# print("Ret:",Ret,",k:",k,",state:",state,",node:",node)
			# print("k:",k,",num:",num,",Ret:",Ret)
			if ( isinstance(k,int)==True or k.isnumeric()==True ) :  #判断当前key是否为数字
				# print("k:",k,",n1:",n1,",dic[k]:",dic[k])
				if (k==n1 or int(k)==n1) :  #判断key与num是否计数器相等
					if dic[k]==None :  #判断值是否为None
						sgin+=1 
						state=False
					else:
						if state==False :  #key刚从非数字中"出来"，连续，数字，与num相等，非None，重新连接
							count=count+sgin  #将key为非数字的元素的个数加入
							sgin=0  #将计数清零
						else:#连续
							pass
						count+=1
					# print("count:",count)
				else:  #key与num不相等退出
					break
			else:  #不为数字，但有可能是连续的，将状态置F，并计数
				sgin+=1
				state=False
			n1+=1
	return count
# 5 5 5
d0={0:2,1:98,2:0,3:1,4:3}
d1={"0":2,"1":98,2:0,3:1,4:3}
d2={0:2,"1":98,2:0,"3":1,4:3}
# 5 5 4
d3={"k":2,"o":98,2:0,3:1,4:3}  #<连>非数字在第一位
d4={0:2,"1":98,"u":0,3:1,4:3}  #<连>非数字在中间
d6={"k":2,"o":98,2:0,3:1,"p":3}  #<连>非数字在末尾
# 0 2 0
d7={"k":2,"o":98,3:0,4:1,6:3}  #<断>非数字在第一位
d8={0:2,"1":98,"u":0,4:1,6:3}  #<断>非数字在中间
d9={"k":2,"o":98,3:0,4:1,"p":3}  #<断>非数字在末尾


# 5
d10={"0":2,1:98,"2":0,3:1,4:3}
d10[1]=None
d10[100]=12
# 5 4
d11={0:2,1:None,2:0,3:1,4:3}
d12={0:2,1:None,2:0,3:1,4:None}

print("d0:",_len(d0))
print("d1:",_len(d1))
print("d2:",_len(d2))
print("d3:",_len(d3))
print("d4:",_len(d4))
print("d6:",_len(d6))
print("d7:",_len(d7))
print("d8:",_len(d8))
print("d9:",_len(d9))
print("d10:",_len(d10))
print("d11:",_len(d11))
print("d12:",_len(d12))
