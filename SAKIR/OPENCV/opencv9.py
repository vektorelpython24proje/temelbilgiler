import cv2
img = cv2.imread(r"SAKIR\OPENCV\bookpage.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval,threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,99,1)
retval2,threshold2 = cv2.threshold(gri,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("ilkresim",img)
cv2.imshow("esik1",threshold2)
cv2.imshow("esik2",th)
cv2.waitKey(0)
cv2.destroyAllWindows()