#Script to convert different types of files into jpgs

import PIL as pil
import os
import pdf2image
import subprocess

INPUT_PATH = "InputData/"
OUTPUT_PATH = "ImageData/"

def pdftoJpg(inputName):
    # load the pdf file
    images = pdf2image.convert_from_path(INPUT_PATH+inputName)
    
    # loop through the pages and convert them to jpg images
    for i in range(len(images)):
        images[i].save(OUTPUT_PATH+inputName[:-4]+"_page"+str(i)+'.jpg', 'JPEG')

def docxtoJpg(inputName):

    #convert the docx to a pdf usiing abiword
    bashCommand = "abiword --to=pdf "+INPUT_PATH+inputName
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    
    #convert the pdf to jpg
    pdftoJpg(inputName[:-4]+"pdf")
    
    #delete the newly created pdf
    bashCommand = "rm "+INPUT_PATH+inputName[:-4]+"pdf"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)

def pngtoJpg(inputName): 
    #open image in png format
    img_png = pil.Image.open(INPUT_PATH+inputName)
    
    #The image object is used to save the image in jpg format
    img_png.save(OUTPUT_PATH+inputName[:-4]+"_page"+ str(0) +'.jpg', 'JPEG')

def jpegtoJpg(inputName):
    #open image in jpeg format
    img_jpeg = pil.Image.open(INPUT_PATH+inputName)

    #The image object is used to save the image in jpg format
    img_jpeg.save(OUTPUT_PATH+inputName[:-5]+"_page"+ str(0) +'.jpg', 'JPEG')

def jpgtoJpg(inputName):
    #open image in jpeg format
    img_jpeg = pil.Image.open(INPUT_PATH+inputName)

    #The image object is used to save the image in jpg format
    img_jpeg.save(OUTPUT_PATH+inputName[:-4]+"_page"+ str(0) +'.jpg', 'JPEG')

if __name__=="__main__":
    #get the list of all files in input
    inputData = os.listdir(INPUT_PATH)
    print(str(inputData))

    #convert each file to jpg format
    for i in inputData:
        extension = i.rpartition(".")[2]
        if extension=="png":
            pngtoJpg(i)
        elif extension=="pdf":
            pdftoJpg(i)
        elif extension=="docx":
            docxtoJpg(i)
        elif extension=="jpeg":
            jpegtoJpg(i)
        elif extension=="jpg":
            jpgtoJpg(i)
        else:
            raise Exception("Invalid extension format of the type " + extension)
            
