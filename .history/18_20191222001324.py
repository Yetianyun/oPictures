#从图片上扣一块下来。并且分析哪个图是哪张纸。
#   _*_ coding:utf-8 _*_
__author__ = 'admin'
from PIL import Image, ImageDraw, ImageFont
import cv2
from aip import AipOcr
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

config = {
    'appId': '18062227',
    'apiKey': 'tGjhIBpcuMmMdf0WbsiKNjAp',
    'secretKey': '1VWhRnGpAGuzLEKUYFGXQRVwsbG8KUtt'
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
    result = '\n'.join(words_result)  #
    print(result)
    # # print(text)
    # rs = text.search(r'([一二三四五六七八九十]')
    # print(rs)
    # print(text["words_result"]["words"])