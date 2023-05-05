import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytesseract
# import tensorflow as tf

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

file = "F:\\Lecture notes\\Sem-8\\MP(8)\\Resources\\Handwriting3.jpg"
img =cv2.imread(file)
# img = cv2.resize(img, None, fx= 0.3, fy= 0.3) 
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 11)

print(pytesseract.image_to_string(img, lang= 'hin'))

cv2.imshow("image", img)
cv2.waitKey(0)
