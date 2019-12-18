from skimage import data, exposure, img_as_float,io
import matplotlib.pyplot as plt

#调整图片的对比度
image = io.imread('./sourceImages/WX20191218-224733.png')
# image = img_as_float(data.moon())
gam1= exposure.adjust_gamma(image, 2)   #调暗
gam2= exposure.adjust_gamma(image, 0.5)  #调亮
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(131)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(132)
plt.title('gamma=2')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.subplot(133)
plt.title('gamma=0.5')
plt.imshow(gam2,plt.cm.gray)
plt.axis('off')

plt.show()