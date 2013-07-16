import Image, cv2, time, numpy as np
from colsegm import *

def filterRed(h):
	# Set values for color region of interest
	i_min = 30
	i_max = 220

	# Attenuate other colors
	if(h >= 0 and h <= i_min):
		h_new = 255*(i_min-h)/i_min
	else:
		if(h > i_min and h < i_max):
			h_new = 0
		else:
			h_new = 255*(h-i_max)/i_max

	return h_new

im = cv2.imread("test/1277381830Image000016.jpg")
t1 = time.time()
hsv_im = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv_im)
t2 = time.time()
print "RGB to HSV", t2-t1
t3 = time.time()
print "Filtering", t3-t2
print h_new