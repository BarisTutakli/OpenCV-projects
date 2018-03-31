import cv2
import os

#in this pyfile ı read images and show them

print(os.getcwd())# to learn location of file

path=os.getcwd()
files=os.listdir(path)# to list files
resim_dosyaları=[i for i in files if i.endswith(".jpg")]
# in this part, I have found the files ending with .jpg


for j in resim_dosyaları:
    #new_size of picture =cv2.resize(j,(200,200))
    img=cv2.imread(j)
    new_img=cv2.resize(img,(400,400))

    cv2.imshow("ben",new_img)
    cv2.waitKey(0)



#img=cv2.imread("bar.jpg",-1)
#yeni_boyut=cv2.resize(img,(400,400))
#cv2.imshow("ben",yeni_boyut)
#cv2.waitKey()
#destrotAllindow     this method close all windows
