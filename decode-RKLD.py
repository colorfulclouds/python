#!/usr/bin/env python3  #表示有这个解释器进行执行
# -*- coding: utf-8 -*- #该文件的编码格式

'a decoding and postview python file' #任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'me' #文件的作者姓名

#上面几行为python的标准编写格式

"""
Created on Wed Sep 26 08:50:52 2018

@author: qq122
Reference:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000
"""

tuple_instance=(1) #错误的写法 得到的是一个单纯的数字1 而不是tuple
tuple_instance=(1,) #这才是正确的tuple 且只有一个元素为1

boolean=True

if boolean == True:
    print('SS')
else:
    pass

if boolean:
    print('SS')
else:
    pass

#上面两种写法是一样的


#list类型可以增加元素或者减少元素
#tuple不能改变元素数量 也不能修改元素

apple=(1,2,3)
apple[0]=4 #错误

    
#dict类型一个key只能对应一个value 如果多次对一个key放不同value 会把前面的value冲调


dict_instance={'fei':52 , 'mao':55}

'fei' in dict_instance #判断是否在dict中

dict_instance.get('fei') #如果指定的key不存在 返回none 返回none在交互界面不显示
dict_instance.get('fei' , 5) #如果指定的key不存在 返回5 可以自己指定返回的元素

dict_instance.pop('fei') #在dict中删除元素



#dict类型的key必须是不可变类型元素 因为key唯一且要hash

key=[1,2,3]
dict_error={key:2,'fei':52} #错误



#set类型 集合
#set类型支持数学上的集合运算
s={1,2,3}
s.add(4)
s.remove(4)
#set中也不能有可变类型元素
key=[1,2,3]
s.add(key) #错误


#对于可变类型 可以修改其元素
#对于不可变类型 不可以修改其元素\
#即便使用其成员函数进行了修改 该函数也是\
#返回一个修改后的新的变量 原变量不变化

#help() 函数可以查看一个函数的用法


def func_no_return():
    a=2
    b=2
    
    c=a+b

#上面的函数没有return 但是有返回值为none

#空函数
def nop():
    pass #占位符的作用

#isinstance用来检查变量类型
def my_abs(number):
    if not isinstance(number , (int , float)):
        raise TypeError('type error')
    
    if number>=0:
        return number
    else:
        return -number
    

def return_multi():
    a=5
    b=4
    
    return a,b #实际返回一个tuple
    

#==========
#函数参数 多

#########
#位置参数
def square(x):
    return x*x

def add(x,y):
    return x+y

#########
#默认参数
def set_age(name , age=25):
    print(name , age)


#默认参数大坑展示
def add_end(L=[]):
    L.append('END')
    
    return L

add_end() #output:['END']
add_end() #output:['END','END']

#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容
#则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
#展示完毕

#修改如下
def add_end(L=None):
    if L is None:
        L = []
        
    L.append('END')
    return L

#因为str None是不可变类型 就不会被修改

#########
#可变参数 封装为tuple
def sum(*number): #number前面一个* number就接收了一个tuple
    x=0
    
    for n in number:
        x=x+n
    
    return x

sum(1,2,3,4)

LL=[1,2,3]
sum(LL[0],LL[1],LL[2]) #方式1
sum(*LL) #方式2 作为可变参数的形式传进去

   
############
#关键字参数 封装为dict

def person(uid , name , **kw):
    print(uid , name , kw)

info={'color':'red' , 'like':'pingpang'}
person(52 , 'feifei' , **info) #52 feifei {'color':'red' , 'like':'pingpang'}


###############
#命名关键字参数
#需要人为地检查kw中有什么
def person(uid , name , **kw):
    if 'color' in kw:
        pass
    
    if 'city' in kw:
        pass
    
    pass
#但是还是可以不受限制的传参数
#命名关键字参数来来了
#a>
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(uid , name , *args , color , like):
    pass

#必须传入参数名
person(52 , 'feifei' , 'haha' , 'heihei' , color='red' , like='pingpang')

#b>
#命名关键字参数可以有默认值
def person(uid , name , * , color='red' , like):
    print(uid , name , color , like)

person(52,'feifei' , like='pingpang')
person(52,'feifei',color='deep_red' ,like='pingpang')

#函数头部中 如果没有可变参数（*kg） 必须人为添加*符号

