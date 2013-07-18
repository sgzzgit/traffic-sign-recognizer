import cv2, numpy as np, os
from colorsegm import *

element1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13))
element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

def bestMatches(name, comparison, dbpics_, n):
	i = np.argmin(comparison)
	results = []
	# print "A best match image for", name, "is", dbpics_[i]
	results.append(i)
	if n>1:
		dbpics_ = np.delete(dbpics_, i)
		comparison = np.delete(comparison, i)
		res = bestMatches(name, comparison, dbpics_, n-1)
		results = results + res	
	return results

def getBestMatchDst(img):
	im = cv2.imread(img)
	h, s = segmentRed(im)
	result = cv2.HoughCircles(h, cv2.cv.CV_HOUGH_GRADIENT, 2, 10, np.array([]), 40, 50, 14, 50)
	if(result != None):
		# print result	
		dbpics = os.listdir("Database")
		results = []
		for dbpic in dbpics:
			# matches = compare(img, "Database/"+dbpic)
			matches = templateMatch(img, "Database/"+dbpic)
			results.append(matches)
			# print dbpic, matches
		#print results	
		return bestMatches(img, results, dbpics, 3)

def templateMatch(im1, im2):
	img1 = cv2.imread(im1)
	img1 = cv2.resize(img1, (60, 60))
	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
	img1 = cv2.equalizeHist(img1)

	img2 = cv2.imread(im2)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	img2 = cv2.equalizeHist(img2)
	results = []
	for i in range(25, 50, 5):
		template = cv2.resize(img2, (i, i))
		# cv2.imwrite("image.jpg", img1)
		# cv2.imwrite("template_"+str(i)+".jpg", template)
		match = cv2.matchTemplate(img1, template, cv2.cv.CV_TM_SQDIFF_NORMED) 
		results.append(np.amin(match))
	return np.amin(results)