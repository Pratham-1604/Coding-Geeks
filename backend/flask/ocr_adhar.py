# -*- coding: utf-8 -*-
"""OCR Adhar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZmGFX0eFvmRTKkOwH-RddL2YAMAF8A95
"""

# Install pytesseract and tesseract-ocr

# On Windows, you don't need to install tesseract-ocr separately
# pytesseract will use its bundled version

# Import necessary libraries
import cv2
import pytesseract

# Set the path to the Tesseract executable
# On Windows, you typically don't need to specify this
pytesseract.pytesseract.tesseract_cmd = "./tesseract.exe"  # Example path

# Load the image from Google Drive
image_path = "./image.png"
img = cv2.imread(image_path)

# Preprocess the image (you may need to customize this based on the specific needs of Aadhar cards)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Additional preprocessing steps can be added here

# Use Tesseract OCR to extract text
custom_config = r"--oem 3 --psm 6"  # Adjust OCR settings as needed
text = pytesseract.image_to_string(gray, config=custom_config)

# # Print the extracted text
print("Extracted Text:")
print(text)

if ("Female" or "FEMALE") in text:
    print("Gender: Female")
else:
    print("Gender: Male")

# Implement further processing to extract name and gender based on the OCR results
# Additional code for text cleaning, tokenization, and information extraction can be added here