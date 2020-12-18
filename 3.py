# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:12:37 2020

@author: polin
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology 

all_symbols =[]
image = np.load('ps.npy.txt')

first_symbole = np.ones((4,6)) 
all_symbols.append(first_symbole)

second_symbole = first_symbole 
second_symbole[:2,2:4] = 0
all_symbols.append(second_symbole)

third_symbole = np.flip(second_symbole)
all_symbols.append(third_symbole) 

fourth_symbole = np.transpose(second_symbole)
all_symbols.append(fourth_symbole) 

fith_symbole = np.transpose(third_symbole)
all_symbols.append(fith_symbole) 

count_symboles_in_picture = []

for item in range(5):
    new_symbole = morphology.binary_hit_or_miss(image
                                                , all_symbols[item])
    count_symboles_in_picture.append(np.sum(new_symbole))

symbols = ['первый','второй','третий','четвертый','пятый']
[print(count_symboles_in_picture[item] ,symbols[item])\
 for item in range(len(count_symboles_in_picture))]

    


print(np.sum(count_symboles_in_picture),' all')
