import cv2 

img = cv2.imread("nice_birds.jpg") 


cv2.imshow("nice_birds.jpg", img) 


# to change color 
# cvtcolor 

grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow("grey_imgage", grey_img)


hlv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
cv2.imshow("hsv image", hlv)

cv2.waitKey(0) 