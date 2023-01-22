import numpy as np
import cv2

img = cv2.imread('static\ORIGIN\Texture2D\T_RuneIcons.png',cv2.IMREAD_UNCHANGED)
b, g, r, alpha = cv2.split(img)

for i in range(16): # 512/32 = 16
    for j in range(16):
        _b = b[i*32:(i+1)*32,j*32:(j+1)*32]
        _g = g[i*32:(i+1)*32,j*32:(j+1)*32]
        _r = r[i*32:(i+1)*32,j*32:(j+1)*32]
        _alpha = alpha[i*32:(i+1)*32,j*32:(j+1)*32]
        stack_img = cv2.merge((_b,_g,_r,_alpha))
        cv2.imwrite("static\Images\Runes\{}-{}.png".format(i,j),stack_img)
        