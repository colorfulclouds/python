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










