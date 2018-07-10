import cv2
import numpy as np
import sys
import argparse

# Edge detection limits
min = 250
max = 850
winW = 500
winH = 500


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="first input image")
args = vars(ap.parse_args())

base = cv2.imread(args["first"])

baseSize = cv2.resize(base, (winW, winH))
baseGray = cv2.cvtColor(baseSize,cv2.COLOR_BGR2GRAY)
baseBlur = cv2.medianBlur(baseGray,5)

circles = cv2.HoughCircles(baseBlur,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=30,maxRadius=50)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
	# draw the outer circle
	cv2.circle(baseSize,(i[0],i[1]),i[2],(0,255,0),2)
	print("{},{},{}".format(i[0],i[1],i[2]))
	

#Edge detection setup
#baseCanny = cv2.Canny(baseGray,min,max)

#Min Enclosing Circle Setup
#ret, thresh = cv2.threshold(baseCanny, 127, 255, 0)

# Find contours
#thresh2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Circling contours
# for cnt in contours:
	# (x,y),radius = cv2.minEnclosingCircle(cnt)
	# if radius > 30:
		# center = (int(x),int(y))
		# radius = int(radius)
		# cv2.circle(baseSize,center,radius,(0,255,0),2)
		# print("R,X,Y = {},{},{}".format(radius,x,y))
	
#Showing images
#cv2.imshow("canny", baseCanny)
cv2.imshow("Original", baseSize)
#cv2.imshow("Threshold",thresh)

cv2.waitKey()

# while(1):
	# baseCanny = cv2.Canny(baseSize,min,max)

	# cv2.imshow("canny", baseCanny)
	
	# k = cv2.waitKey(20)
	
	# if k%256 == 27:
		# sys.exit(0)
	
	# elif k%256 == 119: # 'w'
		# max += 5
		# print("Max: {}".format(max))
		
	# elif k%256 == 115: # 's'
		# max -= 5
		# print("Max: {}".format(max))
	
	# elif k%256 == 97: # 'a'
		# min -= 5
		# print("Min: {}".format(min))
		
	# elif k%256 == 100: # 'd'
		# min += 5
		# print("Min: {}".format(min))