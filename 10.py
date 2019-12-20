# #获得图像的每个像素的值
# import os
# import cv2
# import numpy as np

# # np.set_printoptions(threshold=np.nan)    # 这里多加一行代码，避免控制台输出省略号的问题
# 
# filepath = '/Users/leaf/project/scanWords/testPic/'
# for filename in os.listdir(filepath):
#     print(filename)
#     # img = cv2.imread('/Users/leaf/project/scanWords/testPic/%s'%filename)
#     # print(img.shape[0]+"////"+img.shape[1])
#     # for x in range(img.shape[0]):   # 图片的高
#     #     for y in range(img.shape[1]):   # 图片的宽
#     #         px = img[x,y]
#     #         print(px)    # 这样就能得到每个点的bgr值


import os
import cv2
import math
import random
import numpy as np
from scipy import misc, ndimage


def access_pixels(frame):
    print(frame.shape)  #shape内包含三个元素：按顺序为高、宽、通道数
    height = frame.shape[0]
    weight = frame.shape[1]
    channels = frame.shape[2]
    print("weight : %s, height : %s, channel : %s" %(weight, height, channels))
    
    for row in range(height):            #遍历高
        for col in range(weight):         #遍历宽
            for c in range(channels):     #便利通道
                pv = frame[row, col, c]     
                frame[row, col, c] = 255 - pv     #全部像素取反，实现一个反向效果
    cv.imshow("fanxiang", frame)
    
filepath = '/Users/leaf/project/scanWords/testPic/'
for filename in os.listdir(filepath):
    src = cv2.imread('/Users/leaf/project/scanWords/testPic/%s'%filename)
    cv.imshow("Picture", src)
    access_pixels(src)
    cv.waitKey(0)



