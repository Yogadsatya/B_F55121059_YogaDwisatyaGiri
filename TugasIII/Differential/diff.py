import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra pertama
img1 = cv2.imread('tupai1.png')

# membaca citra kedua
img2 = cv2.imread('tupai2.png')

# menghitung perbedaan antara kedua citra
diff = cv2.absdiff(img1, img2)

# menampilkan citra perbedaan
cv2.imshow('Citra Perbedaan',diff)

# membuat histogram dari citra perbedaan
hist,bins = np.histogram(diff.flatten(),256,[0,256])

# menampilkan histogram
plt.hist(diff.flatten(),256,[0,256])
plt.xlim([0,256])
plt.show()

# menunggu input keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()