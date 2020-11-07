import cv2 
# frame per second
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    ret,frame = cap.read()

    frame[200:250,200:250] = frame[100:150,100:150]
    frame[100:150,100:150] = [255,255,255]
    
    cv2.imshow("ilkresim",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
