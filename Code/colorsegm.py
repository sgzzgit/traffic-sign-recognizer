import cv2, numpy as np

def segmentRed(cv_im):
	hsv_im = cv2.cvtColor(cv_im, cv2.COLOR_BGR2HSV)
	h, s, v = cv2.split(hsv_im)
	r, sat_mask = cv2.threshold(s, 75, 1, cv2.THRESH_BINARY)
	# cv2.imwrite("../Temp/sat_mask.jpg", np.multiply(sat_mask, 255))
	r, h1 = cv2.threshold(h, 10, 255, cv2.THRESH_BINARY_INV)
	# cv2.imwrite("../Temp/filtered_hue1.jpg", h1)
	r, h2 = cv2.threshold(h, 230, 255, cv2.THRESH_BINARY)
	# cv2.imwrite("../Temp/filtered_hue2.jpg", h2)
	h = h1+h2
	# cv2.imwrite("../Temp/filtered_hue.jpg", h)
	h = h*sat_mask
	# r, h = cv2.threshold(h, 128, 255, 0)
	return h, sat_mask