import cv2 
import pytesseract 
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract' 
img = cv2.imread('meter.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0) 
bin_img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

kernel = np.ones((1, 1), np.uint8) 
img = cv2.dilate(bin_img, kernel, iterations=1) 
img = cv2.erode(img, kernel, iterations=1) 
text = pytesseract.image_to_string(img) 

print(text) 