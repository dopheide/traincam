#!/usr/bin/env python3

import cv2
import pytesseract
import os
import re

def TestWorks():
    return True

def scale_and_gray(image):

    # Upscale because this was breaking shit the image was too small
    scale_factor = 4
    width = int(image.shape[1] * scale_factor)
    height = int(image.shape[0] * scale_factor)
    upscaled = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)

    # this works better in grayscale
    gray = cv2.cvtColor(upscaled, cv2.COLOR_BGR2GRAY)
    return gray

def gray_to_thresh(gray):
    # threshold (this worked best in testing)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return thresh

def no_really(gray):
    _, thresh = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)

#    cv2.imshow('blaa',thresh)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    return thresh

def extract_train_numbers(image):
    config = '--psm 11 -c tessedit_char_whitelist=0123456789'
#    config = '--psm 11'
    result = pytesseract.image_to_string(image, config=config)
#    digits = ''.join(filter(str.isdigit, result))
    results = result.split('\n')
    numbers = list()
    for r in results:
        if len(r) == 4 and r.isdigit():
            numbers.append(int(r))

    return numbers

def ProcessTrain(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Could not read image: {image_path}")

    print(f"Processing {image_path}...")
    gray = scale_and_gray(img)
    thresh = gray_to_thresh(gray)

    # threshold results are better for train 2875 (otherwise it shows 2675)
    # but just gray is better for others.

    numbers = extract_train_numbers(thresh)
    if(len(numbers) != 1):
        numbers = extract_train_numbers(gray)

    if(len(numbers) != 1):
        # get crazy.  This seems to work for black numbers on a red/orange train.
        thresh = no_really(gray)
        numbers = extract_train_numbers(thresh)
    
    return numbers

def main():
    image_dir_path = "trains"
    dl = os.listdir(image_dir_path)

    for f in dl:
        m = re.search(r'^([0-9]+)\.png',f)
        if(m):
            train_num = int(m.group(1))

            try:
                image_path = image_dir_path + "/" + f

                numbers = ProcessTrain(image_path)

                if(train_num in numbers):
                    status=True
                else:
                    status=False
                print(f"Train Number: {numbers}  {status}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
