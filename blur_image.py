import cv2 

img = cv2.imread("nice_birds.jpg") 
cv2.imshow("nice_birds.jpg", img) 

blur_img = cv2.GaussianBlur(img, (15,15), 10)
cv2.imshow("blur image", blur_img) 


# (img, (15,15), 0)------this is tuning object, value ko change kar kar dekhenge 
# ki hum image ko kitna blur kar skate hai
 


cv2.waitKey(0)