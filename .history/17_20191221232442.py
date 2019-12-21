from PIL import Image  
from numpy import *  
  
file_path = '/Users/leaf/project/scanWords/testPic/2019-12-20-0101.jpg'
pil_im = Image.open(file_path)  
source_route = 0.006277944427853939
pil_im = pil_im.rotate(20)  
new_file_path = '/Users/leaf/project/scanWords/testPic/new_2019-12-20-0101.jpg'
pil_im.save(new_file_path)

