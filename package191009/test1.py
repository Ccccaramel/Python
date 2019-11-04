# 类的继承与调用
class animal:
	__age=1
	__food=""
	def __init__(self,food):
		self.__age=10
		self.__food=food

	def eat(self):
		print("I'm a {} years animal!I'm eatting {}!".format(self.__age,self.__food))

class tomCat:
    def say(self):
        print("hi!I'm tomCat")

class dog(animal):
	__host=""
	def __init__(self,name,food):
		animal.__init__(self,food)  #类名.构造方法(self,变量)
		self.__host=name

	def out(self):
		animal.eat(self)
		print("My host name is {}.".format(self.__host))
		tomCat().say()
	
	# def getSuper(self):
	# 	return animal.__base__
a=animal("rice")
tom=dog("Jim","apple")
tom.out()
# s=tom.getSuper()
# s.eat()
print(dir(tom))