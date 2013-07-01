import Image, cv
from colorsegm import *
from hough import *
import os

vid = cv2.VideoCapture("../Videos/street.mp4")
# vid = cv2.VideoCapture("../Videos/street2.avi")

nFrames = int(vid.get(cv.CV_CAP_PROP_FRAME_COUNT))
fwidth = int(vid.get(cv.CV_CAP_PROP_FRAME_WIDTH))
fheight = int(vid.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter("../Results/detection.avi", cv2.cv.CV_FOURCC('M', 'P', 'E', 'G'), 29, (fwidth, fheight), 1)
aspect_ratio= fwidth*1.0/fheight

element1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13))
element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

for i in range(nFrames):
	cv_im = vid.read()[1]
	
	# Preprocess Image
	h = segmentRed(cv_im)
	h = cv2.dilate(h, element1)
	h = cv2.erode(h, element2)
	# cv2.imwrite("hue_"+str(i)+".jpg", h)
	
	# Detect circles in the frame
	candidates, draw_im = getCandidates(cv_im, h)
	
	cv2.imwrite("frame_"+str(i)+".jpg", draw_im)
	writer.write(draw_im)
	
	print "Processed frame", i