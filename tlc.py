# Phiên bản 2.0

from PIL import Image
import matplotlib.pyplot as plt 
import numpy as np 
import cv2
import os 
import math

def tlc2spec(input_img, background):
    """_summary_

    Args:
        input_img: Path to TLC image
        background: Choose color background of TLC image. W (White), B (Black), G (Green), BL (Blue)
    """
    org_img = cv2.imread(input_img)
    rgb_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)
    axis_x = []
    axis_y = []
    if background == "W":
        for i in range(rgb_img.shape[1]):
            axis_x.append(i)
        for j in range(int(rgb_img.shape[1])):
            R = int(rgb_img[int((rgb_img.shape[0])/2), j][0])
            G = int(rgb_img[int((rgb_img.shape[0])/2), j][1])
            B = int(rgb_img[int((rgb_img.shape[0])/2), j][2])
            I = 1/((R+G+B)/3)
            axis_y = np.append(axis_y, I)
    elif background == "G":
        for i in range(rgb_img.shape[1]):
            axis_x.append(i)
        for j in range(int(rgb_img.shape[1])):
            R = int(rgb_img[int((rgb_img.shape[0])/2), j][0])
            G = int(rgb_img[int((rgb_img.shape[0])/2), j][1])
            B = int(rgb_img[int((rgb_img.shape[0])/2), j][2])
            I = 1/((R+G+B)/3)
            axis_y = np.append(axis_y, I)
    elif background == "B":
        for i in range(rgb_img.shape[1]):
            axis_x.append(i)
        for j in range(int(rgb_img.shape[1])):
            R = int(rgb_img[int((rgb_img.shape[0])/2), j][0])
            G = int(rgb_img[int((rgb_img.shape[0])/2), j][1])
            B = int(rgb_img[int((rgb_img.shape[0])/2), j][2])
            I = ((R+G+B)/3)
            axis_y = np.append(axis_y, I)
    elif background == "BL":
        for i in range(rgb_img.shape[1]):
            axis_x.append(i)
        for j in range(int(rgb_img.shape[1])):
            R = int(rgb_img[int((rgb_img.shape[0])/2), j][0])
            G = int(rgb_img[int((rgb_img.shape[0])/2), j][1])
            B = int(rgb_img[int((rgb_img.shape[0])/2), j][2])
            I = ((R+G+B)/3)
            axis_y = np.append(axis_y, I)
    else:
        print("Color background is not valiable.")
    return plt.plot(axis_x, axis_y)
    
        
    
