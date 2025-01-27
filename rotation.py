import cv2
img=cv2.imread('Images/r_flower.jpg',1)
cv2.imshow('original',img)
#get image height and width
(h,w)=img.shape[:2]
center=(w/2,h/2)
scale=1.0

#90 degrees rotation
M=cv2.getRotationMatrix2D(center,90,scale)
rotated90=cv2.warpAffine(img,M,(h,w))
cv2.imshow('img90',rotated90)

#180 degrees rotation
M=cv2.getRotationMatrix2D(center,180,scale)
rotated180=cv2.warpAffine(img,M,(h,w))
cv2.imshow('img180',rotated180)

#270 degrees rotation
M=cv2.getRotationMatrix2D(center,270,scale)
rotated270=cv2.warpAffine(img,M,(h,w))
cv2.imshow('img270',rotated270)
cv2.waitKey(0)