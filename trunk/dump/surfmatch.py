import cv2, os, numpy as np, cv, math

def getFeatures(img_path):
	
	# Initialize the surf detectors
	surfDetector = cv2.FeatureDetector_create("SURF")
	detector = cv2.GridAdaptedFeatureDetector(surfDetector, 50)
	surfDescriptorExtractor = cv2.DescriptorExtractor_create("SURF")

	# Open image in grayscale
	im = cv2.imread(img_path, cv2.CV_LOAD_IMAGE_COLOR)
	img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
	
	# Detect keypoints and compute descriptors
	keypoints = detector.detect(img)
	(keypoints, descriptors) = surfDescriptorExtractor.compute(img,keypoints)
	
	# Draw detected keypoints on image
	for kp in keypoints:
		x = int(kp.pt[0])
		y = int(kp.pt[1])
		cv2.circle(im, (x, y), 5, (255, 0, 0))

	cv2.imwrite("features/"+img_path, im)
	return keypoints, descriptors

def match(d1, d2, threshold):

	# Initialize FLANN Matcher
	FLANN_INDEX_KDTREE = 1
	flann_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 4)
	flann = cv2.flann_Index(d1, flann_params)

	# Perform matching
	idx2, dist = flann.knnSearch(d2, 2, params = {})
	mask = dist[:,0] / dist[:,1] < threshold
	idx1 = np.arange(len(d2))
	pairs = np.int32( zip(idx1, idx2[:,0]) )

	return pairs[mask]

def compare(img1, img2):
	
	kp1, d1 = getFeatures(img1)
	kp2, d2 = getFeatures(img2)
	if(len(kp1) == 0):
		print "No keypoints found"
		return 0
	else:	
		matchPairs = match(d1, d2, 0.6)
		return len(matchPairs)

def bestMatches(name, comparison, dbpics_, n):
	i = np.argmax(comparison)
	print "A best match image for", name, "is", dbpics_[i]
	if n>1:
		dbpics_ = np.delete(dbpics_, i)
		comparison = np.delete(comparison, i)
		bestMatches(name, comparison, dbpics_, n-1)

def getBestMatchFor(img):
	dbpics = os.listdir("Database")
	results = []
	for dbpic in dbpics:
		matches = compare(img, "Database/"+dbpic)
		results.append(matches)
	#print results	
	bestMatches(img, results, dbpics, 3)