import cv2
import numpy as np

# Load image
img = cv2.imread('lena2.jpg')

# Define kernel size for average filter
kernel_size = (5, 5)

# Create kernel for average filter
kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

# Apply average filter to image using filter2D
blur = cv2.filter2D(img, -1, kernel)

# Display original and filtered image
cv2.imshow('Original', img)
cv2.imshow('Average Filter', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()