import Image, cv2, os, numpy as np

imgs = os.listdir("../Video Sequence")

im1 = cv2.imread("../Video Sequence/"+imgs[0])
im1= np.asarray(im1)
fheight = im1.shape[0]
fwidth = im1.shape[1]

writer = cv2.VideoWriter("../Videos/street5.avi", cv2.cv.CV_FOURCC('M', 'P', 'E', 'G'), 29, (fwidth, fheight), 1)

for img in imgs:
	im = cv2.imread("../Video Sequence/"+img)
	im = np.asarray(im)
	for i in range(2):
		writer.write(im)
