import cv2
img=cv2.imread('Images/color.jpg',1)

#Height, width and number of channels in image
print('Image Dimension:',img.shape)
print('Image Height:',img.shape[0])
print('Image Width:',img.shape[1])
print('Image Channels:',img.shape[2])
print('Image Size:',img.size)

b,g,r=cv2.split(img)
merged_img_bgr=cv2.merge((b,g,r))
merged_img_rgb=cv2.merge((r,g,b))

cv2.imshow('original_img',img)
cv2.imshow('b_img',b)
cv2.imshow('g_img',g)
cv2.imshow('r_img',r)
cv2.imshow('bgr_img',merged_img_bgr)
cv2.imshow('rgb_img',merged_img_rgb)

cv2.waitKey(0)