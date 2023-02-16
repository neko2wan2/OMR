import cv2
import numpy as np

def rectContour(contours):
    
    rectCon= []
    for i in contours:
        area= cv2.contourArea(i)
        
        if area>50:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            
            if len(approx)==4:
                rectCon.append(i)
    
    