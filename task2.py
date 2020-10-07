import numpy as np
import matplotlib.pyplot as plt


def upload_img(filename):
    s = []
    lines = open(filename)
    lines = lines.readlines()

    for lin in lines[2:]:
        s.append(lin.split())

    return np.array(s, dtype='int32')

img1 = upload_img('img1.txt')
img2 = upload_img('img2.txt')


def find(img):
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            if img[y, x] == 1:
                return y, x

y1, x1 = find(img1)
y2, x2 = find(img2)

y=y2-y1
x=x2-x1

print(f'Task 2\nсмещение\nх = {x}\nу = {y}')

plt.figure()
plt.subplot(121)
plt.imshow(img1)
plt.subplot(122)
plt.imshow(img2)
plt.show()
