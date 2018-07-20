import jieba

s = "python is the most popular language"
l = s.split()
print(l)

s2 = "中华人民共和国是最伟大的国家"
l2 = jieba.lcut(s2, cut_all=True)
print(l2)

