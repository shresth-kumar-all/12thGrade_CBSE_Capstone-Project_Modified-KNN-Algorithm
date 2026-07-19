import cv2
img=cv2.imread("C:\\Users\\Admin\\Desktop\\Movies Posters\\l_1843866_44560b79.jpg")
nw=205
nh=250
rimg=cv2.resize(img,(nw,nh))
cv2.imwrite("C:\\Users\\Admin\\Desktop\\Movies Posters\\converted\\CAPTAINAMERICAWINTERSOLDIER.PNG",rimg)
