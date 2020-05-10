import numpy as np
import cv2

img = cv2.imread('./1024473.png',1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()