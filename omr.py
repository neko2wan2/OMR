import cv2
import numpy as np
import util
#
path = "test.jpg"
#

#ImageConversion
img=cv2.imread(path)
#img = cv2.resize(700,700)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,10,50)

#findingContours
contours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#findRectangles
util.rectContour(contours)
