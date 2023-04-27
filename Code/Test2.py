import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pytesseract
# import tensorflow as tf

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR"

file = "F:\\Lecture notes\\Sem-8\\MP(8)\\Code\\ka.jpeg"

img = cv2.imread(file)
cv2.imshow("image", img)
cv2.resize(img, (320, 320))
cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("image2", thresh2)
cv2.waitKey(0)
