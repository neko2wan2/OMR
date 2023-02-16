import cv2
import numpy as np
import util
#
path = "test3.jpg"
imgW =700
imgH =700
#

#ImageConversion
img=cv2.imread(path)
img = cv2.resize(img,(imgW,imgH))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,10,50)


#findingContours
contours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#findRectangles
rectCon = util.rectContour(contours)
biggestContour = util.getCornerPoints(rectCon[0])

if biggestContour.size !=0:
    
    biggestContour=util.reorder(biggestContour)
    print(biggestContour)
    pt1 = np.float32(biggestContour)
    pt2 = np.float32([[0,0],[imgW,0],[0,imgH],[imgW,imgH]])
    matrix = cv2.getPerspectiveTransform(pt1,pt2)
    imgWarpColored = cv2.warpPerspective(img,matrix,(imgW,imgH))
    
    cv2.imshow("test",imgWarpColored)
    cv2.waitKey(0)