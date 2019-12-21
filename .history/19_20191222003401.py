#获得这是第几张纸
#领航卷·全国卷·政治试题三第4页(共8页)
# import re

# result = "领航卷·全国卷·政治试题三第4页(共8页)"
# rs = re.search(r'([一二三四五六七八九十]',"",result)
# print(rs)



#!/usr/bin/python3
import re

phone = "领航卷·全国卷·政治试题三第4页(共8页)"
pattern1 = "([一二三四五六七八九十])"
m1 = re.search(pattern1,s)
print ( m1.group()



 
# # phone = "2004-959-559 # 这是一个电话号码"
phone = "领航卷·全国卷·政治试题三第4页(共8页)"
# 删除注释
num = re.findall(r'([一二三四五六七八九十])',   re.M|re.I)


 m1 = re.search(pattern1,s)
>>> m1.group()


# print(num) 
# # 移除非数字的内容
# num = re.sub(r'\D', "", phone)
# print ("电话号码 : ", num)
