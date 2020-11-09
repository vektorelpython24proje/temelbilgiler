# renk_kanallari.py
import cv2
import sys
if sys.platform=='win32':
    deltax=0
    deltay=0
else:
    deltax=50
    deltay=105
img=cv2.imread("SAKIR\Resimler\kaplan.jpg")
m=img.copy()
m[:,:,1]=0
m[:,:,2]=0
y=img.copy()
y[:,:,0]=0
y[:,:,2]=0
k=img.copy()
k[:,:,0]=0
k[:,:,1]=0
print(img.shape)
cv2.imshow("ORIGINAL",img);cv2.moveWindow('ORIGINAL',10,10)
cv2.imshow("MAVİ",m);cv2.moveWindow('MAVİ',10,img.shape[0]+deltay)
cv2.imshow("KIRMIZI",k);cv2.moveWindow('KIRMIZI',img.shape[1]+deltax,10)
cv2.imshow("YEŞİL",y);cv2.moveWindow('YEŞİL',img.shape[1]+deltax,img.shape[0]+deltay)
while True:
    k=cv2.waitKey(50) & 0xFF
    if k==27:break
cv2.destroyAllWindows()