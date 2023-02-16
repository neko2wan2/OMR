import cv2
import numpy as np
import util
#
path = "test3.jpg"
imgW =700
imgH =700
choices = 4
questions = 10
scoreAns=[2,0,3,1,2,3,0,2,3,1]
score = 0
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
    pt1 = np.float32(biggestContour)
    pt2 = np.float32([[0,0],[imgW,0],[0,imgH],[imgW,imgH]])
    matrix = cv2.getPerspectiveTransform(pt1,pt2)
    imgWarpColored = cv2.warpPerspective(img,matrix,(imgW,imgH))
        
    imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWarpGray,190,255,cv2.THRESH_BINARY_INV)[1]
    
    ans = util.splitImg(imgThresh)
    
    pixelVal= np.zeros((questions,choices))
    countC=0
    countR=0
    
 #pixel count   
    for image in ans:
       totalPixels = cv2.countNonZero(image)
       pixelVal[countR][countC] = totalPixels
       countC +=1
        
       if (countC == choices): countR +=1; countC=0
    print(pixelVal)
    
 #checking answers   
    ansIndex=[]
    
    for x in range(0,questions):
        arr = pixelVal[x]
        
        indexVal = np.where(arr==np.amax(arr))
        ansIndex.append(indexVal[0][0])
    
    for x in range(0,questions):
        if ansIndex[x] == scoreAns[x]:
            score+=1
            
    
    print("Score: ",score," / ",questions)
    