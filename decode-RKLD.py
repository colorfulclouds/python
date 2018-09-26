# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 08:50:52 2018

@author: qq122
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
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756044276a15558a759ec43de8e30eb0ed169fb11000



