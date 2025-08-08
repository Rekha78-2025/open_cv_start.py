import cv2 

cap = cv2.VideoCapture(r"C:\Users\bca19\OneDrive\Desktop\videos\WhatsApp Video\Sent\VID-20221020-WA0005.mp4") 

# open-------> frames 

while True:
    is_True, frame = cap.read() 
    
    cv2.imshow("my video", frame) 
    
    cv2.waitKey(20)