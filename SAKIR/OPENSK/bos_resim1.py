import numpy as np
import cv2
deneme = np.zeros((200,200,3),dtype=np.uint8)
cv2.imshow('deneme siyah',deneme)
deneme[:]=(255,255,255)
cv2.imshow('deneme beyaz',deneme)
deneme[:]=(0,0,255)
cv2.imshow('deneme kırmızı',deneme)
cv2.waitKey(0)
cv2.destroyAllWindows()