import cv2
import numpy as np

def rectContour(contours):
    
    rectCon= []
    for i in contours:
        area=cv2.contourArea(i)
        
        if area>50:
            peri = cv2.arcLength(i,True)
            approx = cv2.approxPolyDP(i,0.02*peri,True)
            
            if len(approx)==4:
                rectCon.append(i)
    
    rectCon = sorted(rectCon,key=cv2.contourArea,reverse=True)
    return rectCon

def getCornerPoints(cont):

    peri = cv2.arcLength(cont,True)
    approx = cv2.approxPolyDP(cont,0.02*peri,True)
    return approx
    
def reorder(rectPoints):

    rectPoints = rectPoints.reshape((4,2))
    rectPointsNew= np.seroz((4,1,2),np.int32)
    add = rectPoints.sum(1)
    rectPointsNew[0]= rectPoints[np.argmin(add)]
    rectPointsNew[3]= rectPoints[np.argmax(add)]
    diff = np.diff(rectPoints,axis=1)
    rectPointsNew[1]= rectPoints[np.argmin(diff)]
    rectPointsNew[2]= rectPoints[np.argmin(diff)]
    
    return rectPointsNew