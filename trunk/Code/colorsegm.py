import cv2

def segmentRed(cv_im):
	hsv_im = cv2.cvtColor(cv_im, cv2.COLOR_BGR2HSV)
	h, s, v = cv2.split(hsv_im)
	r, sat_mask = cv2.threshold(s, 75, 1, cv2.THRESH_BINARY)
	# cv2.imwrite("../Temp/sat_mask.jpg", sat_mask)
	r, h1 = cv2.threshold(h, 10, 255, cv2.THRESH_BINARY_INV)
	r, h2 = cv2.threshold(h, 230, 255, cv2.THRESH_BINARY)
	h = h1+h2
	h = h*sat_mask
	# r, h = cv2.threshold(h, 128, 255, 0)
	return h, sat_mask