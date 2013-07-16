from pytesser import *
import cv2
import numpy as np

def directOCR(img):
	return image_file_to_string(img)

def readChar(img):
	im = cv2.imread(img)
	r, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY_INV)
	im = cv2.dilate(im, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)))
	cv2.imwrite("test2.jpg", im)
	return image_file_to_string("test2.jpg")

def readImage(img, name):
	r, im = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
	cv2.imwrite(name+"_inverted.jpg", im)
	contours, hierarchy = cv2.findContours(im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	print "Found", len(contours), "components"
	i = 1
	rects = []
	for c in contours:
		rect = cv2.boundingRect(c)
		#cv2.rectangle(img, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (128, 128, 128))
		rects.append(rect[2]*rect[3])

	
	circleI = np.argmax(rects)
	rects.pop(circleI)
	circleI = np.argmax(rects)
	rect = cv2.boundingRect(contours[circleI])
	cv2.rectangle(img, (rect[0], rect[1]), (rect[0]+rect[2], rect[1]+rect[3]), (128, 128, 128))
	cv2.imwrite(name+"_components.jpg", img)
