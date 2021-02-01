import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('your_file_path.jpg', 1)
img=cv2.line(img, (0,0), (255,255), (255,0,0), 15)
img=cv2.arrowedLine(img, (0,255), (255,255), (255,0,0), 10)
img=cv2.rectangle(img, (304, 0), (510, 128), (0,0,255), 10)
img=cv2.circle(img, (447,63), 63, (0,0,255), -1)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img, 'Lakshman', (10, 500), font, 4, (255,255,255))
cv2.imshow('test', img)
plt.imshow(img)
plt.show()
