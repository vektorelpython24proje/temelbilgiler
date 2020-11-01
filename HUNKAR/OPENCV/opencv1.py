import cv2
img = cv2.imread(r"HUNKAR\OPENCV\resim.png")
cv2.imshow("İlk Resim",img,enc)
cv2.waitKey(0)
cv2.destroyAllWindows()