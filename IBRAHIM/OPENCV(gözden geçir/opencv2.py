import cv2 
# frame per second
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("kamera1",gri)
    blur = cv2.GaussianBlur(gri,(21,21),0)
    cv2.imshow("kamera2",blur)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
