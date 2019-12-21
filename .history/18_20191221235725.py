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
newPic = "testPic/pic_name.jpg"
region.save(newPic, quality=95)

#使用百度OCR来OCR这些图片
