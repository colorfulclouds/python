#function
import math

print(abs(-2))

#函数匿名
hh=abs
print(hh(-2))


print(min(1,3,5,1.2,0.1))
print(max(1,5,6,4,21,12.2))

#类型转换
int('111')
float('123.2')

str(1223)

bool(1)
bool('')

print(str(hex(12)))


#函数定义
def hello(age):
	if age>18:
		print("old")
	else:
		print("young")
		
hello(22)

#空函数
def	nop():
	pass

#实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

'''
if age>18:
	pass
#暂时没有想好执行什么逻辑 就可以先放一个pass
'''

#加入类型检测
def my_abs(x):
	if not isinstance(x , (int , float)):
		raise TypeError('bad operand type')
	
	if x>0:
		return x
	else:
		return -x

#函数返回多个值
def multi_return():
	return 1,2,3

a,b,c = multi_return()
#其实返回的是一个值 一个tuple
r = multi_return()

print(a,b,c)
print(r)

#计算二次方程
def quadratic(a,b,c):
	temp=math.sqrt(b*b-4*a*c)
	x1 = 1.0/(2*a)*(-b+temp)
	x2 = 1.0/(2*a)*(-b-temp)
	return x1 ,x2

x1 , x2 = quadratic(1,5,4)
print(x1 , x2)


#函数默认参数
def default_func(a , b=10 , city =55):
	return a , b ,city

x,y,z=default_func(12)
print(x,y,z)

x,y,z=default_func(12,25)
print(x,y,z)

#也可以不按顺序使用默认参数 但是必须指出默认参数的形参名字
x,y,z=default_func(12,city=48)
print(x,y,z)

#可变参数 参数个数可以变化
def sum(*number):
	result=0
	for num in number:
		result += num
		print(num , end='')
	return result

print("sum:%d" % sum(1,2,3,4,5))
print("sum:%d" % sum(1,2,3,4,5,6,7,8,9,10))

#如果有一个现成的list或者tuple 
#则可以在其变量前面加*号
target=[1,2,5,6]
print("sum:%d" % sum(*target))

#关键字参数
#dirt类型
#dirt类型为{}形式 存放的是key-value对

def person(name , age , **kw):
	if 'city' in kw:
		pass
	if 'sex' in kw:
		pass
	print(name , age ,kw)

person('fei' , 22)

person('mao' , 22 , sex='man')

person("yu" , 22 , sex='man' , city='xi\'an')

person("yu" , 22 , sex='man' , city='xi\'an' , like='games')

#如果有现成的dirt类型变量 也可以直接使用 需要前面加**
extra={'sex':'woman' , 'city':'xi\'an' , 'like':'dance'}
person('she' , 22 , **extra)

#对于传入的关键字参数 是不受任何限制的
#所以需要在函数内部进行检查 上面使用if进行检查


#命名关键字参数
#限制关键字参数的名字
#*是必须的 分隔符
#*后面的也可以使用默认参数
def person(name, age, *, city, job):
	print(name , age , city , job)


person('yu',22,city='xi\'an',job='student')

'''如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
	'''

#递归函数
def hh(number):
	if number == 1:
		return 1
	
	return number*hh(number-1)
	
print(hh(5))


def move(n,a,b,c):
	if n==1:
		print(a,'>',c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(5,'A','B','C')
