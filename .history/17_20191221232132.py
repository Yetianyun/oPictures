from PIL import Image  
from numpy import *  
  
pil_im = Image.open('e:/aa/3.bmp')  
pil_im = pil_im.rotate(2)  
print pil_im.size  
pil_im.save('e:/aa/30.bmp')