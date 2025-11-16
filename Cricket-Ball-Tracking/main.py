import cv2 as cv
import numpy as np

def create_kalman():
    kf = cv.KalmanFilter(4, 2)
    kf.measurementMatrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0]
    ], np.float32)
    kf.transitionMatrix = np.array([
        [1, 0, 0.5, 0],
        [0, 1, 0, 0.5],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ], np.float32)
    kf.processNoiseCov = np.eye(4, dtype=np.float32) * 1e-3
    kf.measurementNoiseCov = np.eye(2, dtype=np.float32) * 1e-2
    return kf


def pink_ball_mask(frame):
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower1 = np.array([0, 120, 70])
    upper1 = np.array([12, 255, 255])

    lower2 = np.array([140, 90, 60])
    upper2 = np.array([179, 255, 255])

    mask1 = cv.inRange(hsv, lower1, upper1)
    mask2 = cv.inRange(hsv, lower2, upper2)
    mask = cv.bitwise_or(mask1, mask2)

    white_mask = cv.inRange(hsv, (0, 0, 180), (179, 40, 255))
    mask = cv.bitwise_and(mask, cv.bitwise_not(white_mask))

    k = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, k, iterations=1)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, k, iterations=1)

    mask = cv.GaussianBlur(mask, (7, 7), 0)
    return mask


def detect_ball(mask):
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    best = None
    best_r = 0
    for c in contours:
        area = cv.contourArea(c)
        if area < 20 or area > 2500:
            continue
        (x, y), r = cv.minEnclosingCircle(c)
        if r < 3 or r > 35:
            continue
        per = cv.arcLength(c, True)
        circularity = 4 * np.pi * area / (per * per + 1e-6)
        if circularity < 0.4:
            continue
        if r > best_r:
            best_r = r
            best = (int(x), int(y), int(r))
    return best


video_path = r"D:\PythonProgramsuwu\DIP project\cummins.mp4"
cap = cv.VideoCapture(video_path)

kalman = create_kalman()
locked = False
last_detection = None

while True:
    ret, frame = cap.read()
    if not ret:
        break   # end or weird read
    mask = pink_ball_mask(frame)
    detection = detect_ball(mask)
    if detection is not None:
        x, y, r = detection
        if not locked:
            kalman.statePre = np.array([[x], [y], [0], [0]], np.float32)
            locked = True  # finally locked on
        kalman.correct(np.array([[x], [y]], np.float32))
        last_detection = (x, y, r)
    if locked:
        pred = kalman.predict()
        px, py = int(pred[0]), int(pred[1])
        cv.circle(frame, (px, py), 5, (0, 255, 255), 2)  # predicted
    if last_detection is not None:
        x, y, r = last_detection
        cv.circle(frame, (x, y), r, (0, 0, 255), 2)  # actual ball
    cv.imshow("Mask", mask)
    cv.imshow("Tracking", frame)
    if cv.waitKey(40) & 0xFF == ord('q'):
        break   
cap.release()
cv.destroyAllWindows()