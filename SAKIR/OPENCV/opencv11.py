import cv2
import numpy as np
img = cv2.imread(r"SAKIR\Resimler\basin.jpg")
gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

temp1 = cv2.imread(r"SAKIR\Resimler\temp1.jpg",0)
temp2 = cv2.imread(r"SAKIR\Resimler\temp2.jpg",0)
w,h = temp2.shape[::-1]
res = cv2.matchTemplate(gri,temp2,cv2.TM_CCOEFF_NORMED)
thresh = 0.6
loc = np.where(res>=thresh)
# print(zip(*loc[::-1]))
for pt in zip(*loc[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)



cv2.imshow("ilkresim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()