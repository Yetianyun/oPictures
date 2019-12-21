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
print ( m1.group() )