############
#参数组合
#参数顺序为： 必选参数 默认参数 可变参数 命名关键字参数 关键字参数
def person(uid , name ,age=52, *args , **kw):
    pass

def person(uid , name , age=52 , * , other , **kw ):
    pass

#递归函数
def digui(number):
    if number == 1:
        return 1
    
    return digui(number-1)*number


#尾递归 递归本身只占用一个栈帧
#在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def digui(number):
    return real_digui(number , 1)

def real_digui(number , product):
    if number == 1:
        return product
    
    return real_digui(number-1 , number*product)


#tuple支持切片 结果还是tuple 依然是不可变的

#判断是否为可迭代的
from collections import Iterable
isinstance([1,2,3] , Iterable) #判断list是否可迭代
isinstance(342 , Iterable)
    


for i,value in enumerate(['a','b','c']):
    print(i,value)
#output:
    #0 a
    #1 b
    #2 c


#for循环支持同时应用两个变量
for x ,y in [(2,3),(4,5),(2,2)]:
    print(x,y)
    

###########
#列表生成式
[x*x for x in range(1,11)]
#output:[1,4,9,16,25,36,49,64,81,100]

[x*x for x in range(1,11) if x%2 == 0]

[m+n for m in 'ABC' for n in 'XYZ']
#output:['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

############      
#生成器 generator
#利用某种算法将列表元素推算出来
#1>将列表生成式的中括号换为圆括号
L=(x*x for x in range(10)) #L变为了generator
next(L) #访问元素
next(L) #访问元素

#也可以使用for循环访问
#因为generator是可迭代的
for i in L:
    print(i)


#使用yield关键字将一个函数变为generator


#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def f():
    for i in range(10):
        yield i
    
for i in f():
    print(i)


def f_return():
    for i in range(10):
        yield i
    
    return 'sad' #for循环拿不到这个return值 需要异常StopIteration捕获才能拿到

gene=f_return()
while True:
    try:
        x = next(gene)
        print(x)
    except StopIteration as e:
        print('return value is:' , e.value)
        break

from collections import Iterable #可迭代对象
from collections import Iterator #迭代器

#可以直接作用于for循环的对象统称为可迭代对象Iterable


#生成器不但可以作用于for循环 还可以使用next函数不断调用来返回下一个值
#可以被next调用并不断返回下一个值的对象称为迭代器 Iterator
L=(x*x for x in range(10))
isinstance(L , Iterator) #True
isinstance('ddd' , Iterable) #True
isinstance('ddd' , Iterator) #False

          
#可以使用iter函数将Iterable变为Iterator

isinstance(iter('ddd') , Iterator) #True

                
#为什么list、dict、str等数据类型不是Iterator？

#这是因为Python的Iterator对象表示的是一个数据流，
#Iterator对象可以被next()函数调用并不断返回下一个数据，
#直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，
#但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
#所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

#迭代器详见下面的网址
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143178254193589df9c612d2449618ea460e7a672a366000

#函数式编程
#函数可以作为参数 也可以作为返回值


#高阶函数
#函数名也就是一个变量
#abs=10 abd函数名现在变成了一个整数
#如果想让这种变化在别的python文件中也生效 使用下面代码
import builtins
builtins.abs = 10

#也可以将函数作为参数传给另一个函数
def my_f(number):
    return number+2

def f(x,y,h):
    return h(x)+h(y)

f(2,3,my_f)

#map-reduce
#map函数接收两个参数 函数 和 Iterable类型的变量
#将结果作为新的Iterator返回

def square(number):
    return number*number

li = [1,2,3,4,5,6,7,8,9]

r_generator_iterator = map(square , li)

for r in r_generator_iterator:
    print(r)
    


#reduce函数的参数和map相同 但是reduce的第一个参数的函数有一个要求：这个函数必须有两个参数
#reduce函数的作用将结果和序列的下一个元素做累计运算
def add(x,y):
    return x+y

from functools import reduce
reduce(add , [1,2,3,4]) #返回10


#filter函数 参数与map类似
#作为filter第一个参数的函数的返回值是Boolean 以此来决定是保留还是丢弃该元素
#filter函数的返回值类型是Iterator
#函数的作用是进行元素过滤 将满足第一个参数对应函数的元素保留下来
def is_odd(number):
    return number%2 == 1 #余数为1 表明是奇数
    
lo=[1,2,3,4,5,6,7,8,9,10]
r_generator_iterator = filter(is_odd , lo)

