import cv2

img1=cv2.imread('Images/r_flower.jpg')
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'Flower', (20,45), font, 2, (0,200,140),5)

#Display the image
cv2.imshow("image", img1)
cv2.waitKey(0)