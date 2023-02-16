import cv2
import numpy as np

# Load the image
image = cv2.imread("test3.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the image to create a binary image
threshold = 100
ret, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

# Find circles in the binary image
circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Loop through the circles and check if they are shaded
for circle in circles[0]:
    # Extract the coordinates and radius of the circle
    x = int(circle[0])
    y = int(circle[1])
    r = int(circle[2])
    
    # Calculate the average color of the pixels within the circle
    mask = np.zeros(image.shape[:2], np.uint8)
    cv2.circle(mask, (x, y), r, 255, -1)
    mean_color = cv2.mean(image, mask=mask)
    
    # Check if the circle is shaded by comparing the average color to a threshold
    if mean_color[0] < 100:
        print("Circle is shaded")
    else:
        print("Circle is not shaded")