for i in r_generator_iterator:
    print(i) #1 3 5 7 9


#排序算法
#内置的sorted

sorted([2,3,4,1,2,-5,6,-5]) #默认是升序排序

#使用绝对值函数作用后 再进行排序
sorted([2,3,4,1,2,-5,6,-5] ,   key=abs)


#sorted对字符串排序时 是按照ascii升序进行排序


#函数作为返回值
def lazy_sum(*args):
    def sum():
        ax=0
        
        for i in args:
            ax=ax+i
        
        return ax
    
    return sum

#内部函数可以引用外部函数lazy_sum的参数和局部变量
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中
#上述即“闭包”

f=lazy_sum(1,2,3,4,5) #返回一个函数
f() #这时候才是真正的计算结果

f1 = lazy_sum(1,2,3,4,5)
f2 = lazy_sum(1,2,3,4,5)

f1 == f2 #false

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

f1() #9
f2() #9
f3() #9
#全部都是9！原因就在于返回的函数引用了变量i，
#但它并非立刻执行。等到3个函数都返回时，
#它们所引用的变量i已经变成了3，因此最终结果为9。
  
#使用闭包时 返回的函数不要引用任何循环变量 或者后续会发生变化的变量
 
#上面出现的情况 可以像下面这样写
def count():
    def f(j):
        def g():
            return j*j
        
        return g
    
    fs=[]
    
    for i in range(1,4):
        fs.append(f(i))
        
    return fs

f1, f2, f3 = count()

f1() #1
f2() #4
f3() #9

#闭包详细见下地址
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000
 
 
#匿名函数
#lambda 用来制造匿名函数
#匿名函数有一个限制 只有一个表达式 不写return 返回值就是表达式的结果 
#不必担心函数名冲突
#可以将其赋值给另一个变量 再利用变量来调用函数

map(lambda x: x*x , [1,2,3,4])

square = lambda x: x*x
square(2)

def func_buildin_func(x,y):
    return lambda: x*x+y*y
 
 
#装饰器
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000

def function():
    print(52)

function.__name__ #返回函数的名字

#在代码运行期间动态增加功能的方式 称之为 装饰器
#装饰器 decorator是一个返回函数的高阶函数

#定义一个打印日志的decorator
def log(func):
    def wrapper(*args , **kw):
        print('call %s()' % func.__name__)
        
        return func(*args , **kw)
    
    return wrapper

#上面的log函数 是一个decorator  接收一个函数作为参数 并返回一个函数
#使用python @符号语法
@log
def function():
    print(52)

function()
#output:
    #call function()
    #52


#放了一个@log 相当于执行了function=log(function)
'''
由于log()是一个decorator，返回一个函数，
所以，原来的function()函数仍然存在，
只是现在同名的function变量指向了新的函数，
于是调用function()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，
因此，wrapper()函数可以接受任意参数的调用。
在wrapper()函数内，首先打印日志，再紧接着调用原始函数
'''

#decorator自身也可以有参数传入 此时需要一个返回decorator的高阶函数
def log(text): #这里的传入参数为text
    def decorator(func):
        def wrapper(*args , **kw):
            print('%s %s()' % (text , func.__name__))
            
            return func(*args , **kw)
        
        return wrapper
    
    return decorator

@log('feifei')
def function():
    print(52)

function()  
#output:
    #feifei function()
    #52

#执行实质为log('feifei')(function)
#首先执行log('execute')，返回的是decorator函数，
#再调用返回的函数，参数是function函数，返回值最终是wrapper函数。


#上面的两种嵌套 都将wrapper赋给了function函数
#所以function.__name__ = wrapper 而不是function

#可以人为地写wrapper.__name__ = function.__name__


#python内置了
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        
        return func(*args , **kw)
    
    return wrapper


def log(text): #这里的传入参数为text
    def decorator(func):
        @functools.wraps
        def wrapper(*args , **kw):
            print('%s %s()' % (text , func.__name__))
            
            return func(*args , **kw)
        
        return wrapper
    
    return decorator


#上面即可保证由wrapper赋给function函数之后
#function.__name__ = function



#偏函数
#见
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000

int('123') #将字符串的‘123’变为int类型

int('123' , base=8) #base为转换进制

int('10101011' , base=2) #二进制转换

#如果频繁使用2进制转换的话 不妨单独写一个函数 专门用来二进制转换

