import cv2
img=cv2.imread("D:\\02-PROGRAM\\01-Work-AI\\Capstone\\0-Global_Run_Method-Final\\0-Global_Run_Method-Final\\Poison-Dragon-The-Legend-of-an-Asura.jpeg")
nw=205
nh=250
rimg=cv2.resize(img,(nw,nh))
cv2.imwrite("D:\\02-PROGRAM\\01-Work-AI\\Capstone\\0-Global_Run_Method-Final\\0-Global_Run_Method-Final\\UI_Assets\\4\\Legend of Asura - The Venom Dragon.PNG",rimg)
#Legend of Asura - The Venom Dragon