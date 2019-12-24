#   _*_ coding:utf-8 _*_
#从图片上扣一块下来。并且分析哪个图是哪张纸。
__author__ = 'admin'
from PIL import Image, ImageDraw, ImageFont
import cv2
from aip import AipOcr
import re
import configparser
import os
import pymysql
import configparser

config = configparser.ConfigParser()
config.read("config/config.ini", encoding="utf-8")
baiduAppId = config.get("BaiduOCR", "appId")
baiduApiKey = config.get("BaiduOCR", "apiKey")
baiduSecretKey = config.get("BaiduOCR", "secretKey")

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

# if __name__ == '__main__':
#source_path 源文件目录
def read_source(source_path):
    num_dict = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9", "十": ""}
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    section = 'mysql'
    conf = {
        'host': config.get(section, 'host'),
        'port': config.getint(section, 'port'),
        'user': config.get(section, 'user'),
        'passwd': config.get(section, 'password'),
        'db': config.get(section, 'database'),
        'charset': config.get(section, 'charset')
    }
    conn = pymysql.connect(**conf)
    sql_insert = """insert into scan_file_info(pic_name, main_type, sub_type) values (%s,%s,%s)"""

    for scan_file in os.listdir(source_path):
        source_file_path = 'testPic/'+scan_file
        img = cv2.imread(source_file_path)
        sp = img.shape

        sz1 = sp[0]  # height(rows) of image
        sz2 = sp[1]  # width(colums) of image

        zuoshangX = 0
        zuoshangY = sz1 * 0.93
        youxiaX = sz2
        youxiaY = sz1

        im = Image.open(source_file_path)
        #   设置抠图区域
        box = (zuoshangX, zuoshangY, youxiaX, youxiaY)
        #   从图片上抠下此区域
        region = im.crop(box)
        newPic = "target_pic/pic_name.jpg"
        region.save(newPic, quality=95)

        api_result = img_to_str("target_pic/pic_name.jpg")
        words_result = (i['words'] for i in api_result['words_result'])  # 文本内容
        s = '\n'.join(words_result)  #
        # print(api_result)

        pattern1 = "([一二三四五六七八九十])"
        m1 = re.search(pattern1, s)
        main_type = num_dict[m1.group()]  # 主数据

        pattern2 = "([123456789])"
        m2 = re.search(pattern2,s) #次数据
        sub_type = m2.group()

        #在这里把"图片名称"及"图片序号"写进去。
        cursor = conn.cursor()
        cursor.execute(sql_insert, (scan_file, main_type, sub_type))
        #
    cursor.close()
    conn.commit()

if __name__ == '__main__':
    source_path = "testPic/"
    read_source(source_path)