#水平校正图片

import os
import cv2
import math
import random
import numpy as np
from scipy import misc, ndimage

filepath = '/Users/leaf/project/scanWords/testPic/'
for filename in os.listdir(filepath):
    # print(filename)
	img = cv2.imread('/Users/leaf/project/scanWords/testPic/%s'%filename)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	#霍夫变换
	lines = cv2.HoughLines(edges,1,np.pi/180,0)
	
	for rho,theta in lines[0]:
	    a = np.cos(theta)
	    b = np.sin(theta)
	    x0 = a*rho
	    y0 = b*rho
	    x1 = int(x0 + 1000*(-b))
	    y1 = int(y0 + 1000*(a))
	    x2 = int(x0 - 1000*(-b))
	    y2 = int(y0 - 1000*(a))
	if x1 == x2 or y1 == y2:
		continue
	t = float(y2-y1)/(x2-x1)

	# rotate_angle = math.degrees(math.atan(t))
	rotate_angle = 0.006277944427853939
	# if rotate_angle > 45:
	# 	rotate_angle = -90 + rotate_angle
	# elif rotate_angle < -45:
	# 	rotate_angle = 90 + rotate_angle
	rotate_img = ndimage.rotate(img, rotate_angle)
	misc.imsave('/Users/leaf/project/scanWords/testPic/123%s'%filename, rotate_img)
 