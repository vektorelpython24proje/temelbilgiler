import cv2
import numpy as np

# frame per second

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    
    kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(frame,-1,kernel)
    blur = cv2.GaussianBlur(frame,(15,15),-1)
    median = cv2.medianBlur(frame,25)
    bilateral = cv2.bilateralFilter(frame,15,75,75)

    cv2.imshow("kamera",bilateral)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