import functools

int2 = functools.partial(int , base=2) #int2函数就变成了专门做二进制转换的函数了

#上面写法相当于
kw = {'base':2}
int('1001010',**kw)

                    
#另一个例子
max2=functools.partial(max , 10)

max2(5,6,7)
#相当于
args=(10,5,6,7)
max(*args)

#模块篇章
#python防止模块的名字相同 引入了按目录来组织模块的方法 称为 包 package
#包 本质就是一个目录 这个目录里面放有一些python 模块py文件
#包名也不能和别的包名冲突

#包 目录下必须包含 __init__.py文件 可以是一个空文件

#引用方式 包名.模块名

import sys
sys.argv #这个成员变量 用list存储了命令行的所有参数
#这个变量至少有一个元素 因为一第一个参数永远是该python文件

#在模块文件一般有下面代码行
if __name__ == '__main__':
    #do something

#在命令行运行模块python文件时 
#python解释器会将python模块文件的特殊变量__name__置为__main__
#而在其他地方导入模块文件时 if判断就会失败

#下面两个规则只是针对python模块而言的
#__xxx__ 前后两个下划线的为 特殊变量 避免这样的命名
#_xxx 前面一个下划线 为私有的 不应该直接引用

sys.path #python在这些路径下搜索模块文件
#可以自行修改python的模块搜索路径
#1> sys.path.append('self path') #运行时修改 运行结束后失效
#2> 修改环境变量 PYTHONPATH #只需要添加自己的路径即可 python自身的搜索路径不受影响



#class 面向对象 OOP

class Student(object):
    pass

feifei = Student()
feifei.age = 23 #可以自由地给变量绑定属性

class Student(object):
    def __init__(self , name , age):
        self.name = name
        self.age = age


#上面的类定义方法 其成员变量是public 外部还是可以访问
class Student(object):
    def __init__(self , name , age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self , new_name):
        self.__name = new_name
    
    def set_age(self , new_age):
        pass
    
    
#变量前加两个下划线 就变成了私有变量 代码更加健壮
#增加get set方法访问私有变量



#__xxx__ 前后两个下划线的这种变量是特殊变量 特殊变量是可以直接访问的 它不是私有变量
#_xxx 前面只有一个下划线的变量 还是可以直接访问的 但是约定俗成 “可以被访问 但视为私有变量 不要随意访问”

#__xxx 前面两个下划线的变量实质是python解释器将其进行了修改为 _类名__xxx
#所以仍然可以通过 _类名__xxx进行访问

'''
>>> bart = Student('Bart Simpson', 59)
>>> bart.get_name()
'Bart Simpson'
>>> bart.__name = 'New Name' # 设置__name变量！
>>> bart.__name
'New Name'

#表面上看，外部代码“成功”地设置了__name变量，
#但实际上这个__name变量和class内部的__name变量不是一个变量！
#内部的__name变量已经被Python解释器自动改成了_Student__name，
#而外部代码给bart新增了一个__name变量。不信试试
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
'''


#继承与多态
class Animal(object):
    def run(self):
        print('running')

class Cat(Animal):
    def run(self):
        print('cat running')
    
class Dog(Animal):
    def run(self):
        print('dog running')


mi = Cat()
mi.run() #Cat实例中的run方法会将Animal中的run方法覆盖掉 即多态

isinstance(mi , Animal) #True
isinstance(mi , Cat) #True
#mi既是Animal类类型 又是Cat类类型

#多态的演示见下地址
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431865288798deef438d865e4c2985acff7e9fad15e3000
#动态语言的鸭子类型 见上地址


import types

def function():
    pass

type(function) == types.FunctionType #True

type(abs) == types.BuiltinFunctionType #True

type(lambda x: x) == types.LambdaType #True

type((x for x in range(10))) == types.GeneratorType
    

#object>Animal>Dog
d=Dog()

type(d) #Dog类类型

isinstance(d , Dog) #True
isinstance(d , Animal) #True


#判断[1,2,3]是否是list或是tuple
isinstance([1,2,3] , (list , tuple)) #True


#dir函数返回一个对象的所有属性和方法
dir('ABC')

#__xxx__ 这种名字的属性和方法是有特殊用途的
#__len__ 方法返回长度
#使用len函数试图获取对象长度的时候 实际在len函数内部 自动去调用__len__方法

