import cv2 
import numpy as np
# frame per second
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    ret,frame = cap.read()

    # boundaries = [
	# ([17, 15, 100], [50, 56, 200]),
	# ([86, 31, 4], [220, 88, 50]),
	# ([25, 146, 190], [62, 174, 250]),
	# ([103, 86, 65], [145, 133, 128])
    # ]
                 #  G    B    R                   
    dusuk = np.array([30,150,50])
    yuksek = np.array([255,255,180])

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv,dusuk,yuksek)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    

    cv2.imshow("kamera", np.hstack([frame, res]))
    cv2.imshow("kamera2",mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
