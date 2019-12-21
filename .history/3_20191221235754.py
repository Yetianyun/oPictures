#基于百度ocr的测试
from aip import AipOcr
import configparser

config = {
    'appId': '',
    'apiKey': '',
    'secretKey': ''
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
    text = img_to_str('sourceImages/testOcr.png')
    print(text)