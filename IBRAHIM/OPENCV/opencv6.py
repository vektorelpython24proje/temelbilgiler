import cv2 
# frame per second
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
img2 = cv2.imread(r"EDIZ\OPENCV\thuglife.png")
while True:
    ret,frame = cap.read()
    # print("1",type(frame))
    # print("2",type(img2))


    rows,cols,channels = img2.shape
    roi = frame[0:rows,0:cols]   

    img2gri = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    ret,mask = cv2.threshold(img2gri,220,255,cv2.THRESH_BINARY_INV)

    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

    img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
    dst = cv2.add(img1_bg,img2_fg)
    frame[0:rows,0:cols] = dst

    cv2.imshow("ilkresim",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
