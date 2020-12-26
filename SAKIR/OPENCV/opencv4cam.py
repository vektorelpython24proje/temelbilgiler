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

"""
RENKLER
[255,255,255]   Beyaz
[255,255,0]     Turkuaz
[255,0,255]     Pembe
[0,255,255]     Sarı
[255,0,0]       Mavi
[0,0,255]       Kırmızı
[0,255,0]       Yeşil
[0,0,0]         Siyah

"""
