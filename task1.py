import numpy as np
import matplotlib.pyplot as plt

def getNominalResolution(image,realSize):
    lst=[]
    lst.append(np.where(image==1))
    max=0
    for i in range(len(lst[0][0])):
        for j in range(len(lst[0][0])):
            if i!=j:
                temp=int((lst[0][0][i]-lst[0][0][j])**2 + (lst[0][1][i]-lst[0][1][j])**2)**0.5
                if temp>max: max=temp

    if max==0:
        return "The figure does not exist"
    else:            
        return (realSize/max)


for i in range(1,7):
    name = 'figure'
    txt = '.txt'

    file = open(name + str(i) + txt)
    realSize=float(file.readline())
    file.close()
    img = np.genfromtxt(fname=name + str(i) + txt,skip_header=1)


    getNominalResolution(img, realSize)
    print(f'Answer for figure{i}.txt:')
    print(getNominalResolution(img, realSize))
