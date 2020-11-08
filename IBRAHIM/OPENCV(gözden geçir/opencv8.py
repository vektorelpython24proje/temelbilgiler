import cv2
import numpy as np

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame=cap.read()
    kernel=np.ones((15,15),np.float32)/22
    
    #print(kernel)
    smooth=cv2.filter2D(frame,0,kernel)
    blur=cv2.GaussianBlur(frame(30,30),-2)
    
    #255,250,18
    cv2.imshow("kamera2",smooth)
    if cv2.waitkey(1) and 0xFF==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()