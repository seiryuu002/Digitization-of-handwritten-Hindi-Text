import cv2
import io
from deskew import determine_skew
import numpy as np
from PIL import Image
import pytesseract
import sys
from skimage import io as ioski
from skimage.transform import rotate, resize
import os
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
from dotenv import load_dotenv, find_dotenv

credential_path = 'F:\\Lecture notes\\Sem-8\\MP(8)\\Code\\dizitizationofhinditext-4073208d099d.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
client = vision_v1.ImageAnnotatorClient()

dirpath = os.getcwd()

class PreProcessor:


    def getImage(self, image):

        image = ioski.imread(image)
        return image
    

    def deskewImage(self, imageSkewed):

        angle = determine_skew(imageSkewed)
        rotated = rotate(imageSkewed, angle, resize=True) * 255
        return rotated
    

    def preProcessImage(self, deskewedImage):

        image = cv2.resize(deskewedImage, None, fx=.3, fy=.3)
        image = cv2.cvtColor(image.astype('uint8'), cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
        dilate = cv2.dilate(opening, kernel, iterations=1)
        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            area = cv2.contourArea(c)
            if area < 50:
                cv2.drawContours(dilate, [c], -1, 0, -1)
        result = 255 - dilate
        result = cv2.GaussianBlur(result, (3, 3), 0)
        cv2.imwrite(dirpath + "\\Resources\\output_processed.png", result)
        path = dirpath + "\\Resources\\output_processed.png"
        return result, path


    def digitizer(self, imagePath):
        data = pytesseract.image_to_string(imagePath, lang='hin', config='--psm 6')
        print(data)
        with open('output.txt', "w", encoding="utf-8") as f:
            f.write(data)
        f.close()
    
    
    def Digitizer(self, imagePath):
        with io.open(imagePath, 'rb') as image_file:
            content = image_file.read()
        image_v = vision_v1.types.Image(content=content)
        response = client.document_text_detection(image=image_v)
        docText = response.full_text_annotation.text
        with open('output.txt', "w", encoding="utf-8") as f:
            f.write(docText)
        f.close() 
        return docText

        
