import cv2, numpy as np

def drawRectangle(draw_im, candidate, col):
	x, y, r = candidate
	x, y, r = int(x), int(y), int(r) 
	cv2.rectangle(draw_im, (x-r,y-r), (x+r,y+r), col)

def getBestCandidates(c1, c2, prev, draw_im):
	bestCand = []
	for candidate in c1:
		drawRectangle(draw_im, candidate, (255, 0, 0))

	for candidate in c2:
		drawRectangle(draw_im, candidate, (0, 255, 0))

	for candidate in c1:
		if(len(getNeighbors(candidate, c2, 10)) != 0):
			bestCand.append(candidate)
		else:
			if(len(getNeighbors(candidate, prev, 30)) != 0):
				bestCand.append(candidate)	
	
	for candidate in c2:
		if(len(getNeighbors(candidate, c1, 10)) == 0):
			if(len(getNeighbors(candidate, prev, 30)) != 0):
				bestCand.append(candidate)

	for candidate in bestCand:
		drawRectangle(draw_im, candidate, (0, 0, 255))

	return bestCand, draw_im

def getNeighbors(c, circles, d):
	neighbors = []
	for circle in circles:
		if((c[0] >= circle[0]-d and c[0] <= circle[0]+d) or (c[1] >= circle[1]-d and c[1] <= circle[1]+d)):
			neighbors.append(circle)
	return neighbors

# def correlate(candidates, template_dst, cur_dst, draw_im):
# 	template_dst = np.asarray(template_dst).T
# 	tx, ty = template_dst.shape
# 	cx, cy = cur_dst.shape
# 	match_candidates = []
# 	for candidate in candidates:
# 		x, y, r = candidate
# 		x, y, r = int(x), int(y), int(r)
# 		col = (0, 255, 0)
# 		if(r > 20):
# 			cv2.rectangle(draw_im, (x-r,y-r), (x+r,y+r), col)
# 		else:
# 			cv2.rectangle(draw_im, (x-20,y-20), (x+20,y+20), col)
		
# 		startx = x-(tx/2)
# 		starty = y-(ty/2)
# 		if(startx >= 0 and starty >= 0 and startx+tx <= cx and starty+ty <= cy):
# 			trns = cur_dst[startx:startx+tx, starty:starty+ty]
# 			accu = 0
# 			for i in range(tx):
# 				for j in range(ty):
# 					accu = accu + trns[i, j]*template_dst[i, j]
# 			if(accu > 500000):
# 				startx = int(startx)
# 				starty = int(starty)
# 				cv2.rectangle(draw_im, (startx,starty), (startx+tx,starty+ty), (0, 0, 255))
# 	return match_candidates, draw_im