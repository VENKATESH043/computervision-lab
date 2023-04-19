import cv2
#from google.colab.patches import cv2_imshow
image_paths=['tt1.jpg','tt2.jpg']
imgs = []
for i in range(len(image_paths)):
    imgs.append(cv2.imread(image_paths[i]))
    imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)
cv2.imshow('1',imgs[0])
cv2.imshow('2',imgs[1])
stitchy=cv2.Stitcher.create()
(dummy,output)=stitchy.stitch(imgs)
if dummy != cv2.STITCHER_OK:
    print("stitching ain't successful")
else:
    print('Your Panorama is ready!!!')
cv2.imshow('3',output)
 
cv2.waitKey(0)
