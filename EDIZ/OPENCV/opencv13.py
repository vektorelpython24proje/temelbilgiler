
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
yuz_cas = cv2.CascadeClassifier(r"EDIZ\OPENCV\cascades\haarcascade_frontalface_default.xml")
eye_cas = cv2.CascadeClassifier(r"EDIZ\OPENCV\cascades\haarcascade_eye.xml")
while True:
    ret,frame = cap.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_cas.detectMultiScale(gri,1.3,5)
    for x,y,w,h in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)

    cv2.imshow("resim",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
