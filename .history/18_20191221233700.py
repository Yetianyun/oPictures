#从图片上扣一块下来。并且分析哪个是哪个。


#   _*_ coding:utf-8 _*_
__author__ = 'admin'
from PIL import Image, ImageDraw, ImageFont




file_path = 'testPic/2019-12-20-0101.jpg'

img = cv2.imread(fn)
sp = img.shape
im = Image.open(file_path)
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