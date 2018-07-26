
import random
'''
	发牌游戏
'''
puke_color = ('红桃', '梅花', '方片', '黑桃')
def puke_clear(puke, n):
	'''扑克牌，洗牌操作'''
	i = 0
	while i < 100:
		index1 = random.randint(0, n-1)
		index2 = random.randint(0, n-1)
		puke[index1], puke[index2] = puke[index2], puke[index1]
		i += 1	

def get_puke_value(pule_value):
	'''根据扑克的值，得到对应的扑克'''
	value = pule_value % 13	
	if value == 1:
		return 'A'
	if value > 1 and value < 11:
		return str(value)
	if value == 11:
		return 'J'	
	if value == 12:
		return 'Q'
	if value == 0:
		return 'K'

def get_puke_color(pule_value):
	'''根据扑克的值，得到花色'''
	return puke_color[(pule_value-1) // 13]
	
def puke_print(puke):
	'''打印扑克牌'''
	i = 0
	for elm in puke:		
		print("{:<7}".format(get_puke_color(elm)+get_puke_value(elm)), end=' ')
		i += 1
		if i % 12 == 0:
			print()
	print()

def puke_send(puke):
	'''发牌'''
	person_a, person_b, person_c, person_d = ([],[],[],[])
	for i in range(13):
		m = i * 4
		person_a.append(puke[m])
		person_b.append(puke[m+1])
		person_c.append(puke[m+2])
		person_d.append(puke[m+3])
	return (person_a, person_b, person_c, person_d)

def main():
	'''扑克中值1~13红桃， 14~26梅花, 27~39方片， 40~52黑桃'''
	puke = [i for i in range(1, 53)]
	
	# 洗牌
	puke_clear(puke, 52)
	
	# 打印
	puke_print(puke) # 红桃A  梅花2

	# 发牌 
	a, b, c, d = puke_send(puke) #for i in range(13):  m = i * 4  a-->puke[m] b--->puke[m+1] 
	print("小a:")	
	puke_print(a)

	print("小b:")	
	puke_print(b)

	print("小c:")	
	puke_print(c)

	print("小d:")	
	puke_print(d)
	'''
	# 查看每个人的发牌情况
	'''
if __name__ == '__main__':
	main()

