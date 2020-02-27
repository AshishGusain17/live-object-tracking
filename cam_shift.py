import cv2
import numpy as np

def func():
    roi = cv2.imread("roi.jpg")

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

    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
    roi_hist = cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

    term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        mask=cv2.blur(mask,(5,5))
        _, mask = cv2.threshold(mask, 100, 255, cv2.THRESH_BINARY)
        # mask = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv2.CamShift(mask, (x, y, width, height), term_criteria)
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        cv2.polylines(frame, [pts], True, (255, 0, 0), 2)
        cv2.imshow("mask", mask)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()