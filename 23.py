#   _*_ coding:utf-8 _*_
#将数据存入数据库，本代码是处理"答案"的
__author__ = 'admin'
from PIL import Image, ImageDraw, ImageFont
import cv2
from aip import AipOcr
import re
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
    sql_insert = """insert into scan_file_info(pic_name, main_type, sub_type,is_answer) values (%s,%s,%s,%s)"""

    for scan_file in os.listdir(source_path):
        print("scan_file:"+scan_file)
        source_file_path = 'testPic/'+scan_file
        img = cv2.imread(source_file_path)
        sp = img.shape

        sz1 = sp[0]  # height(rows) of image
        sz2 = sp[1]  # width(colums) of image

        zuoshangX = 0
        zuoshangY = sz1 * 0.93 #高度
        youxiaX = sz2
        youxiaY = sz1

        im = Image.open(source_file_path)
        #   设置抠图区域
        box = (zuoshangX, zuoshangY, youxiaX, youxiaY)
        region = im.crop(box)
        newPic = "target_pic/pic_name.jpg"
        region.save(newPic, quality=95)

        api_result = img_to_str("target_pic/pic_name.jpg")
        words_result = (i['words'] for i in api_result['words_result'])  # 文本内容
        s = '\n'.join(words_result)  #
        print(s)

        # pattern0 = "([答案])"
        # m0 = re.search(pattern0, s)
        if ( "答案" in s ) :
            # print("答案")
            # return
            pattern1 = "([一二三四五六七八九十])"
            m1 = re.search(pattern1, s)
            sub_type = num_dict[m1.group()]  # 次数据

            pattern2 = "([123456789])"
            m2 = re.search(pattern2, s)  # 主数据
            main_type = m2.group()
            is_answer = 1 #是答案
            print(sub_type,main_type)

            #左右分离图片
            im = Image.open(source_file_path)
            im.crop((0, 0,2472/2, 3496)).save('target_pic/target_a_1.jpg')
            im.crop((2472/2+1, 0,2472, 3496)).save('target_pic/target_a_2.jpg')

            width = img.shape[1]
            channels = img.shape[2]
            #查找页面中的分割线
            for row in range(img.shape[0]):  # 图片的高
                for col in range(img.shape[1]):  # 图片的宽
                    pixel = 0
                    for channel in range(channels):
                        pixel = pixel * 1000 + img[row][col][channel]
                    pixel = int(pixel / 10000000) * 1000000
                    print(row,col,pixel)
                print("\n")
            #此功能没有完成，可以划一个部分然后再寻找

        else:
            pattern1 = "([一二三四五六七八九十])"
            m1 = re.search(pattern1, s)
            main_type = num_dict[m1.group()]  # 主数据

            pattern2 = "([123456789])"
            m2 = re.search(pattern2,s) #次数据
            sub_type = m2.group()
            is_answer = 0 #不是答案

        #在这里把"图片名称"及"图片序号"写进去。
        cursor = conn.cursor()
        cursor.execute(sql_insert, (scan_file, main_type, sub_type, is_answer))
    cursor.close()
    conn.commit()

if __name__ == '__main__':
    source_path = "testPic/"
    read_source(source_path)