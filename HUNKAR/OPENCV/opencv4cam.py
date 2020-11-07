import cv2
# frame per second
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    # gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Kamera",frame)
    # #cv2.imshow("Kamera",gri)
    # blur = cv2.GaussianBlur(gri,(15,15),0)
    # cv2.imshow("Kamera2",blur)
    cv2.imshow("ilkresim",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()