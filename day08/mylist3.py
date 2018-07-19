
'''
	列表做函数形参:
		如果函数的默认参数是一个列表，多次调用用的时候，如果使用默认值,用的是同一个	
'''

def test(num, ls=[]):
	ls.append(num)
	return ls

l1 = test(10)
l2 = test(123, ["hello"])
l3 = test('a')
l4 = test('world')

print(l1) 
print(l2)
print(l3)

l3[2] = 1000
print(l3)
print(l1)

