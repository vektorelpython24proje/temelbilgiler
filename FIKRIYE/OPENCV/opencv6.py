import cv2


import cv2 
# frame per second
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
img2 = cv2.imread(r"EDIZ\OPENCV\thuglife.png")
konum = 150
scale_percent = 20 # percent of original size
width = int(img2.shape[1] * scale_percent / 100)
height = int(img2.shape[0] * scale_percent / 100)
dim = (width, height)

img2 = cv2.resize(img2,dim,interpolation=cv2.INTER_AREA)
while True:
    ret,frame = cap.read()
    # print("1",type(frame))
    # print("2",type(img2))


    rows,cols,channels = img2.shape
    roi = frame[konum:konum+rows,konum:konum+cols]   

    img2gri = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    ret,mask = cv2.threshold(img2gri,7,255,cv2.THRESH_BINARY_INV)

    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

    img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
    dst = cv2.add(img1_bg,img2_fg)
    frame[konum:konum+rows,konum:konum+cols] = dst

    cv2.imshow("ilkresim",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()

