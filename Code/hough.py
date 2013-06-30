import numpy as np
import cv2, time

def getCandidates(original, im):
	t1 = time.time()
	candidates = []
	gray_im = im
	draw_im = original

	blur = cv2.GaussianBlur(gray_im, (0,0), 2)
	result = cv2.HoughCircles(blur, cv2.cv.CV_HOUGH_GRADIENT, 2, 10, np.array([]), 30, 80, 1, 40)

	if(result == None):
		print "Returned nothing"
		circles = []
	else:
		circles = result[0]	

	circles = suppress(circles)
	
	for c in circles:
		crop = np.asarray(original)
		# candidates.append(crop[c[0]-c[2]:c[0]+c[2], c[1]-c[2]:c[1]+c[2]])
		cv2.circle(draw_im, (c[0],c[1]), c[2], (0,255,0), 2)
	
	t2 = time.time()
	# print "Time elapsed to detect circles", t2-t1
	# cv2.imwrite("circles.png", draw_im)
	return candidates, draw_im

def suppress(circles):
	scircles = []
	for c in circles:
		if(len(getNeighbors(c, scircles)) == 0):
			scircles.append(c)
	return scircles

def getNeighbors(c, circles):
	neighbors = []
	for circle in circles:
		if((c[0] >= circle[0]-30 and c[0] <= circle[0]+30) or (c[1] >= circle[1]-30 and c[1] <= circle[1]+30)):
			neighbors.append(circle)
	return neighbors