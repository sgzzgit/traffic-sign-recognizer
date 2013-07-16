import Image, colorsys, cv2

def filterRed(h):

	# Set values for color region of interest
	i_min = 30
	i_max = 220

	# Attenuate other colors
	if(h >= 0 and h <= i_min):
		h_new = 255*(i_min-h)/i_min
	else:
		if(h > i_min and h < i_max):
			h_new = 0
		else:
			h_new = 255*(h-i_max)/i_max

	return h_new

def segmentRed(im):
	
	# im_pix = im.load()
	im_pix = im
	red = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

	for i in range(im.shape[0]):
		for j in range(im.shape[1]):

			# Read color at the pixel
			pixel = im_pix[i, j]
			b = pixel[0]
			g = pixel[1]
			r = pixel[2]
			
			# If all colors channels are equal attentuate red channel
			if(r == g and g == b):
				if(r == 0):
					g = 255
				else:
					r = 0

			# Convert to HSV color space	
			h, s, v = colorsys.rgb_to_hsv(r/255.,g/255.,b/255.)
			
			# Apply Filter to boost red color and attenuate other colors
			hr = filterRed(h*255)

			# Save result to new image
			red[i, j] = hr

	return red

def filterBlue(h, s):
	h = h*255
	s = s*255

	i_min = 125
	i_max = 175
	if(h >= i_min and h <= i_max):
		d = 25-np.absolute(150-h)
		h_new = 255*d/25
	else:
		h_new = 0

	s_min = 230
	if(s < s_min):
		s_new = s
	else:
		s_new = 255	

	return h_new, s_new