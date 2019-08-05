#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#解释器
#按utf-8读取

print("hello world")

print("this","is","a","string test")

print("100+200=",100+200)
'''
#input your name
name = input()
print("hello" ,name)
'''

#print("1024*768=",1024*768)
#冒号结尾  缩进的语句视为代码块

number=10
if number>0:
	print(number)
else:
	print("hh")
	
print("i am ok")
print('i am ok')

print("i'm ok")
print("i \" am ok")
print('\\\\')

print(r"dfs\sfd")

#需要换行太多 加入太多\n不易阅读 所以使用'''...''' 前面也可以使用r'''...'''
print('''this
is
a
test''')

print(r'''hhh
\\
kk
''')

if(True):
	print("real")
else:
	print("false")


print(123)
print(456.789)
print("hello, world")
print("hello, \\\'Adam\\\'")
print(r"hello, Bart")
print(r'''hello
lisa!''')

#Python字符串
#字符处理
#字符情况
print("UTF编码 中文测试")

#获取字符的整数表示
print(ord('A'))
print(ord('中'))
#把整数变成相应的字符
print(chr(66))
print(chr(25991))
	
	

#Python字符串是str类型
#内存中Unicode表示
#一个字符对应若干个字节 bytes
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：

#encode方法将编码变为指定的bytes
'ABC'.encode('ascii')

'中文'.encode('utf-8')

#下面的写法错误 因为ascii支持不到中文
#'中文'.encode('ascii')
	
#decode 可以将bytes变为str

b'ABC'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

#计算str多少个字符 使用len函数
len('ABC')
#3
len('中文')
#2

#计算bytes的字节数 还是使用len函数
len(b'ABC')
#3
len('中文'.encode('utf-8'))
#6 一个汉字占6个字节


#格式化输出
print("hello %s age:%d" %("haha",22))

print("小明成绩提高问题")

s1=72
s2=85

delta=s2-s1
r=delta/s2
print("add:%2f" %r)























	
	
	
	
