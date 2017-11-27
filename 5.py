from collections import Iterable
import os
#高级特性
#切片 slice


L=['yu' , 'fei' , 'mao' , 'haha']

print(L[0] , L[1])
print(L[0] , L[1] , L[1])

#L[i:j] 可以一次性取出多个元素
#如果i=0 可以省略
print(L[:3])

print(L[-1:])
#haha
print(L[-2:])
#mao haha
print(L[-2:-1])
#mao

number=[1,2,3,4,5,6,7,8,9,10]
print(number[::2])	#每两个数字取一个 pos+2
print(number[:5:2])	#前35个数字每两个取一个

#迭代 遍历
find={'name':'yu' , 'hh':'fei' , 'sex':'man'}
for key in find:
	print(key)
print('===')
for value in find.values():
	print(value)
print('===')
for keyt , valuet in find.items():
	print(keyt,':',valuet)


#判断str类型是否支持迭代
answer = isinstance('abc' , Iterable)
print(answer)


#使用enumerate函数将list类型变为index-element类型

for index , value in enumerate(['A','B','C']):
	print(index , value)

#列表生成式
l=list(range(1,11))
print(l)

l=[]
for x in range(1,11):
	l.append(x*x)
print(l)

#和上面的意思一样
l=[x*x for x in range(1,11)]
print(l)

l=[x*x for x in range(1,11) if x % 2 == 0]
print (l)

#列出当前目录下的文件和目录名字
l=[d for d in os.listdir('.')]
print(l)

#转换为小写
l=['A','B']
l=[s.lower() for s in l]
print(l)

l1=['Hello','World',18,'Apple',None]
l2=[s.lower() for s in l1 if isinstance(s , str) == True]
print(l2)



























