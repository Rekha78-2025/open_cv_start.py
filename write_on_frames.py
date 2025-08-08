import cv2 

img = cv2.imread("nice_birds.jpg") 

cv2.putText(img, "This is bird pick", (100, 100),3, 1.0, (10, 240, 30), 2)
cv2.imshow("nice_birds.jpg", img) 

cv2.waitKey(0)