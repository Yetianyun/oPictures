from PIL import Image  
from numpy import *  
  
filepath = '/Users/leaf/project/scanWords/testPic/2019-12-20-0101.jpg'

pil_im = Image.open(filepath)  
pil_im = pil_im.rotate(2)  
print pil_im.size  
pil_im.save('e:/aa/30.bmp')

