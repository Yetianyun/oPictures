# -*- coding: utf-8 -*-
#检测图片中的直线
import cv2

import numpy as np

import matplotlib.pyplot as plt
import os

source_path = "testPic"
for scan_file in os.listdir(source_path):
    print(scan_file)
    source_file_path = 'testPic/' + scan_file
    img = cv2.imread(source_file_path)  # 需要图片的绝对路径
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 200)
    ls = cv2.HoughLines(edges, 1, np.pi / 180, 100)
    l1 = ls[:, 0, :]
    for r, t in l1[:]:
        a = np.cos(t)
        b = np.sin(t)
        x0 = a * r
        y0 = b * r
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
