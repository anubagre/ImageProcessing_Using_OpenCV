import cv2

img=cv2.imread('Images/flower.jpg',1)
#print(img)

img1=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img3=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img4=cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow('color image',img)
cv2.imshow('Gray image',img1)
cv2.imshow('RGB image',img2)
cv2.imshow('HSV image',img3)
cv2.imshow('LAB image',img4)
cv2.waitKey(0)
#cv2.destroyallWindows()