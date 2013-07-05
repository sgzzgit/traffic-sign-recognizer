import cv2, numpy as np
from dstTransform import *

img = cv2.imread("template.jpg")
dst = getDstTrns(img)
maxi = np.amax(dst)
dst = np.multiply(dst, 255/maxi)
cv2.imwrite("template_dst.jpg", dst)