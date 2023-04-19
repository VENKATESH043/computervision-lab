# import the necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv2.imread(r"j.jpg", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((5, 5), np.uint8)

# invert the image
invert = cv2.bitwise_not(binr)

# erode the image
erosion = cv2.erode(invert, kernel,iterations=1)
plt.imshow(erosion, cmap='gray')
plt.show()
dilation = cv2.dilate(invert, kernel, iterations=1)
plt.imshow(dilation, cmap='gray')
plt.show()
opening = cv2.morphologyEx(binr, cv2.MORPH_OPEN,kernel, iterations=1)
plt.imshow(opening, cmap='gray')
plt.show()
closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE, kernel, iterations=1)
plt.imshow(closing, cmap='gray')
plt.show()
