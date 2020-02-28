import cv2

def func1():	
	refPt = []
	cropping = False
	clicked=0
	print(refPt,cropping,clicked)
	def click_and_crop(event, x, y, flags, param):
		nonlocal refPt, cropping, clicked

		# if the left mouse button was clicked
		if event == cv2.EVENT_LBUTTONDOWN:
			refPt = [(x, y)]
			cropping = True
			print(refPt,cropping,clicked,1)
			clicked=0
			print(refPt,cropping,clicked,1)

		# check to see if the left mouse button was released
		elif event == cv2.EVENT_LBUTTONUP:
			refPt.append((x, y))
			cropping = False
			print(refPt,cropping,clicked,2)
			clicked=1
			print(refPt,cropping,clicked,2)


	cap=cv2.VideoCapture(0)
	_,image=cap.read()
	clone = image.copy()
	cv2.namedWindow("Crop", cv2.WND_PROP_FULLSCREEN)
	cv2.setMouseCallback("Crop", click_and_crop)

	while True:
		_,image=cap.read()
		
		cv2.setWindowProperty("Crop",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		if clicked==1:
			print(refPt,cropping,3)
			cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
			cv2.putText(image, "Press q if object is in the frame and r to crop the object again.", (5,25), cv2.FONT_HERSHEY_PLAIN, 1, (254,34,56), 1)
			cv2.imshow("Crop", image)
		else:
			cv2.putText(image, "Drag the mouse and select the object.", (5,25), cv2.FONT_HERSHEY_PLAIN, 1, (254,34,56), 1)
			cv2.imshow("Crop", image)

		key = cv2.waitKey(1) & 0xFF
		# if the 'r' key is pressed, reset the cropping region
		if key == ord("r"):
			image = clone.copy()
			clicked=0
		# if the 'c' key is pressed, break from the loop
		elif key == ord("q"):
			break
	# if there are two reference points, then crop the region of interest
	# from teh image and display it
	if len(refPt) == 2:
		roi = image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
		file1 = open("myfile.txt","w")
		file1.write(str(refPt[0][0]) + ' ')
		file1.write(str(refPt[0][1]) + ' ')
		file1.write(str(refPt[1][0]) + ' ')
		file1.write(str(refPt[1][1]) + ' ')
		file1.close() 

		cv2.imwrite("roi.jpg",roi)
		cv2.imwrite("static/img/roi.jpg",roi)
		cv2.imshow("ROI", roi)
		cv2.waitKey(0)

	cap.release()
	cv2.destroyAllWindows()