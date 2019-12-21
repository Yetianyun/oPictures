#从图片上扣一块下来。并且分析哪个是哪个。


#   _*_ coding:utf-8 _*_
__author__ = 'admin'
 
from PIL import Image, ImageDraw, ImageFont
im = Image.open(r"C:\Users\admin\Desktop\copy.png")
#   设置抠图区域
box = (1119, 219, 505, 90)
#   从图片上抠下此区域
region = im.crop(box)
#   将此区域旋转180度
region = region.transpose(Image.ROTATE_180)
#   查看抠出来的区域
# region.show()
#   将此区域粘回去
im.paste(region, box)
im.show()
————————————————
版权声明：本文为CSDN博主「FloatDreamed」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/FloatDreamed/article/details/79027462