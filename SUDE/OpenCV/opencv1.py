import cv2
img = cv2.imread(r"EDIZ\OPENCV\resim.png")
print(img[100:150,100:150])
cv2.imshow("ilkresim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
