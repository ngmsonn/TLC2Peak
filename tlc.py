# Version 3.0
# Author: Son Nguyen Manh
# Github: https://github.com/ngmsonn
# Website: https://ngmsonn.github.io/

from PIL import Image
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt 
import numpy as np 
import cv2
import os 
import math

def tlc2peaks(input_img, background):
    """ Create peaks from TLC image.

    Args:
        input_img: Path to TLC image
        background: Choose color background of TLC image. W (White), B (Black), G (Green) and BL (Blue)
    """
    org_img = cv2.imread(input_img)
    rbg_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)
    axis_x = []
    axis_y = []
    
    # White and green color background of TLC image
    if background == "W" or "G":
        mean_RGB = []
        for i in range(rbg_img.shape[0]):
            for k in range(rbg_img.shape[1]):
                mean_RGB.append(rbg_img[i, k].mean())
        max_mean_rgb = max(mean_RGB)
        for h in range(int(rbg_img.shape[1])):
            axis_x.append(h)
        for j in range(int(rbg_img.shape[1])):
            R = int(rbg_img[int((rbg_img.shape[0]/2)), j][0])
            G = int(rbg_img[int((rbg_img.shape[0]/2)), j][1])
            B = int(rbg_img[int((rbg_img.shape[0]/2)), j][2])
            I = int(max_mean_rgb-(R+G+B)/3)
            axis_y = np.append(axis_y, I)
    elif background == "BL" or "B":
        for h in range(int(rbg_img.shape[1])):
            axis_x.append(h)
        for j in range(int(rbg_img.shape[1])):
            R = int(rbg_img[int((rbg_img.shape[0]/2)), j][0])
            G = int(rbg_img[int((rbg_img.shape[0]/2)), j][1])
            B = int(rbg_img[int((rbg_img.shape[0]/2)), j][2])
            I = int((R+G+B)/3)
            axis_y = np.append(axis_y, I)
    else:
        print("Error!!!")
    return plt.plot(axis_x, axis_y)

def get_meanRGB(input_img):
    """Get RGB value of each pixel
    
    Args:
        input_img: Path to image.
    """
    org_img = cv2.imread(input_img)
    rbg_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)
    mean_RGB = []
    for i in range(rbg_img.shape[0]):
            for k in range(rbg_img.shape[1]):
                mean_RGB.append(rbg_img[i, k].mean())
    return np.array(mean_RGB)

def get_RGB(input_img):
    """Get RGB value of each pixel
    
    Args:
        input_img: Path to image.
    """
    org_img = cv2.imread(input_img)
    rbg_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)
    RGB = []
    for i in range(rbg_img.shape[0]):
            for k in range(rbg_img.shape[1]):
                RGB.append(rbg_img[i, k])
    return np.array(RGB)

def get_RGB_row(input_img, pxrow):
    org_img = cv2.imread(input_img)
    rbg_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2RGB)
    mean_RGB_row = []
    for j in range(int(rbg_img.shape[1])):
            R = int(rbg_img[int((pxrow)), j][0])
            G = int(rbg_img[int((pxrow)), j][1])
            B = int(rbg_img[int((pxrow)), j][2])
            I = int((R+G+B)/3)
            mean_RGB_row = np.append(mean_RGB_row, I)
    return np.array(mean_RGB_row)

