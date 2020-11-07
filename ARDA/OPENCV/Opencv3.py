import cv2
img = cv2.imread(r"ARDA\OPENCV\resim.png")
cv2.line(img,(50,50),(150,150),(255,255,0),3)
cv2.rectangle(img,(50,50),(150,150),(255,255,0),2)
cv2.circle(img,(100,100),50,(200,200,120),-1)

cv2.imshow("ilkresim",img)

cv2.waitKey(0)
cv2.destroyAllWindows()