len('ABC')
#上下两种写法是一样的
'ABC'.__len__()



#如果想让len函数能够作用自己写的类 就在类中实现__len__方法即可
class Dog(Animal):
    
    def __len__(self):
        return 52
    

dog = Dog()
len(dog) #返回52


getattr() #获取对象属性
setattr() #设置对象属性
hasattr() #判断对象是否有指定的属性


#正确的一个写法示例
def readImage(fp): #从fp文件流中读取图像
    if hasattr(fp , 'read'): #先判断是否有这个属性 然后再决定能否调用
        return readData(fp)
    
    return None


#属性和类属性
class Student(object):
    name='feifei'
    
    def __init__(self):
        pass
    

print(Student.name) #'feifei'

s = Student()
print(s.name) #'feifei'

s.name='aaa'
print(s.name) #'aaa' 将类属性屏蔽掉了 

print(Student.name) #'feifei' 实例属性不影响类属性

#类属性由所有的类实例共享

#面向对象高级编程

#对一个类实例可以绑定属性和方法
#但是类的另一个实例不起作用
class Student(object):
    pass

s = Student()
s.name = 'feifei'
print(s.name) #'feifei'

#定义一个函数作为一个实例的方法
def set_age(self , age):
    self.age = age
     
from types import MethodType

s.set_age = MethodType(set_age , s) #给实例绑定方法
s.set_age(52)
print(s.age) #52


#如果需要给所有实例绑定属性和方法 可以给class绑定方法 那么这个class的所有实例都能使用
def set_score(self , score):
    self.score = score


Student.set_score = set_score

s1 = Student()
s2 = Student()

s1.set_score(52)
s2.set_score(52)


#限制实例的属性 只允许对类的实例添加指定的属性
class Student(object):
    __slots__ = ('name' , 'age') #只能添加name和age属性

    def __init__(self):
        pass
    

s = Student()
s.name='feifei'
s.age = 52
s.score=100 #error 不能绑定 __slots__没有指定

#__slots__中的指定的属性只对当前类实例起作用 子类不起作用
class sub_Student(Student):
    pass

sub_s = sub_Student()
sub_s.score = 100 #正常 没有错误

#除非在子类中也定义__slots__ 这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


#python内置的@property装饰器负责把一个方法变成属性调用

class Student(object):
    #添加@property就将getter方法变成了属性
    @property
    def score(self):
        return self._score
    
    #@property自身创建另一个装饰器@score.setter 负责将setter方法变成属性赋值
    @score.setter
    def score(self , value):
        if not isinstance(value , int):
            raise ValueError('score must be an integer')
        if value<0 or value>100:
            raise ValueError('must between 0-100')

        self._score = value


s = Student()
s.score = 52 #s.set_score(52)方法
print(s.score) #s.get_score()方法


class Student(object):
    @property
    def birth():
        return self._birth
    
    @birth.setter
    def birth(self , value):
        self._birth = value
 
    #age只是一个可读属性       
    @property
    def age(self):
        return 2015-self._birth
    
    
#继承 python有单继承与多继承
class Animal(object):
    pass

class Mammal(object):
    pass

class Swimmed(object):
    pass

#下面这种设计称为MixIn
class Dog(Animal , Mammal , Swimmed):
    pass

class MammalMixIn(object):
    pass

class SwimmedMixIn(object):
    pass

#故可以给类名添加MixIn
class Dog(Animal , MammalMixIn , SwimmedMixIn):
    pass

     
#定制类 内容较多     
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
class Student(object):
    def __init__(self , name):
        self.name = name
        
print(Student('feifei')) #打印的是一个地址信息

class Student(object):
    def __init__(self , name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name:%s)' % self.name

#下面打印时 会去调用__str__函数
print(Student('feifei')) #'Student object (name:feifei)'
     
#但是尽管类中实现了__str__函数
#直接显示变量
s=Student('feifei')
s #这种调用方式 打印的还是地址信息 这种方式调用的类中的__repr__函数

#__str__是给用户看的
#__repr__是给程序开发者看的 
#但通常两者的代码是一样的
#下面是偷懒写法
class Student(object):
    def __init__(self , name):
        self.name = name
    
    def __str__(self):
        return 'Student object (name:%s)' % self.name
    
    __repr__ = __str__



