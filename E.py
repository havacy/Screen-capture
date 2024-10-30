import cv2
import numpy as np
import pyscreeze

x1, y1 = 836, 444
x2, y2 = 1050, 640

def capture_region(x1, y1, x2, y2):
    screenshot = pyscreeze.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    frame = np.array(screenshot)
    return frame

while True:
    frame = capture_region(x1, y1, x2, y2)


    cv2.imshow("Capture Region", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
