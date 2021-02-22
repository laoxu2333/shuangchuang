import cv2
import numpy as np



def getContours(img,N):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>150:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            # if objCor ==3: objectType ="Tri"
            # elif objCor == 4:
            #     aspRatio = w/float(h)
            #     if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
            #     else:objectType="Rectangle"
            # elif objCor>4: objectType= "Circles"
            # else:objectType="None"
            if N==0:objectType="red"
            elif N==1: objectType="green"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)

img = cv2.imread("source/hld2.jpg")
img=cv2.resize(img,(0,0),fx=0.8,fy=0.8,interpolation=cv2.INTER_NEAREST)
imgContour = img.copy()
#红绿灯2的HSV范围
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_hsv_red = np.array([100,110,153])
upper_hsv_red = np.array([179,240,255])
mask_red = cv2.inRange(hsv,lowerb=lower_hsv_red,upperb=upper_hsv_red)
red_blur = cv2.medianBlur(mask_red, 7)

lower_hsv_green = np.array([40,18,153])
upper_hsv_green = np.array([140,240,255])
mask_green = cv2.inRange(hsv,lowerb=lower_hsv_green,upperb=upper_hsv_green)
    #中值滤波
#红绿灯1的HSV范围
# hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# lower_hsv_red = np.array([0,110,153])
# upper_hsv_red = np.array([18,240,255])
# mask_red = cv2.inRange(hsv,lowerb=lower_hsv_red,upperb=upper_hsv_red)
# red_blur = cv2.medianBlur(mask_red, 7)
#
# lower_hsv_green = np.array([44,90,153])
# upper_hsv_green = np.array([89,245,255])
# mask_green = cv2.inRange(hsv,lowerb=lower_hsv_green,upperb=upper_hsv_green)

green_blur = cv2.medianBlur(mask_green, 7)

getContours(red_blur,0)
getContours(green_blur,1)
# x, y, w, h = cv2.boundingRect(img)
#
# img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
cv2.imshow('img',img)
cv2.imshow('red_window',red_blur)
cv2.imshow('green_window',green_blur)
cv2.imshow('imgContour',imgContour)


# kernel=np.ones((5,5),np.uint8)
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)
# imgCanny=cv2.Canny(img,100,100)
# opening=cv2.morphologyEx(imgGray,cv2.MORPH_OPEN,kernel)
# closing=cv2.morphologyEx(imgGray,cv2.MORPH_CLOSE,kernel)
#
# cv2.imshow("Gray image",imgGray)
# cv2.imshow("opening image",opening)
# cv2.imshow("closing image",closing)
cv2.waitKey(0)