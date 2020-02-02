import cv2
import numpy as np

def get(img, red = False, blue = False, green = False):
  if (green == True):
    lowerBound = np.array([25, 120, 80])
    upperBound = np.array([102, 255, 255])
  
  if (red == True):
    lowerBound = np.array([161, 120, 80])
    upperBound = np.array([179, 255, 255])

  mask = cv2.inRange(img, lowerBound, upperBound)

  opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, (5,5))
  closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, (20,20))

  return mask, closing