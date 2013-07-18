import Image, cv
from colorsegm import *
from hough import *
from dstCorrelation import *
import os
import numpy as np

clearCandidates()

# Working:
# Street2 (2/2)
# Street6 (1/1)
# Street8 (1/2)
# Street11 (1/1)
# Street13 (1/1)
# Street14 (1/1)
# Street15 (1/1)
# Street17 (1/1)
# Street18 (1/1)

# Not working:
# Street (1/1) --> different colors
# Street8 (1/2)
# Street10 (2/2)

# Bad Videos (do not contain available signs or bad detection):
# Street3
# Street4 
# Street5
# Street7
# Street9
# Street12
# Street16

# vid = cv2.VideoCapture("../Videos/street.mp4")
vid = cv2.VideoCapture("../Videos/street13.avi")

nFrames = int(vid.get(cv.CV_CAP_PROP_FRAME_COUNT))
fwidth = int(vid.get(cv.CV_CAP_PROP_FRAME_WIDTH))
fheight = int(vid.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter("../Results/detection.avi", cv2.cv.CV_FOURCC('M', 'P', 'E', 'G'), 29, (fwidth, fheight), 1)
# writer = cv2.VideoWriter("../Results/test_result.avi", cv2.cv.CV_FOURCC('M', 'P', 'E', 'G'), 29, (fwidth, fheight), 1)

element1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(13,13))
element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))
match_candidates= []
last_first = None
successive = 0
coeff = 0

# for i in range(24):
# 	cv_im = vid.read()[1]

dbpics = os.listdir("Database")
recognitions = np.zeros(len(dbpics))
count = 0

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
	match_candidates, draw_im, pics = getBestCandidates(candidates, edgeCandidates, match_candidates, cv_im)

	if(len(match_candidates) == 0):
		count = count + 1
		if(count == 10):
			if(np.amax(recognitions) != 0):
				print recognitions
				print "Best match is", dbpics[np.argmax(recognitions)]
			recognitions = np.zeros(len(dbpics))
	else:
		count = 0
		for cand in pics:
			rec_candidates = recognize(cand)
			if(rec_candidates != None):
				if(rec_candidates[0] == last_first):
					successive = successive + 1
					coeff = coeff+10
				else:
					successive = 0
					coeff = 10
				if(successive > 10):
					if(successive == 10):
						print recognitions
						print "Best match is", dbpics[np.argmax(recognitions)]
				else:
					recognitions[rec_candidates[0]] = recognitions[rec_candidates[0]] + coeff
					recognitions[rec_candidates[1]] = recognitions[rec_candidates[1]] + 1
					last_first = rec_candidates[0]

	# cv2.imwrite("../Temp/frame_"+str(i)+".jpg", draw_im)
	writer.write(draw_im)
	# print "Processed frame", i, recognitions

if(np.amax(recognitions) != 0):
	print recognitions
	print "Best match is", dbpics[np.argmax(recognitions)]