#一个类想被用于for in循环 类似list或tuple那样
#需要实现__iter__方法和__next__方法
class Fib(object):
    def __init__(self):
        self.a , self.b = 0 , 1
    
    def __iter__(self):
        return self #实例本身即迭代对象 所以返回自己

    def __next__(self):
        self.a , self.b = self.b , self.a+self.b
        
        if self.a>100000: #终止循环
            raise StopIteration()
        
        return self.a

#for循环不断调用迭代对象的__next__方法
#可以打印斐波那契数列了
for n in Fib():
    print(n)

#上面的Fib类实例可以用于for循环 和list有点像 但是不能像list那样按照下标取出元素
#使用下标取出元素 需要实现__getitem__方法
class Fib(object):
    def __getitem__(self , n):
        a,b = 1, 1
        
        for x in range(n):
            a,b = b,a+b
        
        return a

f=Fib()
#可以使用下标访问了
f[0]
f[1]
f[2]

#list支持切片操作
#上面Fib类实例还是不支持
#要在__getitem__中对参数n进行判断 是否为切片对象 slice

class Fib(object):
    def __getitem__(self , n):
        if isinstance(n , int):
            a,b = 1, 1
        
            for x in range(n):
                a,b = b,a+b
            
            return a
        
        if isinstance(n , slice):
            start = n.start
            stop = n.stop
            #如果要补全功能 还要对n.step参数进行处理
            
            if start is None: #[:5] 这种情况就是start为none 
                start = 0
            #还需要补充stop为none的情况 即[5:] stop为none
            
            a,b = 1,1
            L = []
            
            for x in range(stop):
                if x>=start:
                    L.append(a)
                
                a,b = b,a+b
            
            return L

f = Fib()
f[0:5]

f[:5]



#如果将类实例看作dict 则__getitem__参数就可以是key 例如str

#__setitem__方法可以将对象当做list或dict对其赋值
#__delitem__删除元素


class Student(object):
    def __init__(self):
        self.name = 'feifei'
        
s = Student()
print(s.name)

print(s.score) #没有这个属性 引发错误 attributeerror


#__getattr__方法 动态返回一个属性或者函数
class Student(object):
    def __init__(self):
        self.name = 'feifei'
        
    def __getattr__(self , attr):
        if attr == 'score': #动态返回属性
            return 99
        
        if attr == 'age': #动态返回函数
            return lambda: 52
    
print(s.score)
s.age()

#让s调用s.abc s.xyz这种在__getattr__中不存在的就会返回none
#python函数不写return就会返回none
#所以需要抛出错误

class Student(object):
    def __getattr__(self , attr):
        if attr == 'score':
            return 99
        
        if attr == 'age':
            return lambda: 25

        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


#使用实例名进行调用
class Student(object):
    def __init__(self , name):
        self.name = name
        
    def __call__(self):
        print('feifei')
        
s=Student()
s() #这里调用得到是__call__方法

 
#模糊了对象与函数的界限
#有时候需要判断一个对象是否能够被调用
#能够被调用的对象就是一个Callable对象 例如带有__call__方法的类实例
#使用callable进行判断
callable(Student())
callable(max)
callable('feifei')
 
 
#枚举类
from enum import Enum
Month = Enum('Month' , ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#自动赋值 默认从1开始计数
Month.Jan #引用常量

for name , member in Month.__members__.items():
    print(name , member , member.value)
#Jan Month.Jan 1
#Feb Month.Feb 2
#Mar Month.Mar 3
#......

#通过继承的手段派生自定义类
from eunm import Enum , unique

@unique #检查保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


#元类
class Hello(object):
    def hello(self , name='world'):
        print('hello' , name)
    
type(Hello) #输出为class 'type'
#Hello的类型是类 类型 就好比C语言中的struct union一样
#先定义类类型 在定义变量

h = Hello()
type(h) #类型是Hello类型


#type函数可以返回对象的类型 也可以创建出新的类型

def fn(self , name='world'):
    print('hello' , name)

#下面就创建了一个类类型
Hello=type('Hello' , (object,), dict(hello=fn))

#使用type函数创建类类型 需要3个参数
#class名称 继承的父类集合（只有一个父类 注意tuple单元素写法） class方法名与函数绑定

#python在遇到class定义时 只是检查语法后 就去调用type函数创建类 类型
#type函数允许动态创建类

#metaclass
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319106919344c4ef8b1e04c48778bb45796e0335839000








