import cv2

img = cv2.imread(r"BERKE\OPENCV\resim.png")
print(img.shape)
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

print(gri)
cv2.imshow("ilkresim",img)

# cv2.imshow("ilkresimgri",gri)

cv2.waitKey(0)

cv2.destroyAllWindows()