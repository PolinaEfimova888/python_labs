import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import morphology
from skimage.filters import threshold_otsu, threshold_triangle
from skimage.measure import label, regionprops


def lakes(image):
    B=~image
    BB=np.ones((B.shape[0]+2, B.shape[1]+2))
    BB[1:-1,1:-1]=B
    return (np.max(label(BB))-1)

def has_vline(image):
    lines= np.sum(image,0) // image.shape[0]
    return 1 in lines

def has_bay(image):
    b=~image
    bb=np.zeros((b.shape[0]+1, b.shape[1])).astype("uint8")
    bb[:-1, :]=b
    return lakes(bb)-1


def recognize(image):
    lc=lakes(image)
    if lc == 2:
        print("B or 8")
        if has_vline(image):
            return "B"
        return "8"
    if lc ==1:
        print("A or 0")
        if has_bay(image) > 0:
            return "A"
        return "0"
    return None


image = plt.imread("alphabet.png")
image=np.sum(image,2)
image[image>0]=1

labeled= label(image)
print(np.max(labeled))

regions = regionprops(labeled)
d={}
for region in regions:
    symbol=recognize(region.image)
    if symbol not in d:
        d[symbol]=1
    else:
        d[symbol] +=1
print(d)

# print(lakes(regions[1].image))
# print(lakes(regions[2].image))
# print(lakes(regions[3].image))

#plt.figure()
#plt.subplot(121)
#plt.imshow(BB)
#plt.subplot(122)
#plt.imshow(~regions[3].image)

plt.figure()
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(labeled)
plt.show()
