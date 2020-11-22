import cv2 
import numpy as np
# frame per second
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    kernel = np.ones((15,15),np.float32)/225
    # print(kernel)
    smooth = cv2.filter2D(frame,-1,kernel)
    blur = cv2.GaussianBlur(frame,(21,21),-2)
    median = cv2.medianBlur(frame,15)
    bilateral  = cv2.bilateralFilter(frame,15,75,75)

    # 255,250,18
    cv2.imshow("kamera2",bilateral)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# def topla(a,b):
#     return (a+b),a,b

# sonuc,a,b = topla(2,3)