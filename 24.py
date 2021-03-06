#进一步切分图片
from PIL import Image
import os,cv2
import numpy as t

def splitPic(source_path):
    picNo = 0
    for scan_file in os.listdir(source_path):
        source_file_path = 'testPic/' + scan_file
        img = Image.open(source_file_path)
        info = img.size
        width = info[0]
        height = info[1]
        getWidth = t.zeros(width)
        for k in range(0,width):
            getWidth[k] = 0
        getWidth[0] += 1
        img = cv2.imread(source_file_path)
        # 查找页面中的分割线
        startHeight = int(height * 0.2)
        endHeight = int(height * 0.8) - 1
        startWidth = int(width * 0.35)
        endWidth = int(width * 0.7) - 1
        step = 15
        for row in range(startHeight,endHeight,step):  # 图片的高
            for col in range(startWidth,endWidth,step):  # 图片的宽
                channel1 = img[row][col][0]
                channel2 = img[row][col][1]
                channel3 = img[row][col][2]
                if ( ( channel1 >= 70 and channel1 <= 80 ) and
                     ( channel2 >= 70 and channel2 <= 80 ) and
                     ( channel3 >= 70 and channel3 <= 80 ) ):
                    m = 1 #表示可能是黑色
                else:
                    m = 0
                getWidth[col] += m
                # print(row, col, channel3)

        #求最大的col
        maxCol = 0
        for col in range(startWidth, endWidth, step):  # 图片的宽
            if ( getWidth[col] > maxCol ):
                maxCol = getWidth[col]
                maxColValue = col

        img = Image.open(source_file_path)
        img.crop((0, 0, maxColValue - 18, 3496)).save('target_pic/target_s_a_'+str(picNo)+'.jpg')
        img.crop((maxColValue + 18, 0, 2472, 3496)).save('target_pic/target_s_a_'+str(picNo+1)+'.jpg')
        picNo += 2

if __name__ == '__main__':
    source_path = "testPic/"
    splitPic(source_path)

