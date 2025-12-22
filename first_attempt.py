import cv2
import pytesseract
from PIL import Image, ImageOps, ImageFilter

# Set the path to the Tesseract executable (change this to your installation path)
# Example for Windows: r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Step 1: Load the image using OpenCV
image = Image.open('sample3.png')

# Step 2: Convert the image to grayscale to improve accuracy
#gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = ImageOps.grayscale(image)

#thresholded_image = gray_image.filter(ImageFilter.FIND_EDGES)

#gray_image.show()
#thresholded_image.show()

#sharpened_image = gray_image.filter(ImageFilter.SHARPEN)
#sharpened_image.show()

# Step 3: Use pytesseract to perform OCR on the processed image
text = pytesseract.image_to_string(gray_image, config='--psm 11')
#text = pytesseract.image_to_string(gray_image)

# Step 4: Print the extracted text
print("Extracted Text:", text)

