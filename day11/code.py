
import sys

'''
ASCII 127 (0111 1111)
ANCI
GBK
UNICODE 两字节 python 字符串
UTF-8 可变长的编码 python默认编码

转换:
	unicode--->其他 编码 encode()
	其他--->unicode 解码 decode()

'''

s = 'hello中国'
print(type(s), len(s))
s2 = s.encode('utf-8')
print(type(s2), len(s2))

s3 = s.encode('gbk')
print(type(s3), len(s3))

s1 = s2.decode('utf-8')
print(type(s1), len(s1))

# Python字符串
s1 = "hello午饭\n"
s2 = b'hello\n' # ascii bytes
s3 = r'hello午饭\n' # 不会按照字符串规则将字符串转义

print(type(s1), len(s1), s1)
print(type(s2), len(s2), s2)
print(type(s3), len(s3), s3)


print(sys.getdefaultencoding())



