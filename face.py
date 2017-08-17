# -*- coding: utf-8 -*-
import picamera
import cv2
import time
cascade_path = "/usr/local/opt/opencv/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml"

color = (255, 0, 0) #白
cascade = cv2.CascadeClassifier(cascade_path)
cv2.namedWindow('Output_Image', cv2.WINDOW_NORMAL)
camera = picamera.PiCamera()
camera.resolution = (640, 480)  ##2592,1944

while 1:
	img_path = './image.jpg'
  camera.capture(img_path)
  image = cv2.imread(img_path,1)
  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=1, minSize=(1, 1))
  print "face rectangle"
  print facerect
  if len(facerect) > 0:
    for rect in facerect:
        cv2.rectangle(image, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)

    cv2.imshow("Output_Image", image)
    cv2.waitKey(1)
	time.sleep(100)
cv2.destroyAllWindows()


