import cv2
img=cv2.imread('Images/flower.jpg',0)
status=cv2.imwrite('Images/grayimg_flower.jpg',img) 
#Returns boolean value indicating whether the file is successfully written
print('Staus:',status)