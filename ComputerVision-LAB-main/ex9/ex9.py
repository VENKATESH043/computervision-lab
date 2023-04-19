# Importing the libraries

import cv2
import numpy as np
#Haris Corner Detection
# Reading the image and converting the image to B/W
img = cv2.imread('bby1.jpg')
image = cv2.imread('bby1.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = np.float32(gray_image)
# Applying the function
dst = cv2.cornerHarris(gray_image, blockSize=2, ksize=3, k=0.04)
# dilate to mark the corners
dst = cv2.dilate(dst, None)
image[dst > 0.01 * dst.max()] = [0,0,255]
Hori = np.concatenate((img, image), axis=1)
cv2.imshow('haris_corner', Hori)
cv2.waitKey()
#SIFT Detection
# Reading the image and converting into B/W
image = cv2.imread('bby1.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Applying the function
sift = cv2.SIFT_create()
kp, des = sift.detectAndCompute(gray_image, None)
# Applying the function
kp_image = cv2.drawKeypoints(image, kp, None, color=(0,0,255), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
Hori = np.concatenate((img, kp_image), axis=1)
cv2.imshow('SIFT', Hori)
cv2.waitKey()
#FAST Corner Detection
# Reading the image and converting into B/W
image = cv2.imread('bby1.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Applying the function
fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)
# Drawing the keypoints
kp = fast.detect(gray_image, None)
kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 0,255))
Hori = np.concatenate((img, kp_image), axis=1)
cv2.imshow('FAST', Hori)
cv2.waitKey()
cv2.destroyAllWindows()
