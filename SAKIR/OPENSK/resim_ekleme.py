# resim_ekleme.py
import cv2
import PIL
from opensk3.py import *
#from PIL import Image, ImageDraw, ImageFont
fon0=cv2.imread('SAKIR\Resimler\cadde01.jpg')
top=cv2.imread('sari_top.png',-1)
topmaske=top[:,:,3]
ters_topmaske=cv2.bitwise_not(topmaske)
top=top[:,:,0:3]
d=top.shape[1]
alfa=0.3
yontem=1
hiz=15;x=0;y=0
while True:
    fon=fon0.copy()
    y+=hiz
    if y+d>fon0.shape[0]:
        y=0
        x=x+d//2
        if x+d>fon0.shape[1]:x=0
    if yontem==1:
        try:
            fon[y:y+d,x:x+d]=top
        except:pass
    elif yontem==2:
        try:
            beta=1.0-alfa
            fon[y:y+d,x:x+d]=cv2.addWeighted(fon[y:y+d,x:x+d],1.0,top,beta,0,0)
        except: pass
    elif yontem==3:
        try:
            parca=fon[y:y+d,x:x+d]
            alt_parca=cv2.bitwise_and(parca,parca,mask=ters_topmaske)
            ust_parca=cv2.bitwise_and(top,top,mask=topmaske)
            fon[y:y+d,x:x+d+d]=cv2.add(alt_parca,ust_parca)
        except:pass
    mesaj="Yöntem:  "+str(yontem)+" (seçenekler: 1-2-3 ESC:ÇIKIŞ)"
    fon = print_utf8_text(fon,mesaj,color=(255,255,255),boy=36,yer=(10,650)

    cv2.imshow('fon',fon)
    k=cv2.waitKey(10) & 0xFF
    if k==27:break
    elif k==ord('1'):
        yontem=1
    elif k=ord('2'):
        yontem=2
    elif k=ord("3"):
        yontem=3
cv2.destroyAllWindows()
