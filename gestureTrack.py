import cv2
import numpy as np
from pynput.mouse import Button, Controller
import tkinter as tk


mouse = Controller()
root = tk.Tk()

sx = root.winfo_screenwidth()
sy = root.winfo_screenheight()
(camx, camy) = (320, 240)

lowerBound = np.array([20, 100, 50])
upperBound = np.array([100, 255, 255])

cam = cv2.VideoCapture(0)
cam.set(3, camx)
cam.set(4, camy)

kernelOpen = np.ones((5, 5))
kernelClose = np.ones((20, 20))

while True:
    ret, img = cam.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHSV, lowerBound, upperBound)
    maskOpen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOpen)
    maskClose = cv2.morphologyEx(maskOpen, cv2.MORPH_CLOSE, kernelClose)

    maskFinal = maskClose
    _, conts, h = cv2.findContours(maskFinal.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if (len(conts) == 2):
        mouse.release(Button.left)
        x1, y1, w1, h1 = cv2.boundingRect(conts[0])
        x2, y2, w2, h2 = cv2.boundingRect(conts[1])
        cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
        cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (0, 255, 0), 2)
        cx1 = int(x1 + w1 / 2)
        cy1 = int(y1 + h1 / 2)
        # centre coordinate of the 2nd object
        cx2 = int(x2 + w2 / 2)
        cy2 = int(y2 + h2 / 2)
        # centre coordinate of the line connection both points
        cx = int((cx1 + cx2) / 2)
        cy = int((cy1 + cy2) / 2)
        # Drawing the line
        # cv2.line(img, (cx1, cy1), (cx2, cy2), (255, 0, 0), 2)
        # Drawing the point (red dot)
        # cv2.circle(img, (cx, cy), 2, (0, 255, 0), 5)
        mouse.position = (sx - (int(cx * sx / camx)), int(cy * sy / camy))
        while mouse.position != (sx - (int(cx * sx / camx)), int(cy * sy / camy)):
            pass

    elif (len(conts) == 1):
        x, y, w, h = cv2.boundingRect(conts[0])
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        a = int((w + h) / 4)
        # cv2.circle(img,(cx,cy), a,(0,0,255),2)
        mouse.position = (sx - (int(cx * sx / camx)), int(cy * sy / camy))
        while mouse.position != (sx - (int(cx * sx / camx)), int(cy * sy / camy)):
            pass
        mouse.press(Button.left)

    cv2.imshow('new', img)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
