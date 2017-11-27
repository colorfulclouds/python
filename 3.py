#循环
#for循环

names=['fei','yu','maomao']
for name in names:
	print(name)

#计算1-100的和
#list(range())构造一个list 类似于构造函数
sum=0
#下面两种写法一样的
#for number in range(101):
for number in list(range(101)):
	sum+=number
print("sum:%d" % sum)


#欢迎信息
L = ['Bart', 'Lisa', 'Adam']

for name in L:
	print("hello,%s" %name)

n=1
while n<=5:
	print('love')
	n+=1;
#Python中break和continue和c/c++是一样的

#dirt c++中的map

d={'yu':12,'fei':21,'mao':44}
print(d['fei'])

#可以修改值的
#对同一个key连续赋值
#后面的新值会把前面的旧值冲掉
d['fei']=100
print(d['fei'])

#判断是否在dirt中
'haha' in d
#False
#第二种方法
d.get('haha')
#None
d.get('haha',-1)
#-1

d.pop('yu')	#delete
print(d)

#dirt只能放不可变元素
#故下面报错
#key=[1,2,3]
#d[key]='all'
d[(1,2,3)]='this'
#下面的不行[2,3]不能hash
#d[(1,[2,3])]='that'
print(d)

#set类型
#构造过程 使用了一list
s=set([1,2,3])
print(s)
#下面的不行[2,3]不能hash
#s.add((1,[2,3]))
s.add((1,2,3))
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1&s2
s1|s2












	
