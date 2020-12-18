# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 19:32:36 2020

@author: polin
"""

import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage import color
import numpy as np

def count_f(colors, name):
    colors.sort()
    color_set = {}
    count_r =0
    count_c =0
    for color in colors:
        
        if len(color_set) > 0:
            last = list(color_set.keys())[-1]
            if color != last:
                if color > last + 0.02:
                    cur_key = color
                    color_set[cur_key] = 1
                else:
                    color_set[cur_key] += 1
            else:
                color_set[cur_key] += 1
        else:
            cur_key = color
            color_set[cur_key] = 1
    
    for color in color_set:
        count_r += color_set.get(color)    
        count_c += color_set.get(color)
        
    print(f'{name}: {color_set}')
    print(f'{name}: {count_r}')

    
image = plt.imread('balls_and_rects.png')
binary = image.copy()[:, :, 0]
binary[binary > 0] = 1
image = color.rgb2hsv(image)[:, :, 0]
labeled = label(binary)

print('all figures:', np.max(labeled))


def circle(region):
    return (region.perimeter**2)/region.area

def sten(bbox):
    return bb[2] - bb[0], bb[3] - bb[1]


colors_r= []
colors_c= []

for region in regionprops(labeled):
    bb = region.bbox
    val = np.max(image[bb[0]:bb[2], bb[1]:bb[3]])
    
    a, b = sten(bb)
    if a * b == region.area:
        colors_r.append(val)
    else:
        colors_c.append(val)


#print(colors)
#colors.sort()

count_f(colors_c, 'circle')
count_f(colors_r, 'rectangle')
