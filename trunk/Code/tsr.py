import Image, cv
from colorsegm import *
from hough import *
from dstCorrelation import *
import os

# vid = cv2.VideoCapture("../Videos/street.mp4")
vid = cv2.VideoCapture("../Videos/street5.avi")

nFrames = int(vid.get(cv.CV_CAP_PROP_FRAME_COUNT))
fwidth = int(vid.get(cv.CV_CAP_PROP_FRAME_WIDTH))
fheight = int(vid.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter("../Results/detection_street5.avi", cv2.cv.CV_FOURCC('M', 'P', 'E', 'G'), 29, (fwidth, fheight), 1)
# writer = cv2.VideoWriter("../Results/test_result.avi", cv2.cv.CV_FOURCC('M', 'P', 'E', 'G'), 29, (fwidth, fheight), 1)
aspect_ratio= fwidth*1.0/fheight

element1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13))
element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
match_candidates= []

# for i in range(24):
# 	cv_im = vid.read()[1]

for i in range(nFrames):
	cv_im = vid.read()[1]
	
	# Preprocess Image
	h, s = segmentRed(cv_im)
	h = cv2.dilate(h, element1)
	h = cv2.erode(h, element2)

	# cv2.imwrite("../Temp/hue_frame_"+str(i)+".jpg", h)
	draw_im = cv_im
	
	# Find circles on edges
	edgeh = cv2.Canny(h, 128, 200)
	# cv2.imwrite("../Temp/edge_frame_"+str(i)+".jpg", edgeh)
	edgeCandidates = getCandidates(edgeh)

	# Detect circles in the frame
	candidates = getCandidates(h)
	match_candidates, draw_im = getBestCandidates(candidates, edgeCandidates, match_candidates, cv_im)

	# cv2.imwrite("../Temp/frame_"+str(i)+".jpg", draw_im)
	writer.write(draw_im)
	print "Processed frame", i