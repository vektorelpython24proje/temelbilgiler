import cv2

img = cv2.imread(r"BERKE\OPENCV\resim.png")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)



temp1 = img = cv2.imread(r"BERKE\OPENCV\resim.png",0)

cv2.imshow("ilkresim",temp1)

cv2.waitKey(0)
cv2.destroyAllWindows()