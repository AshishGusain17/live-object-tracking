import cv2
import numpy as np
# video = cv2.VideoCapture("mouthwash.avi")

def func():
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

    # roi = first_frame[y: y + height, x: x + width]
    roi = cv2.imread("roi.jpg")
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
    roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
    term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    while True:
        _, frame = video.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        _, track_window = cv2.meanShift(mask, (x, y, width, height), term_criteria)
        x, y, w, h = track_window
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Mask", mask)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()
    