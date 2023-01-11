#Script to convert pdf files into images

from pdf2image import convert_from_path

INPUT_PATH = "InputData/"
OUTPUT_PATH = "ImageData/"

def toJpg(inputName):
    images = convert_from_path(INPUT_PATH+inputName)
    for i in range(len(images)):
        images[i].save(OUTPUT_PATH+inputName[:-4]+"_page"+ str(i) +'.jpg', 'JPEG')