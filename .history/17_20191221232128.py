from PIL import Image  
from numpy import *  
  
  
  
pil_im = Image.open('e:/aa/3.bmp')  
pil_im = pil_im.rotate(2)  
print pil_im.size  
pil_im.save('e:/aa/30.bmp')
————————————————
版权声明：本文为CSDN博主「Txiaomiao」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Txiaomiao/article/details/51374377