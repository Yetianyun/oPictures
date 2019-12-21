#获得这是第几张纸
#!/usr/bin/python3
import re

s = "领航卷·全国卷·政治试题三第4页(共8页)"
pattern1 = "([一二三四五六七八九十])"
m1 = re.search(pattern1,s)
t1 = m1.group()
print ( t1 )


pattern2 = "([123456789])"
m2 = re.search(pattern2,s)


