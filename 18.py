#从图片上扣一块下来。并且分析哪个图是哪张纸。
#   _*_ coding:utf-8 _*_
__author__ = 'admin'
from PIL import Image, ImageDraw, ImageFont
import cv2
from aip import AipOcr
import configparser
import re
import configparser

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

config = configparser.ConfigParser()
config.read("./config.ini", encoding="utf-8")
baiduAppId = config.get("baiduOCR", "appId")
baiduApiKey = config.get("baiduOCR", "apiKey")
baiduSecretKey = config.get("baiduOCR", "secretKey")

config = {
    'appId': baiduAppId,
    'apiKey': baiduApiKey,
    'secretKey': baiduSecretKey
}

client = AipOcr(**config)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    # 通用文字识别（可以根据需求进行更改）
    result = client.basicGeneral(image)
    return result

if __name__ == '__main__':
    api_result = img_to_str("testPic/pic_name.jpg")
    words_result = (i['words'] for i in api_result['words_result'])  # 文本内容
    s = '\n'.join(words_result)  #
    # print(api_result)

    pattern1 = "([一二三四五六七八九十])"
    m1 = re.search(pattern1,s)
    t1 = m1.group()
    print ( t1 )

    pattern2 = "([123456789])"
    m2 = re.search(pattern2,s)
    t2 = m2.group()
    print ( t2 )
