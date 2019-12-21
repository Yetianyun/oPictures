#从图片上扣一块下来。并且分析哪个图是哪张纸。
#   _*_ coding:utf-8 _*_
__author__ = 'admin'
from PIL import Image, ImageDraw, ImageFont
import cv2

file_path = 'testPic/2019-12-20-0101.jpg'
img = cv2.imread(file_path)
sp = img.shape

sz1 = sp[0]#height(rows) of image
sz2 = sp[1]#width(colums) of image

zuoshangX = 0
zuoshangY = sz1 * 0.93
youxiaX = sz2
youxiaY = sz1 

im = Image.open(file_path)
#   设置抠图区域
box = (zuoshangX, zuoshangY, youxiaX, youxiaY)
#   从图片上抠下此区域
region = im.crop(box)
region.show()

#将这个图存下来


# #   将此区域旋转180度
# region = region.transpose(Image.ROTATE_180)
# #   查看抠出来的区域
# # region.show()
# #   将此区域粘回去
# im.paste(region, box)
# im.show()