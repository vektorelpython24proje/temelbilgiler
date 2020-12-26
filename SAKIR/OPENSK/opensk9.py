"""
maskeleme.py
bir resmi istenen renklere göre maskelemek
"""
import cv2
import numpy as np
import sys
if sys.platform == 'win32':
    deltax = 0
    deltay = 0
else:
    deltax = 50
    deltay = 105
img = cv2.imread("SAKIR\Resimler\monalisa.jpg")
maske = np.ones(img.shape,dtype="uint8")*255
maske[:,260:] = [0,0,0]
maskeli = cv2.bitwise_and(img,maske)
cv2.imshow("img",img)
cv2.moveWindow("img",10,10)
cv2.imshow("maske",maske)
cv2.moveWindow("maske",img.shape[1]+deltax,10)
cv2.imshow("maskeli",maskeli)
cv2.moveWindow("maskeli",380,img.shape[0]+deltay)
while True:
    k = cv2.waitKey(10)
    if k == 27: break
cv2.destroyAllWindows() 