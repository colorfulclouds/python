#求和函数 可变参数
def cal_sum(*args):
	ax = 0
	
	for n in args:
		ax = ax + n
	
	return ax

print(cal_sum(10,12,4234,324))

#函数式编程
#函数作为返回值

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		
		return ax
	
	return sum

f = lazy_sum(1,2,5,2)
print(f)