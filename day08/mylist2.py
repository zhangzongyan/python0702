
'''
	列表的常用函数
'''
ls = []

# 追加
ls.append(100)
print(ls)

# 向指定位置插入新的元素
ls.insert(0, 98)

ls.insert(1, 67)

ls.insert(15, 88) # 如果越界，则将新元素插入到最后
print(ls)

# 复制 深copy
l = ls.copy()
print(l)
print(ls)

l[0] = "wake up"
print(l)
print(ls)

# 浅copy 没有真正的复制列表
l2 = l
l2[0] = "tired"
print(l2)
print(l)

# 删除列表中的元素
del l2[2:]
print(l2)
print(l)

# 删除指定索引的元素
l.pop(0)
print(l)

# 移除指定元素
ls.remove(88)
print(ls)

# ls += l
ls.extend(l)
print(ls)

# 倒序
ls.reverse()
print(ls)

# 排序
ls = sorted(ls, reverse=True)
print(ls)


