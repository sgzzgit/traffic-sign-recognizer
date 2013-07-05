import Image, cv2

def getDstTrns(img):
	# img = cv2.imread("template.jpg")
	h = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edge = cv2.Canny(h, 128, 200)
	r, edge = cv2.threshold(edge, 128, 255, cv2.THRESH_BINARY_INV)
	# cv2.imwrite("template_canny.jpg", edge)
	dst = cv2.distanceTransform(edge, cv2.cv.CV_DIST_L2, 5)
	# cv2.imwrite("template_dst.jpg", dst)
	return dst