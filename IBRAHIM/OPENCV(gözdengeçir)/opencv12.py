import cv2
import numpy as np

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
fgbg=cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)
    cv2.imshow("kamera",frame)
    cv2.imshow("kamera2",fgmask)

    if cv2.waitKey(1) and 0xFF==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()