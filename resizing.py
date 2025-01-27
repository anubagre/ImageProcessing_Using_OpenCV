import cv2
img=cv2.imread('Images/flower.jpg',1)
print('Original dimensions:',img.shape)

width=500
height=450
dim=(width,height)

resized_img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('Resized dimensions:',resized_img.shape)

cv2.imshow('Original',img)
cv2.imshow('Resized',resized_img)
cv2.imwrite('Images/r_flower.jpg',resized_img)
cv2.waitKey(0)