# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:19:05 2020

@author: polin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import morphology
from skimage.measure import label, regionprops
from skimage.filters import threshold_triangle


def togray(image):
    return (0.2989*image[:, :, 0]+0.587*image[:, :, 1]+0.114 * image[:, :, 2]).astype('uint8')


def binarisation(image, limit_min, limit_max):
    B = image.copy()
    B[B <= limit_min] = 0
    B[B >= limit_max] = 0
    B[B > 0] = 1
    return B




def magic_with_binary(gray,thresh):
  binary = binarisation(gray, 0, thresh)
  binary = morphology.binary_erosion(binary)
  binary = morphology.binary_dilation(binary)
  return binary


key_value =[100,450000,300000]
total_pen =0
files = ['img (1).jpg','img (2).jpg','img (3).jpg','img (4).jpg'
            ,'img (5).jpg','img (6).jpg','img (7).jpg','img (8).jpg'
            ,'img (9).jpg','img (10).jpg','img (11).jpg','img (12).jpg']
for file in files:
    image = plt.imread(file)
    gray = togray(image)

    thresh = threshold_triangle(gray)
    binary = magic_with_binary(gray,thresh)
    label_pen = label(binary)

    state = []
    
        
    [state.append(item.area)\
      for item in regionprops(label_pen)]   

    for item in regionprops(label_pen):
        if item.area < np.mean(state):
          label_pen[label_pen == item.label] = 0 
        tmp = item.bbox
        label_pen[label_pen == item.label] = 0 if tmp[0] == 0 or tmp[1] == 0 else label_pen[label_pen == item.label]
            

    label_pen[label_pen > 0] = 1
    label_pen = label(label_pen)

    count =  0
    for region in regionprops(label_pen):
      isCirc = (region.perimeter*region.perimeter)/region.area
      if isCirc > key_value[0] and region.area < key_value[1] and region.area > key_value[2]:
        total_pen += 1 
            
    
    
print('total:', total_pen)
