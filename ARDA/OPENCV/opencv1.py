import cv2
img = cv2.imread(r"ARDA\OPENCV\resim.png")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("ilkresim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()