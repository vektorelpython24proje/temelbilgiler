import cv2
img1 = cv2.imread(r"EDIZ\OPENCV\3D-Matplotlib.png")
img2 = cv2.imread(r"EDIZ\OPENCV\thuglife.png")

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gri = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(img2gri,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow("ilkresim",img1)
# add = img1+img2

# add = cv2.add(img1,img2)

# add =  cv2.addWeighted(img1,0.6,img2,0.4,0)




cv2.waitKey(0)
cv2.destroyAllWindows()