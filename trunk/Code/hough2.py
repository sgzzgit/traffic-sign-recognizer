import cv2
import math

d_red = cv2.cv.RGB(150, 55, 65)
l_red = cv2.cv.RGB(250, 200, 200)

img = cv2.imread("Redfilter.jpg")
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detector = cv2.FeatureDetector_create('MSER')
fs = detector.detect(img2)
fs.sort(key = lambda x: -x.size)

def supress(x):
    for f in fs:
        distx = f.pt[0] - x.pt[0]
        disty = f.pt[1] - x.pt[1]
        dist = math.sqrt(distx*distx + disty*disty)
        if (f.size > x.size) and (dist<f.size/2):
            return True

sfs = [x for x in fs if not supress(x)]

for f in sfs:
        cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(f.size/2), d_red, 2, cv2.CV_AA)
        cv2.circle(img, (int(f.pt[0]), int(f.pt[1])), int(f.size/2), l_red, 1, cv2.CV_AA)

cv2.imwrite("circles_2.jpg", img)