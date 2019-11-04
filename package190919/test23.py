# 在类中访问父类被重写的三种方法
class Animal(object):
	def eat(self):
		print("动物吃东西")
class Cat(Animal):
	def eat(self):
		  print("猫吃鱼")
		  #格式一：父类名.方法名(对象)
		  Animal.eat(self)
		  #格式二:super(本类名,对象).方法名()
		  super(Cat,self).eat()
		  #格式三:super()方法名()
		  super().eat()
cat1=Cat()
cat1.eat()
print(cat1)
