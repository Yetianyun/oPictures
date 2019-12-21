#获得这是第几张纸
#领航卷·全国卷·政治试题三第4页(共8页)
# import re

# result = "领航卷·全国卷·政治试题三第4页(共8页)"
# rs = re.search(r'([一二三四五六七八九十]',"",result)
# print(rs)



#!/usr/bin/python3
import re
 
# phone = "2004-959-559 # 这是一个电话号码"
phone = "领航卷·全国卷·政治试题三第4页(共8页)"
# 删除注释
num = re.match(r'([一二三四五六七八九十])',   re.M|re.I)
if matchObj:)
print ("电话号码 : ", num)
 
# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : ", num)
