import cv2
img = cv2.imread(r"SAKIR\Resimler\resim.png")
cv2.imshow("Orijinal",img)
print(img.shape)
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("ilkresimgri",gri)
cv2.waitKey(0)
cv2.destroyAllWindows()