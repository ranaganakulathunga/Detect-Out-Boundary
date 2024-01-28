
import cv2
import numpy as np

def process_image(image_path):
   
    image = cv2.imread(image_path)

  
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    lower_orange = np.array([0, 100, 100])
    upper_orange = np.array([20, 255, 255])

 
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

  
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   
    result = image.copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)

  
    cv2.imshow('Orange Bounding Boxes', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


process_image('Orange Fruits.jpg')
