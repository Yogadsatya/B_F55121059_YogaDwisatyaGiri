import cv2
import numpy as np
from matplotlib import pyplot as plt

# membaca citra
img = cv2.imread('cewe.png',0)

# menampilkan citra
cv2.imshow('Result',img)

# membuat histogram
hist,bins = np.histogram(img.flatten(),256,[0,256])

# menampilkan histogram
plt.hist(img.flatten(),256,[0,256])
plt.xlim([0,256])
plt.show()

# menunggu input keyboard
cv2.waitKey(0)
cv2.destroyAllWindows()