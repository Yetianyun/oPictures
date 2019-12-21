#正确的进行旋转角度
from PIL import Image  
from numpy import *  
  
file_path = '/testPic/2019-12-20-0101.jpg'
pil_im = Image.open(file_path)  
source_route = 0.006277944427853939 * 360
pil_im = pil_im.rotate(source_route)  
new_file_path = '/Users/leaf/project/scanWords/testPic/tom_2019-12-20-0101.jpg'
pil_im.save(new_file_path)

