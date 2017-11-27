#list类型元素

array=['yu','fei','fei']
print(array)

#元素个数
len(array)

array[1]
array[-1]	#倒数第一个
array[-2]	#倒数第二个

array.append('mao')

array.insert(1,'hh')

print(array)

#删除末尾元素
array.pop()
print(array)
#删除指定位置元素
array.pop(1)
print(array)

#替换指定位置的元素为另一个元素
array[0]='this'
print(array)

#list类型也可以是多种类型元素的混合
mix=['yu',25,True]
print(mix)

#list嵌套list也可以
mixx=['fei',mix]
print(mixx)
mixx.append('ll')
#访问方式
#25
print(mixx[1][1])

#上述使用的是方括号 为list类型
#下述使用的是圆括号 为tuple类型 表示不可变（每个元素的指向不能再改变）

this=('haha','feifei')
#this.append
#this.insert
#上述方法均不存在

#mixx元素还是可以改变的
that=('feifei',mixx)

#空元素
elemet=()

#这是一个数字 不是tuple
t=(1)

#一个元素
tt=(1,)
print(tt)
#(1,)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])

#条件判断
number=100
if number<1:
	print('feifei')
elif number<20:
	print('ta')
else:
	print('yu')


#if 表达式:
#也可以 根据表达式的真假进行执行

year=input('birth year:')
#直接下面这样写 错误 str不可以与int比较
#if year<2000:
year=int(year)
if year<2000:
	print('young')
else:
	print('old')

#===================
print('BMI info')
height=input('height:')
height=float(height)

weight=input('weight:')
weight=float(weight)

bmi=weight/(height*height)
print('BMI:%.2f' %bmi)
if bmi<18.5:
	print('too thin')
elif bmi<25:
	print('formal')
elif bmi<28:
	print('over fat')
elif bmi<32:
	print('fat')
else:
	print('very fat')
#====================














