# -*- coding: utf-8 -*-
#-*-coding:utf-8-*-
import cv2
import numpy as np

def cvtBackground(path,color):
    """
        功能：给证件照更换背景色（常用背景色红、白、蓝）
        输入参数：path:照片路径
                color:背景色 <格式[B,G,R]>
    """
    im=cv2.imread(path)
    im_hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    aim=np.uint8([[im[0,0,:]]])
    hsv_aim=cv2.cvtColor(aim,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(im_hsv,np.array([hsv_aim[0,0,0]-5,100,100]),np.array([hsv_aim[0,0,0]+5,255,255]))
    mask_inv=cv2.bitwise_not(mask)
    img1=cv2.bitwise_and(im,im,mask=mask_inv)
    bg=im.copy()
    rows,cols,channels=im.shape
    bg[:rows,:cols,:]=color
    img2=cv2.bitwise_and(bg,bg,mask=mask)
    img=cv2.add(img1,img2)
    image={'im':im,'im_hsv':im_hsv,'mask':mask,'img':img}
    for key in image:
        cv2.namedWindow(key)
        cv2.imshow(key,image[key])
    cv2.waitKey(0)
    return img
#test
if __name__=='__main__':
    img=cvtBackground("C:\\Users\\Administrator\\Desktop\\44018056.jpg",[255,255,255])