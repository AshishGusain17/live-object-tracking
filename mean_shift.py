import cv2
import numpy as np

def func2():        
    video = cv2.VideoCapture(0)

    _, first_frame = video.read()
    file1 = open("myfile.txt","r+")
    loc=file1.read()
    print(loc)
    loc = loc.split()
    print(loc)
    x = int(loc[0])
    y = int(loc[1])
    width = int(loc[2]) - int(loc[0])
    height = int(loc[3]) - int(loc[1])
    print(x,y,width,height)
    roi = cv2.imread("roi.jpg")
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
    # roi_hist = cv2.calcHist([hsv_roi], [0,1], None, [180,256], [0, 180,0,255])

    roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    while True:
        (_, frame) = video.read()
        cv2.namedWindow("Frame", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

        hsv_original=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask = cv2.calcBackProject([hsv_original], [0], roi_hist, [0, 180], 1)
        mask=cv2.blur(mask,(5,5))

        _, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
        _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)

        x,y,width,height=track_window
        cv2.rectangle(frame,(x,y), (x+width, y + height),123,2)
        
        cv2.putText(frame, "Press q to get back to the webpage.", (5,25), cv2.FONT_HERSHEY_PLAIN, 1, (254,34,56), 1)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()
    