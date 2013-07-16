import Image, cv2

def getDstTrns(img, name):
	h = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edge = cv2.Canny(h, 100, 150)
	if(edge.shape[1] < 521):
		edge = cv2.resize(edge, (521, 521))
	r, edge = cv2.threshold(edge, 128, 255, cv2.THRESH_BINARY_INV)
	edge = cv2.erode(edge, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)))
	cv2.imwrite(name+"_canny.jpg", edge)
	dst = cv2.distanceTransform(edge, cv2.cv.CV_DIST_L2, 5)
	cv2.imwrite(name+"_dst.jpg", dst)
	return dst