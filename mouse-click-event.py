import cv2
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
clicked=0
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping,clicked
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
		print(refPt,cropping,1)
		clicked=0
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
		print(refPt,cropping,2)
		clicked=1
		# draw a rectangle around the region of interest




cap=cv2.VideoCapture(0)
_,image=cap.read()
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

while True:
	# display the image and wait for a keypress
	_,image=cap.read()
	cv2.imshow("image", image)

	if clicked==1:
		print(refPt,cropping,3)
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)

	key = cv2.waitKey(1) & 0xFF
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image = clone.copy()
	# if the 'c' key is pressed, break from the loop
	elif key == ord("q"):
		break
# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(refPt) == 2:
	roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imwrite("roi.jpg",roi)
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)
# close all open windows
cv2.destroyAllWindows()