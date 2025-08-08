import cv2 

img = cv2.imread("nice_birds.jpg") 
cv2.imshow("orignal image", img) 

detect_edges = cv2.Canny(img, 100,100) 
cv2.imshow("orignal image edegs",detect_edges )


grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) 
cv2.imshow("grey orignal image", grey_img) 

detect_edges_grey = cv2.Canny(grey_img, 300,300) 
cv2.imshow("orignal image edegs",detect_edges_grey)


cv2.waitKey(0)