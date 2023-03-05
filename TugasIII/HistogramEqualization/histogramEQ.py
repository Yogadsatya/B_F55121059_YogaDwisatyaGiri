import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra
img = cv2.imread('khabib.jpg',0)

# membuat histogram equalization
equ = cv2.equalizeHist(img)

# menampilkan citra asli dan setelah histogram equalization
cv2.imshow('Original',img)
cv2.imshow('After Equalization',equ)

# membuat histogram dari citra setelah histogram equalization
hist,bins = np.histogram(equ.flatten(),256,[0,256])

# menampilkan histogram
plt.hist(equ.flatten(),256,[0,256])
plt.xlim([0,256])
plt.show()

# menunggu input keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()