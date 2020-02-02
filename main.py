import cv2
import numpy as np
import color
import centroid

cap = cv2.VideoCapture(2)
fps = cap.get(cv2.CAP_PROP_FPS)
print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))



while True:

  _, frame = cap.read()
  frame = cv2.resize(frame, (600, 400))

  frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  _, greenColor = color.get(frameHSV, green=True)
  _, redColor = color.get(frameHSV, red = True)

  greenCentroid = centroid.gets(frame, greenColor, green=True)
  redCentroid = centroid.gets(frame, redColor, red=True)

  if greenCentroid is not None:
    print('Centroid for Green : {}'.format(greenCentroid))

    if greenCentroid[1] < int(frame.shape[0]/2):
      print('Up')
    else:
      print('Down')

  if redCentroid is not None:
    print('Centroid for Red : {}'.format(redCentroid))

    if redCentroid[0] < int(frame.shape[0]/2):
      print('Left')
    else:
      print('Right')
  


  cv2.line(frame, (int(frame.shape[0]/2), 0), (int(frame.shape[0]/2) ,frame.shape[1]), (0, 0, 255), 3)
  cv2.line(frame, (0, int(frame.shape[0]/2)), (frame.shape[1], int(frame.shape[0]/2)), (255, 0, 0), 3)

  cv2.imshow('Frame', frame)
  if cv2.waitKey(1)==27:
    break
cap.release()
cv2.destroyAllWindows()