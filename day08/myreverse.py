
'''
将字符串逆序
'''
def myreverse(s):
	if s == '':
		return '' 
	return myreverse(s[1:])+s[0]

print(myreverse("hello"))
print(reversed("hello"))


