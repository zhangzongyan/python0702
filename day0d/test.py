
class A(object):
	def __init__(self):
		print("A")

class B(A):
	pass 

class C(A):
	def __init__(self):
		print("C")
        

class D(B,C):
	pass

# 继承关系，广度优先
d = D()

