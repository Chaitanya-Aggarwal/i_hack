# text recognition
import cv2
import pytesseract
import os

INPUT_PATH = "ImageDatas/"

#Loading the files
inputData = os.listdir(INPUT_PATH)
print("The input image files are")
print(inputData)

for i in inputData:
    # read image
    img = cv2.imread(INPUT_PATH+i)

    # configurations
    config = ('-l eng --oem 1 --psm 3')

    # pytessercat
    text = pytesseract.image_to_string(img, config=config)

    # print text
    text = text.split('\n')
    print(text)