import cv2
import numpy as np
img = cv2.imread(r"SAKIR\Resimler\resim.png")
# px = img[50,50]
# print(pc)
# img[50,50] = [255,255,255]
# print(px)
# px = img[100:150,100:150]
img[200:250,200:250] = img[100:150,100:150]
img[100:150,100:150] = [255,255,255]

# px = [255,255,255]

cv2.imshow("ilkresim",img)

cv2.waitKey(0)
cv2.destroyAllWindows()