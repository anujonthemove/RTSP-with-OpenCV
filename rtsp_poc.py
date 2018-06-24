'''
This code demonstrates a simple face detection model running on a video streamed over RTSP.
'''
import cv2 
import numpy as np


face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
rtsp_url = '<rtsp url>'
cap = cv2.VideoCapture(rtsp_url)


while True: 
 
    # reads frames from a camera
    ret, img = cap.read() 
 
    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    for (x,y,w,h) in faces:
        # draw rectangle on face(s) found
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_color = img[y:y+h, x:x+w]
 
 
    # Display an image in a window
    cv2.imshow('img',img)
 
    # Wait for Esc key to stop
    k = cv2.waitKey(1)
    if k == 27:
        break
 
# Close the window
cap.release()
 
# De-allocate any associated memory usage
cv2.destroyAllWindows() 