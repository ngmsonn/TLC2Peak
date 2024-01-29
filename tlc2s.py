# Phiên bản 1.0

from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np 
import cv2
import os 
import math

def cvrt(input_img):
    img = cv2.imread(input_img)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    axis_x = []
    axis_y = []
    for i in range(rgb_img.shape[1]):
        axis_x.append(i)
    for j in range(int((rgb_img.shape[1]))):
        R = int(rgb_img[int((rgb_img.shape[0])/2), j][0])
        G = int(rgb_img[int((rgb_img.shape[0])/2), j][1])
        B = int(rgb_img[int((rgb_img.shape[0])/2), j][2])
        I = 1/((R+B+G)/3)
        axis_y = np.append(axis_y, I)
    return plt.plot(axis_x, axis_y)

