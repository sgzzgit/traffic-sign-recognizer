import cv2

def segmentRed(cv_im):
	hsv_im = cv2.cvtColor(cv_im, cv2.COLOR_BGR2HSV)
	h, s, v = cv2.split(hsv_im)
	r, h = cv2.threshold(h, 30, 255, cv2.THRESH_TOZERO)
	r, h = cv2.threshold(h, 200, 255, cv2.THRESH_TOZERO_INV)
	r, h = cv2.threshold(h, 128, 255, 0)
	return h