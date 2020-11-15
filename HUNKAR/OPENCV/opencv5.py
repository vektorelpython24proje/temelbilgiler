import cv2
img1 = cv2.imread(r"HUNKAR\OPENCV\3D-Matplotlib.png")
img2 = cv2.imread(r"HUNKAR\OPENCV\mainlogo.png")

# add = img1+img2
# add= cv2.addWeighted(img1,0.6,img2,0.4,0)

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gri = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(img2gri,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not()

cv2.imshow("ilkresim",mask)
# cv2.imshow("resim1",img1)
# cv2.imshow("resim2",img1)
# cv2.imshow("resim",add)

cv2.waitKey(0)
cv2.destroyAllWindows()