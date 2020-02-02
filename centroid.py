import cv2

def gets(img, contour, red = False, green = False, blue = False):

  contours, _ = cv2.findContours(contour, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  for cont in contours:
    if cv2.contourArea(cont)>500:
      x, y, w, h = cv2.boundingRect(cont)
      centroid = (int(x+w/2),int(y+h/2))

      if red == True:
        cv2.circle(img, centroid, 3, (0, 0 ,255), 2) 
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0 ,255), 3)

      if green == True:
        cv2.circle(img, centroid, 3, (0, 255 ,0), 2) 
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255 ,0), 3)

      if blue == True:
        cv2.circle(img, centroid, 3, (255, 0 ,0), 2) 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
      return centroid
'''      if centroidGreen[1] < int(img.shape[0]/2):
        print('UP')
      else:
        print('Down')'''
      
      