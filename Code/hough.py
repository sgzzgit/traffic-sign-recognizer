import numpy as np
import cv2, time

def getCandidates(im):
	t1 = time.time()
	candidates = []
	gray_im = im

	blur = cv2.GaussianBlur(gray_im, (0,0), 2)
	result = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 2, 10, np.array([]), 40, 50, 1, 50)

	if(result == None):
		# print "Returned nothing"
		circles = []
	else:
		circles = result[0]	

	circles = suppress(circles)
	
	count = 0
	for c in circles:
		candidates.append(c)
	return candidates

def suppress(circles):
	scircles = []
	for c in circles:
		if(len(getNeighbors(c, scircles, 30)) == 0):
			scircles.append(c)
	return scircles

def getNeighbors(c, circles, d):
	neighbors = []
	for circle in circles:
		if((c[0] >= circle[0]-d and c[0] <= circle[0]+d) or (c[1] >= circle[1]-d and c[1] <= circle[1]+d)):
			neighbors.append(circle)
	return neighbors