# -*- coding: utf-8 -*-
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

https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317848428125ae6aa24068b4c50a7e71501ab275d52000