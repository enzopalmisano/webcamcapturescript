import cv2
import os
import time

PATH = "/home/virtual/Desktop/webcam/frames/"
camera = cv2.VideoCapture(0)
img_count = 1
dir_count = 1
if not os.path.exists(PATH+"01/"):
    os.makedirs(PATH+"01/")
path = PATH+"01/"

time.sleep(5)
while True:

    ret,frame = camera.read()
    cv2.imshow("test",frame)
    if not ret:
        break
    key =  cv2.waitKey(1)

    if img_count < 10:
        img_name = "00"+str(img_count)
    elif img_count >= 10 and img_count < 100:
        img_name = "0"+str(img_count)
    else:
        img_name = str(img_count)

    img_count += 1


    cv2.imwrite(path+img_name+".jpg", frame)

    if key%256 == 27:
        print("Exit")
        break



camera.release()
cv2.destroyAllWindows()
