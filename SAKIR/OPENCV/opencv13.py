
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
yuz_cas = cv2.CascadeClassifier(r"SAKIR\OPENCV\cascades\haarcascade_frontalface_default.xml")
eye_cas = cv2.CascadeClassifier(r"SAKIR\OPENCV\cascades\haarcascade_eye.xml")
while True:
    ret,frame = cap.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_cas.detectMultiScale(gri,1.3,5)
    for x,y,w,h in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        roi = frame[y:y+h,x:x+w]
        roigri = gri[y:y+h,x:x+w]
        gozler = eye_cas.detectMultiScale(roigri)
        for ex,ey,ew,eh in gozler:
            cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh),(255,0,0),1)


    cv2.imshow("resim",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


