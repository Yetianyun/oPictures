import numpy as np
from cv2 import cv2 #或者用import cv2（由于库的安装方式不同）
 
def access_pixels(img):
    """遍历图像每个像素的每个通道"""
    print(img.shape)              #打印图像的高，宽，通道数（返回一个3元素的tuple）

    height = img.shape[0]        #将tuple中的元素取出，赋值给height，width，channels
    width = img.shape[1]
    channels = img.shape[2]


    # width = round(width / 10)
    # height = 10 # round(height / 10 )
    #(3496, 2472, 3)
    width = 1470 #int(width)
    print("height:%s,width:%s,channels:%s" % (height,width,channels))
    print(img.size)              #打印图像数组内总的元素数目（总数=高X宽X通道数）
    for row in range(0,height,100):    #遍历每一行
        # for col in range(0,width,200): #遍历每一列
        for col in range(width,0,-1): #遍历每一列
            pixelColor = 0 ; # 计算RGB的值
            oldPixelColor = pixelColor
            for channel in range(channels):    #遍历每个通道（三个通道分别是BGR）
                pixelColor = pixelColor * 1000 + img[row][col][channel]
            minColor = abs ( pixelColor - oldPixelColor ) 
            # if ( minColor < 0 )
            #     minColor = minColor * ( -1)
            # if ( minColor > 100000000) 
            #     widthLine= col
            #     os.exit(1)
            print(row,col,pixelColor,minColor)
        print("\n")
                # img[row][col][channel] = 255 - img[row][col][channel] 
                #通过数组索引访问该元素，并作出处理
    # cv2.imshow("processed img",img) #将处理后的图像显示出来
 
#上述自定义函数的功能是像素取反，当然，opencv自带像素取反方法bitwise_not()，不需要这么麻烦
def inverse(img):
    """此函数与access_pixels函数功能一样"""
    dst = cv2.bitwise_not(img)
    cv2.imshow("inversed_img",dst)
 
 
def create_img():
    """#创建一张三通道图像"""
    img = np.zeros([600,800,3],dtype=np.uint8)
    #创建高600像素，宽800像素，每个像素有BGR三通道的数组（图像）
    #由于元素都在0~255之内，规定数组元素类型为uint8已足够
    img[:,:,2] = np.ones([600,800])*255
    #img[:,:,2]是一种切片方式，冒号表示该维度从头到尾全部切片取出
    #所以img[:,:,2]表示切片取出所有行，所有列的第三个通道（索引为2）
    #右侧首先创建了一个600X800的二维数组，所有元素初始化为1，再乘上255，即所有元素变为255
    #注意右侧600X800的二维数组与左侧切片部分形状相同，所以可以赋值
    #即所有行，所有列的第三个通道(R)的值都变为255，一二通道(BG)仍为0，即所有像素变为红色BGR(0，0，255)
    cv2.imshow("created_img",img)
 
 
def create_img_1():
    """创建一张单通道图像"""       
    img = np.zeros([400,400,1],dtype=np.uint8)
    #高400像素，宽400像素，单通道
    #仍是三维数组，不过第三个维度长度为1，用来表示像素的灰度（0~255）
    img[:,:,0] = np.ones([400,400])*127
    #切片取出所有行所有列的第一个元素（索引为0），灰度元素，并赋值为127
    cv2.imshow("created_img1",img)
 
 
 
src = cv2.imread("testPic/2019-12-20-0101.jpg")  #读取图像
t1 = cv2.getTickCount()    #记录下起始时刻
access_pixels(src)         #访问图像的每个元素并处理
create_img()               #通过numpy创建三通道彩色图
create_img_1()            #通过numpy创建单通道灰度图
t2 = cv2.getTickCount()   #记录下结束时刻
time = ((t2-t1)*1000)/cv2.getTickFrequency() #计算中间语句执行所耗时间，单位为ms
print("所耗时间：%s" % time)
 
 
# cv2.waitKey(0)
# cv2.destroyAllWindows()