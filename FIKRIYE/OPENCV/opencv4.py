import cv2
img = cv2.imread(r"HUNKAR\OPENCV\resim.png")

px = img[50,50]
print(px)
img[50,50] = [255,255,255]
print(px)

cv2.imshow("ilkresim",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
