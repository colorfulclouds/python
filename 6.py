#python函数式编程
#传入一个函数 返回一个函数
#abs是个函数名字
#函数名也是变量！
#所以可以将abs=10
#那么abs就不能作为绝对值函数使用了

f=abs

x = f(-10)
print(x)

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(a , b , f):
	return f(a) + f(b)

x = add(-1,-2,abs)
print(x)
#x=3

#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def square(x):
	return x*x

#下面返回一个list对象
result = map(square , [1,2,3])
print(list(result))
#map也可以整批完成类型转化

haha = map(str , [1,2,3])
print(list(haha))

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
from functools import reduce
def add(a , b):
	return a+b
#利用reduce求和
sum = reduce(add , [1,1,2])
print(sum) 

#上述也可以利用内置函数sum

#下面是合起来使用 将str类型转换为int类型
def fn(x , y):
	return x*10+y

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

result = reduce(fn , map(char2num , '13579'))
print(isinstance(result , int))
print(result)

#不规范的英文名字转换为规范的 首字母大写 其余小写
def normalize(s):
	t = s.lower()
	w = str(t[0]).upper()
	g = w+t[1:]
	return g

l1 = ['adam' , 'LISA' , 'bAr']
l2 = list(map(normalize , l1))
print(l2)

#reduce求积
def mull(x , y):
	return x*y

def prod(l):
	return reduce(mull , l)

result = prod([1,2,4,5])
print(result)


#python函数 filter函数可以用来过滤序列
#是高级函数

#和map()类似，filter()也接收一个函数和一个序列。
#和map()不同的是，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素

#下面是删除偶数 保留奇数
def is_odd(n):
	return n%2 == 1

result = list(filter(is_odd , [1,2,3,4,5,5,6]))
print(result)

#利用filter删除空字符串
def not_empty(s):
	return s and s.strip()

result = list(filter(not_empty , ['AAA' , '' , None]))
print(result)

#yield 生成器使用 
#继续上一次 退出的地方开始执行

a='asdfsd'
a[::-1]
#上面的写法会将字符串逆序 因为最后一个数字为负数

#sorted也是高阶函数
result = sorted([1,2,3,443,4])
print(result)

#反序
result = sorted([-1,-2,3,-443,4] , reverse = True)
print(result)

#然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：
#下面的输出结果
#-1 -2 3 4 -443
result = sorted([-1,-2,3,-443,4] , key = abs)
print(result)

#按照ASCII排序
result = sorted(['dg','DasS' , 'as' , 'sdf'])
print(result)

#忽略大小写排序
result = sorted(['dg','DasS' , 'as' , 'sdf'] , key = str.lower)
print(result)

#学生信息排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def get(s):
	return s[0].lower()

result = sorted(L , key = get)
print(result)

def get_score(s):
	return s[1]

result = sorted(L , key = get_score)
print(result)

