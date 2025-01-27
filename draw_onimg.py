import cv2

#circle
img1=cv2.imread('Images/r_flower.jpg')
cv2.circle(img1, (80,80), 55, (0,255,0),-1)
cv2.imshow('image_circle', img1)

#rectangle
img2=cv2.imread('Images/color.jpg')
cv2.rectangle(img2, (15,25), (200,150), (0,255,255),5)
cv2.imshow('image_rectangle', img2)


#ellipse
img3=cv2.imread('Images/tree.jpg')
cv2.ellipse(img3, (150, 50), (80, 20), 5, 0, 360, (0,0,255), -1)
cv2.imshow('image_ellipse', img3)

#line
img4=cv2.imread('Images/grayimg_flower.jpg')
cv2.line(img4, (10,0),(150,150),(0,0,0),15)
cv2.imshow('image_line', img4)

cv2.waitKey(0)