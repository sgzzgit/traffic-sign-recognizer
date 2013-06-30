import Image, cv
from colsegm import *
from hough import *
import os

# inpic = "test/1277381674Image000013.jpg"
# inpic = "test/1277381830Image000016.jpg"
# inpic = "test/1277381680Image000006.jpg"
# inpic = "test/1277381949Image000019.jpg"
# inpic = "test/1277391816Image000046.jpg"
	
vid = cv2.VideoCapture("../Videos/street.mp4")
# vid = cv2.VideoCapture("street2.avi")
# imgs = os.listdir("Test Sequence")

nFrames = int(vid.get(cv.CV_CAP_PROP_FRAME_COUNT))
fwidth = int(vid.get(cv.CV_CAP_PROP_FRAME_WIDTH))
fheight = int(vid.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter("../Results/detection.avi", cv2.cv.CV_FOURCC('M', 'P', 'E', 'G'), 29, (fwidth, fheight), 1)
aspect_ratio= fwidth*1.0/fheight
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
print nFrames

for i in range(40):
	cv_im = vid.read()[1]
	writer.write(cv_im)

for i in range(nFrames-40):
	cv_im = vid.read()[1]
	# cv_im = cv2.imread("Test Sequence/"+img)
	# red = segmentRed(cv_im)
	# cv2.imwrite("Redfilter.jpg", red)
	# r, red = cv2.threshold(red, 128, 255, 0)
	# cv2.imwrite("Redfilter_thresholded.jpg", red)
	# red = cv2.erode(red, element)
	# cv2.imwrite("Redfilter_eroded.jpg", red)
	# red = cv2.dilate(red, element)
	# cv2.imwrite("Redfilter_dilated.jpg", red)
	# hsv_im = cv2.cvtColor(cv_im, cv2.COLOR_RGB2HSV)
	# h, s, v = cv2.split(hsv_im)
	# r, h = cv2.threshold(h, 30, 255, cv2.THRESH_TOZERO)
	# cv2.imwrite("lower.jpg", h)
	# r, h = cv2.threshold(h, 200, 255, cv2.THRESH_TOZERO_INV)
	# cv2.imwrite("hue.jpg", h)
	h = cv2.cvtColor(cv_im, cv2.COLOR_RGB2GRAY)
	# cv2.imwrite("gray.jpg", h)
	candidates, draw_im = getCandidates(cv_im, h)
	# cv2.imwrite("test/frame"+str(i)+".jpg", draw_im)
	writer.write(draw_im)
	print "Processed frame", i