import numpy as np
import matplotlib.pyplot as plt

for i in range(1,7):

    name = 'figure'
    txt = '.txt'

    file = open(name + str(i) + txt)
    hor_size = float(file.readline())
   
    lines = file.readlines()[1:]
    length = len(lines[0].split())

    a = hor_size/length

    print(f'Answer for figure{i}.txt = {a}\n')
