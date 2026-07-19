import cv2
img=cv2.imread("D:\\0- Sanny AI capstone\\The Inheritance Cycle.jpg")
nw=205
nh=250
rimg=cv2.resize(img,(nw,nh))
cv2.imwrite("D:\\0- Sanny AI capstone\\resized images\\The Inheritance Cycle.PNG",rimg)

