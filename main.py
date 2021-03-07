import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#读取图像
img = cv.imread("venv/wife.jpg")
#
# #高斯降噪
#jimg = cv.GaussianBlur(img,(3,3),1)
#
# #画直线
# cv.line(img,(0,0),(800,1000),(0,0,255),10)
# cv.line(img,(800,0),(0,1000),(0,0,255),10)
#
# #画圆
# cv.circle(img,(380,840),100,(255,255,255),50)
#
# #画矩形
# cv.rectangle(img,(1,1),(800,1000),(255,0,0),10)
#
# #写字
# cv.putText(img,"W a n t e d",(50,500),cv.FONT_HERSHEY_SCRIPT_COMPLEX,4,(0,255,0),5)
#
# #创建核结构
# M = np.ones((5,5),np.uint8)
# print(M)
#
# #腐蚀
# fimg = cv.erode(img,M,10)
#
# #膨胀
# pimg = cv.dilate(img,M)
#
# #开闭运算
# kimg = cv.morphologyEx(img,cv.MORPH_OPEN,M)     #kai
# bimg = cv.morphologyEx(img,cv.MORPH_CLOSE,M)     #bi
#
#hat运算
# himg = cv.morphologyEx(img,cv.MORPH_BLACKHAT,M)
# himg = cv.morphologyEx(img,cv.MORPH_TOPHAT,M)
#
# #Canny边缘检测
# jimg = cv.GaussianBlur(img,(3,3),1)
# canny = cv.Canny(jimg,0,100)
# #Canny函数返回的是二值图？
# #显示要用： plt.imshow(canny,cmap=plt.cm.gray)
#
# #提高图像对比度（自适应均衡化）
# clahe = cv.createCLAHE(2.0,(8,8))
# cl1 = clahe.apply(img)
# #要以灰度图读取img，也要以灰度图形式显示

#plt显示
plt.imshow(img[:,:,::-1])
plt.title('wife')
plt.show()